from discord.ext import commands
import asyncpg


class Database(commands.Cog):
    """Database related code and tools"""
    def __init__(self, bot):
        self.bot = bot
        bot.database = self
        bot.logger.info("Initialized Database cog")

    async def log_direct_messages(self, message):
        conn = await asyncpg.connect(dsn="postgres://stavlorkaralain_gmail_com@localhost/bot", password="1234")
        sqlstatement = "INSERT INTO pm_tracking (user_id, user_name, message) VALUES ('{user_id}', '{user_name}{user_discriminator}', '{message}')".format(user_id=message.author.id, user_name=message.author.name, message=message.content, user_discriminator=message.author.discriminator);
        await conn.execute(sqlstatement)
        await conn.close()

def setup(bot):
    bot.add_cog(Database(bot))