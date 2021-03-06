from aiohttp import web
import asyncio
import discord
from discord.ext import commands


class BotWebserver(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.web = self
        self.site = None
        self.bot.logger.info("Web Cog Loaded, will start webserver in on ready.")

    async def handler(self, request):
        self.bot.logger.debug(f"WEB: Got GET / {request}")
        return web.Response(
            text="Greetings from the Bot Rexford's internal webserver this feature is still under development."
        )

    async def handle_github(self, request):
        import json
        headers = request.headers
        content = await request.post()
        event_type = headers.getone('X-GitHub-Event')
        payload = json.loads(content.getone('payload'))
        channel = await self.bot.fetch_channel(738097347916988447)
        if 'push' == event_type:
            branch = payload['ref'].replace('refs/heads/', '')
            user = payload['sender']['login']
            embed = discord.Embed(title=f"New Commits Pushed to {branch} by {user}", color=0x26a781)
            await channel.send(embed=embed)
            self.bot.logger.debug("WEB: GITHUB: Processed push Event.")
        elif 'issues' == event_type:
            action = payload['action']
            issue_title = payload['issue']['title']
            issue_url = payload['issue']['html_url']
            issue_number = payload['issue']['number']
            user = payload['sender']['login']
            embed = discord.Embed(title=f"User {user} {action} an issue #{issue_number}", url=issue_url, color=0x37ada1)
            embed.add_field(name="Issue Title:", value=issue_title)
            await channel.send(embed=embed)
            self.bot.logger.debug("WEB: GITHUB: Processed issues Event.")
        elif 'issue_comment' == event_type:
            action = payload['action']
            issue_title = payload['issue']['title']
            issue_url = payload['issue']['html_url']
            issue_number = payload['issue']['number']
            user = payload['sender']['login']
            embed = discord.Embed(title=f"User {user} {action} an issue comment on issue #{issue_number}", url=issue_url, color=0x37ada1)
            embed.add_field(name="Issue Title:", value=issue_title)
            await channel.send(embed=embed)
            self.bot.logger.debug("WEB: GITHUB: Processed issue_comment Event.")
        elif 'pull_request' == event_type:
            action = payload['action']
            number = payload['number']
            title = payload['pull_request']['title']
            pull_url = payload['pull_request']['html_url']
            body = payload['pull_request']['body']
            user = payload['sender']['login']
            embed = discord.Embed(title=f"User {user} {action} pull request number #{number}", url=pull_url, color=0x37ada1)
            embed.add_field(name="Pull Request Title:", value=title)
            embed.add_field(name="Pull Request Body:", value=body)
            await channel.send(embed=embed)
        self.bot.logger.info(f"WEB: GITHUB EVENT {event_type} Keys recieved. {payload.keys()}")
        self.bot.logger.debug(f"WEB: GITHUB EVENT CONTENT: {content}")
        return web.Response(text="Event Recieved.")

    async def webserver(self):
        app = web.Application()
        app.router.add_get('/', self.handler)
        app.router.add_post('/github', self.handle_github)
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, '104.131.86.125', 8099)
        await self.bot.wait_until_ready()
        await self.site.start()

    def __unload__(self):
        asyncio.ensure_future(self.site.stop())


def setup(bot):
    bot.add_cog(BotWebserver(bot))
