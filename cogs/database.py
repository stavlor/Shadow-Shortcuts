from discord.ext import commands
import asyncpg


class Database(commands.Cog):
    """Database related code and tools"""
    def __init__(self, bot):
        self.bot = bot
        bot.database = self
        bot.dblogger = bot.logging_root.getLogger("database")
        self.logger = bot.dblogger
        bot.logger.info("Initialized Database cog")

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Moderators')
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
    @commands.has_any_role('Shadow Guru', 'Moderators')
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
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
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
        await conn.execute(sqlstatement)
        await conn.close()

    async def update_leaver_roles(self, member):
        role_list = list()
        role_str = str()
        if member.guild.id != 460948857304383488:
            self.bot.logger.info(f"Ignoring leaver not in our guild of interest {member.id} left guild {member.guild.id}.")
            return
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
        if hasattr(member, 'roles'):
            for role in member.roles:
                role_list.append(role.id)
        for item in role_list:
            role_str += f"{item},"
        SQL = f"INSERT INTO role_tracking(discord_id, roles) VALUES('{member.id}', '{role_str}') ON CONFLICT (discord_id) DO UPDATE SET roles='{role_str}';"
        self.logger.info(f"SQL: {SQL}")
        await conn.execute(SQL)
        await conn.close()

    async def re_apply_roles(self, member):
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
        roles = list()
        applied_roles = list()
        if member.guild.id != 460948857304383488:
            self.bot.logger.info(f"Ignoring leaver not in our guild of interest {member.id} left guild {member.guild.id}.")
            return
        SQL = f"SELECT roles FROM role_tracking WHERE discord_id='{member.id}' LIMIT 1;"
        res = await conn.fetch(SQL)
        if len(res) != 0:
            res = res.pop()
        else:
            return
        res = dict(res)
        await conn.close()
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
