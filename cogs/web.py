from aiohttp import web
import asyncio
import discord
from discord.ext import commands


class BotWebserver(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.site = None

    async def webserver(self):
        async def handler(request):
            return web.Response(text="Hello, world")

        app = web.Application()
        app.router.add_get('/', handler)
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, '157.245.134.212', 8099)
        await self.bot.wait_until_ready()
        await self.site.start()

    def __unload__(self):
        asyncio.ensure_future(self.site.stop())


def setup(bot):
    webserver = BotWebserver(bot)
    bot.add_cog(web)
    bot.loop.create_task(webserver.webserver())
