from aiohttp import web
from discord.ext import commands
import discord
import typing


class Web(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.web = self
        bot.logger.info("Initializing Web Cog")
        self.bot.web.routes = web.RouteTableDef()
        self.bot.web.application = web.Application()
        self.bot.web.application.add_routes(self.bot.web.routes)
        web.run_app(self.bot.web.application)

    @self.bot.web.routes.get('/')
    async def hello(self, request):
        return web.Response(text="Hello World")


def setup(bot):
    bot.add_cog(Web(bot))