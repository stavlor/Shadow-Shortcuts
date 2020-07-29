from aiohttp import web
import asyncio
from discord.ext import commands


class BotWebserver(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.site = None
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.webserver())

    @staticmethod
    async def handler(request):
        return web.Response(
            text="Greetings from the Bot Rexford's internal webserver this feature is still under development."
        )

    async def webserver(self):
        app = web.Application()
        app.router.add_get('/', self.handler)
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, '157.245.134.212', 8099)
        await self.bot.wait_until_ready()
        await self.site.start()

    def __unload__(self):
        asyncio.ensure_future(self.site.stop())


def setup(bot):
    bot.add_cog(BotWebserver(bot))
