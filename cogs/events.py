from discord.ext import commands
import discord


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.logger.info("Initialized Events Cog")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            ctx.send("{author.mention} {exception}".format(author=ctx.author, exception=exception))
        await ctx.message.add_reaction("😢")
        self.bot.logger.info(
            "Error encountered processing command enacting message: {ctx.message} enacting user: {ctx.author.name} Exception: {exception}".format(
                ctx=ctx, exception=exception))

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info("Bot Starting up.. Logged in as:" + str(self.bot.user.name) + " ID: " + str(self.bot.user.id))

    @commands.Cog.listener()
    async def on_message(self, message):
        self.bot.logger.debug("Recieved message from {message.author} Content {message.content}".format(message=message))
        author = message.author
        if not hasattr(author, 'roles'):
            role_names = []
        else:
            role_names = author.roles
        if message.author.id == self.bot.user.id:
            pass
        elif "good bot" in message.content.lower():
            await message.add_reaction("🍪")
            await message.add_reaction("👍")
        elif "bad bot" in message.content.lower():
            await message.add_reaction("😢")
            await message.add_reaction("🖕🏼")
        elif "error 102" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png",
                                        trigger="error 102")
        elif "102 error" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png",
                                        trigger="102 error")
        elif "800x600" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png",
                                        trigger="800x600")
        elif "input lag" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following tips for solving input lag issues http://core.stavlor.net/inputlag.png",
                                        trigger="input lag")
        elif "password expired" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following for expired password messages http://core.stavlor.net/password.png",
                                        trigger="password expired")
        elif "expired password" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following for expired password messages http://core.stavlor.net/password.png",
                                        trigger="password expired")
        elif "waiting for video" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png",
                                        trigger="waiting for video")
        elif "video error" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png",
                                        trigger="waiting for video")
        elif "long to boot up" in message.content.lower() and not await bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png",
                                        trigger="waiting for video")
        elif "3/3" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                        message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png",
                                        trigger="3/3")

def setup(bot):
    bot.add_cog(Events(bot))