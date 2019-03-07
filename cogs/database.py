from discord.ext import commands
import discord
import asyncpg

class Database(commands.Cog):
    """Database related code and tools"""
    def __init__(self, bot):
        self.bot = bot
        bot.database = self
        bot.logger.info("Initialized Database cog")

    async def log_direct_messages(self, message):
        conn = asyncpg.connect()