from discord.ext import commands
import discord
import asyncpg
import asyncio


class Database(commands.Cog):
    """Database related code and tools"""
    def __init__(self, bot):
        self.bot = bot
        bot.database = self
        bot.dblogger = bot.logging_root.getLogger("database")
        loop = asyncio.get_event_loop()
        bot.dbpool = loop.run_until_complete(asyncpg.create_pool(dsn=self.bot.config.SQLDSN, min_size=5, max_size=50, password=self.bot.config.SQLPASS))
        self.logger = bot.dblogger
        bot.logger.info("Initialized Database cog")

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def sql(self, ctx, *, arguments):
        """Admin SQL Tool"""
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send("{ctx.author.mention} your not authorized to do that.".format(ctx=ctx))
            return
        self.logger.info("SQL: {sql}".format(sql=str(arguments)))
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
        sql = str(arguments)
        await conn.execute(sql)
        await conn.close()

    @commands.command(aliases=['cleanpms'])
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def clean_pm_tracking(self, ctx, *, arguments = None):
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send("{ctx.author.mention} your not authorized to do that.".format(ctx=ctx))
            return
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
        sql = 'TRUNCATE pm_tracking;'
        self.logger.info(f"PM Tracking cleared by {ctx.author.name} --")
        await conn.execute(sql)
        await conn.close()
        await ctx.send(f"{ctx.author.mention} PMs have been cleared.")
        await ctx.message.delete()

    async def log_direct_messages(self, message):
        attach_url = None
        if hasattr(message, 'attachments'):
            attach_url = str()
            for attach in message.attachments:
                attach_url += "<a href=\""+str(attach.url)+"\">Attachment</a> "
        rmessage = message.content
        rmessage = rmessage.replace("'", "\'")
        rmessage = rmessage.replace('"', '\"')
        sqlstatement = "INSERT INTO pm_tracking (user_id, user_name, message, attachment_url) VALUES ('{user_id}', '{user}', '{message}', '{attachment_url}')".format(user_id=message.author.id, user=str(message.author), message=rmessage, attachment_url=attach_url);
        self.logger.info("SQL: {sql}".format(sql=sqlstatement))
        async with self.bot.dbpool.acquire() as connection:
            await connection.execute(sqlstatement)

    async def update_leaver_roles(self, member):
        role_list = list()
        role_str = str()
        if member.guild.id != 460948857304383488:
            self.bot.logger.info(f"Ignoring leaver not in our guild of interest {member.id} left guild {member.guild.id}.")
            return
        if hasattr(member, 'roles'):
            for role in member.roles:
                role_list.append(role.id)
        for item in role_list:
            role_str += f"{item},"
        SQL = f"INSERT INTO role_tracking(discord_id, roles) VALUES('{member.id}', '{role_str}') ON CONFLICT (discord_id) DO UPDATE SET roles='{role_str}';"
        async with self.bot.dbpool.acquire() as connection:
            await connection.execute(SQL)

    async def find_database_record(self, hash):
        if hash is None:
            return None
        sql = f"SELECT * from game_tracking WHERE app_id='{hash}' LIMIT 1;"
        async with self.bot.dbpool.acquire() as connection:
            res = await connection.fetch(sql)
        if len(res) != 0:
            res = res.pop()
        else:
            return None
        res = dict(res)
        return res

    async def create_database_record(self, dataset):
        if dataset['id'] is None:
            return
        elif dataset['id'] == 0:
            return
        title = dataset['title']
        title = title.replace("'", "\'")
        title = title.replace('"', '\"')
        sql = f"INSERT INTO game_tracking (app_id, title, players) VALUES ('{dataset['id']}', '{title}', '{dataset['players']}');"
        try:
            async with self.bot.dbpool.acquire() as connection:
                await connection.execute(sql)
        except:
            self.bot.logger.info(f"error encountered SQL: {sql}")



    async def update_database_record(self, dataset):
        sql = f"UPDATE game_tracking SET players='{dataset['players']}', time_played='{dataset['time_played']}' WHERE app_id='{dataset['id']}';"
        async with self.bot.dbpool.acquire() as connection:
            await connection.execute(sql)

    async def process_member_update(self, before: discord.Member, after: discord.Member):
        prior = None
        current = None
        if after.guild.id != 460948857304383488:
            return
        if before.activity != after.activity:
            prior = before.activity
            current = after.activity
            if before.activity is None:
                prior = None
                current = after.activity
                if hasattr(prior, 'application_id'):
                    papp_id = prior.application_id
                else:
                    papp_id = None
                if hasattr(current, 'application_id'):
                    capp_id = current.application_id
                else:
                    capp_id = None
                if current.type == "ActivityType.streaming":
                    self.bot.logger.info(f"DBG: M:{after.id} has started streaming URL: {current.url}")
                elif current.type == "ActivityType.listening":
                    self.bot.logger.info(f"DBG: M:{after.id} has started listening to Spotify: S:{current.title} Ar:{current.artist} Al: {current.album} TID:{current.track_id}")
                else:
                    rec = await self.find_database_record(capp_id)
                    if rec is None:
                        dataset = dict()
                        dataset['id'] = capp_id
                        if dataset['id'] is None:
                            dataset['id'] = 0
                        dataset['title'] = current.name
                        dataset['players'] = list()
                        dataset['players'].append(after.id)
                        await self.create_database_record(dataset)
                    else:
                        import json, datetime
                        dataset = dict()
                        dataset['id'] = capp_id
                        if dataset['id'] is None:
                            dataset['id'] = 0
                        dataset['title'] = current.name
                        dataset['players'] = json.loads(rec['players'])
                        dataset['time_played'] = datetime.timedelta()
                        if after.id not in dataset['players']:
                            dataset['players'].append(after.id)
                        dataset['players'] = json.dumps(dataset['players'])
                        await self.update_database_record(dataset)
            elif after.activity is None:
                current = None
                prior = before.activity
                if prior.type == "ActivityType.streaming":
                    self.bot.logger.info(f"DBG: M:{after.id} has stopped streaming.")
                elif prior.type == "ActivityType.listening":
                    self.bot.logger.info(f"DBG: M:{after.id} has stopped listening to Spotify.")
                else:
                    if hasattr(prior, 'application_id'):
                        app_id = prior.application_id
                    else:
                        app_id = 0
                    rec = await self.find_database_record(app_id)
                    if rec is None:
                        pass
                    else:
                        import datetime
                        now = datetime.datetime.now()
                        before = prior.start
                        if before is None:
                            playtime = datetime.timedelta()
                        else:
                            delta = before - now
                            playtime = rec['time_played']
                            if playtime is None:
                                playtime = delta
                            elif isinstance(playtime, datetime.time):
                                playtime = datetime.timedelta(hours=playtime.hour, minutes=playtime.minute, seconds=playtime.second, microseconds=playtime.microsecond)
                            else:
                                playtime += playtime + delta
                        dataset = dict()
                        dataset['id'] = capp_id
                        if dataset['id'] is None:
                            dataset['id'] = 0
                        dataset['title'] = current.name
                        dataset['players'] = json.loads(rec['players'])
                        dataset['time_played'] = datetime.timedelta()
                        if after.id not in dataset['players']:
                            dataset['players'].append(after.id)
                        dataset['players'] = json.dumps(dataset['players'])
                        await self.update_database_record(dataset)
            elif before.name == after.name:
                if hasattr(prior, 'application_id'):
                    papp_id = prior.application_id
                else:
                    papp_id = 0
                if hasattr(current, 'application_id'):
                    capp_id = current.application_id
                else:
                    capp_id = 0
                if current.type == "ActivityType.listening":
                    self.bot.logger.info(f"DBG SSW: M:{after.id} Spotify Song change: S:{current.title} Ar:{current.artist} Al: {current.album} TID:{current.track_id}")
                elif current.type == "ActivityType.streaming":
                    self.bot.logger.info(f"DBG StrIG: M:{after.id} U:{current.url}")
                else:
                    pass
            else:
                if hasattr(prior, 'application_id'):
                    papp_id = prior.application_id
                else:
                    papp_id = 0
                if hasattr(current, 'application_id'):
                    capp_id = current.application_id
                else:
                    capp_id = 0
                if prior.type is "ActivityType.listening":
                    self.bot.logger.info(f"DBG S2G: M:{after.id} G: {current.name} AH: {current.application_id}")
                else:
                    rec = await self.find_database_record(capp_id)
                    if rec is None:
                        dataset = dict()
                        dataset['id'] = capp_id
                        if dataset['id'] is None:
                            dataset['id'] = 0
                        dataset['title'] = current.name
                        dataset['players'] = list()
                        dataset['players'].append(after.id)
                        await self.create_database_record(dataset)
                    else:
                        import json, datetime
                        dataset = dict()
                        dataset['id'] = capp_id
                        if dataset['id'] is None:
                            dataset['id'] = 0
                        dataset['title'] = current.name
                        dataset['players'] = json.loads(rec['players'])
                        dataset['time_played'] = datetime.timedelta()
                        if after.id not in dataset['players']:
                            dataset['players'].append(after.id)
                        dataset['players'] = json.dumps(dataset['players'])
                        await self.update_database_record(dataset)
                    self.bot.logger.info(f"DBG G2G Swap M: {after.id} P:{prior.name} A:{current.name} PH:{papp_id} AH: {capp_id}")

    async def re_apply_roles(self, member):
        roles = list()
        applied_roles = list()
        if member.guild.id != 460948857304383488:
            self.bot.logger.info(f"Ignoring leaver not in our guild of interest {member.id} left guild {member.guild.id}.")
            return
        SQL = f"SELECT roles FROM role_tracking WHERE discord_id='{member.id}' LIMIT 1;"
        async with self.bot.dbpool.acquire() as connection:
            res = await connection.fetch(SQL)
        if len(res) != 0:
            res = res.pop()
        else:
            return
        res = dict(res)
        if res is not None:
            roles = res['roles']
            self.bot.logger.info(f"User {member.id} Has prior roles, reapplying.Found roles: {roles}")
            roles = roles.split(',')
            for item in roles:
                if item is not None:
                    if item == '':
                        continue
                    role = member.guild.get_role(int(item))
                    if role.name == "@everyone":
                        continue
                    if role is not None:
                        applied_roles.append(role)
                        await member.add_roles(role, reason="Re-Applying leaver's roles.")
        self.bot.logger.info(f"Leaver roles applied, for ({member.id}){member.name} Roles-applied: {applied_roles}")


def setup(bot):
    bot.add_cog(Database(bot))
