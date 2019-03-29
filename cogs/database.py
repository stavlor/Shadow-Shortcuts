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
    async def clean_pm_tracking(self, ctx, *, arguments = None):
        conn = await asyncpg.connect(dsn=self.bot.config.SQLDSN, password=self.bot.config.SQLPASS)
        sql = 'TRUNCATE pm_tracking;'
        self.logger.info(f"PM Tracking cleared by {ctx.author.name} --")
        await conn.execute(sql)
        await conn.close()

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

def setup(bot):
    bot.add_cog(Database(bot))