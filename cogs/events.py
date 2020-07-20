from discord.ext import commands, tasks
import discord
import traceback


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.events = self
        bot.logger.info("Initialized Events Cog")
        self.check_status.start()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.message.add_reaction("😢")
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            await ctx.author.send("{author.mention} {exception}".format(author=ctx.author, exception=exception))
            await ctx.message.add_reaction('✋')
        elif isinstance(exception, discord.ext.commands.errors.BadArgument):
            await ctx.send(
                "{author.mention} Bad Argument exception: {exception}".format(author=ctx.author, exception=exception))
        elif isinstance(exception, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("{author.mention} Required argument missing: {exception}".format(author=ctx.author,
                                                                                            exception=exception))
        elif isinstance(exception, discord.NotFound):
            await ctx.send("{author.mention} Got a discord.NotFound error: {exception}".format(author=ctx.author,
                                                                                               exception=exception))
        elif isinstance(exception, discord.ext.commands.CheckFailure):
            await ctx.send(f"{ctx.author.mention} You are not authorized to perform this command.")
        self.bot.logger.info(
            "Error encountered processing command enacting message: {ctx.message} enacting user: {ctx.author.name} Exception: {exception}\nTraceback:{traceback}".format(
                ctx=ctx, exception=exception, traceback=traceback.format_tb(exception.__traceback__)))

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info(
            "Bot Starting up.. Logged in as:" + str(self.bot.user.name) + " ID: " + str(self.bot.user.id))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.database.update_leaver_roles(member)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.database.re_apply_roles(member)

    @commands.Cog.listener()
    async def on_message(self, message):
        self.bot.logger.debug(
            "Recieved message from {message.author} Content {message.content}".format(message=message))
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id == self.bot.user.id:
                return
            if message.author.bot:
                return
            await self.bot.database.log_direct_messages(message)
            await message.author.send(
                "{message.author.mention} your message has been logged, This is an automated bot.".format(
                    message=message))
        if message.author.bot:
            return
        if not hasattr(message.author, 'roles'):
            role_names = []
        else:
            role_names = message.author.roles
        if message.author.id == self.bot.user.id:
            return  # Don't react to our own messages.
        elif message.role_mentions != list():
            if not await self.bot.admin.can_run_command(role_names):
                self.bot.logger.info(f"Role mentions: {message.role_mentions}")
                await message.channel.send(
                    f"{message.author.mention} Please don't mass tag, unless an absolute emergency. Thanks.")
        elif ("L:104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="L:104")
        elif ("L 104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="L 104")
        elif (" 104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="104")
        elif ("shadow is off" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="104")
        elif "800x600" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix issues with 800x600 resolution http://botrexford.shdw.info/800x600.png",
                                                             trigger="800x600")
        elif "input lag" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following tips for solving input lag issues http://botrexford.shdw.info/inputlag.png",
                                                             trigger="input lag")
        elif "password expired" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="""{ctx.author.mention} Ready-To-Go Password Update
If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903) - 

If you have any issues updating the default password is blank “” if your password is expired.""",
                                                             trigger="password expired")
        elif "expired password" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="""{ctx.author.mention} Ready-To-Go Password Update
            If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903) - 

            If you have any issues updating the default password is blank “” if your password is expired.""",
                                                             trigger="password expired")
        elif "waiting for video" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "video error" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "long to boot up" in message.content.lower() and not await bot.admin.can_run_command(role_names):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "3/3" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autorespone.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="3/3")
        elif "shadow is off" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                              message="{ctx.author.mention} Please follow the following steps to resolve your issue, Please access your help menu :grey_question: then scroll down and hit ***Shutdown Shadow***, then wait 2-5 minutes and restart your client to resolve your issue http://botrexford.shdw.info/reboot.gif ",
                                                              trigger="shadow is off")
        elif "valorant" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message, message="""{ctx.author.mention} Unfortunately, Valorant is not compatible with Shadow at this time. This is due to the nature of the game's "Vanguard" anti-cheat and how it is installed. Since Riot uses a custom anti-cheat mechanism, this makes it nearly impossible to run on virtual machines, including cloud platforms. 

This article might be helpful: <https://www.extremetech.com/gaming/309320-riot-games-new-anti-cheat-system-runs-at-system-boot-uses-kernel-driver>""")
        elif "good bot" in message.content.lower():
            await message.add_reaction("🍪")
            await message.add_reaction("👍")
        elif "bad bot" in message.content.lower():
            await message.add_reaction("😢")
            await message.add_reaction("🖕🏼")

    @tasks.loop(minutes=5.0)
    async def check_status(self):
        channel = await self.bot.get_channel(633713376316620829)
        msg = await channel.fetch_message(553765896666087442)
        if await self.bot.admin.get_status() == "All services operating normally":
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
            embed.add_field(name="All services operating normally",
                            value="For additional status information please see the status page", inline=True)
            await msg.edit(embed=embed)
        else:
            status = await self.bot.admin.get_status()
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0xff8040)
            embed.add_field(name=status,
                            value="For additional status information please see the status page", inline=True)
            await msg.edit(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        from datetime import datetime
        links = str()
        ignored_channels = ['bot_users', 'gurus-lab', 'bot-logs', 'known-issues', 'dariisas-deli']
        cur_time = datetime.now().isoformat()
        author = message.author
        content = message.content
        channel = message.channel
        if channel in ignored_channels:
            return
        if message.author.id == self.bot.user.id:
            return
        dest_channel = await self.bot.fetch_channel(462170485787066368)
        if message.content.startswith("\\"):
            return
        for attachment in message.attachments:
            links += attachment.url + ' '
        await dest_channel.send(f"Message was deleted {author} - {content} Attachments: {links}- in {channel} created: {message.created_at} edited: {message.edited_at} current_time: {cur_time}")


def setup(bot):
    bot.add_cog(Events(bot))
