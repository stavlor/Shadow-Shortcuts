from aiohttp import web
from discord.ext import commands
import discord
import typing
routes = web.RouteTableDef()

class Web(commands.Cog):
    def __init__(self, bot):
        global routes
        self.bot = bot
        bot.web = self
        botrefrence = self.bot
        bot.logger.info("Initializing Web Cog")
        self.bot.web.application = web.Application()
        self.bot.web.application.add_routes(routes)
        await web.run_app(self.bot.web.application)

    @routes.get('/')
    async def hello(self, request):
        return web.Response(text="Hello World")


def setup(bot):
    bot.add_cog(Web(bot))