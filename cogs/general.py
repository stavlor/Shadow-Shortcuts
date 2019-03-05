from discord.ext import commands
import discord


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.logger.info("Initialized General Cog")

    @commands.command(description="Send instructions on how to get Verified")
    async def verify(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Verify command received from {author.name} with argument of {user}".format(author=ctx.author,
                                                                                            user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} To get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nTo get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                        author=ctx.message.author))
        await ctx.message.delete()

    @commands.command(description="800x600 instructions", name="800x600")
    async def _800x600(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
                author=ctx.message.author, user=user))
            if user is not None:
                await ctx.send(
                    "From {author.name}\n{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From {author.name}\nPlease see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info(
                "Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
                    author=ctx.message.author,
                    user=user))
            await ctx.author.send(
                content="""{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Waiting for video instructions")
    async def waitingvideo(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
                author=ctx.message.author, user=user))
            if user is not None:
                await ctx.send(
                    "From {author.name}\n{user} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From {author.name}\nPlease see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info(
                "Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
                    author=ctx.message.author,
                    user=user))
            await ctx.author.send(
                content="""{user}  Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Error 102 Fix.")
    async def fix102(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "102 command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nPlease follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                        author=ctx.message.author))
        else:
            self.bot.logger.info("Error 102 Fix command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author,
                user=user))
            await ctx.author.send(
                content="""{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png""".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Default pass")
    async def password(self, ctx, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Password command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                              user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
                        author=ctx.message.author, user=user.mention))
            else:
                await ctx.send(
                    "From: {author.name}\nPlease see the following for expired password messages http://core.stavlor.net/password.png".format(
                        author=ctx.message.author))
        else:
            self.logger.info("Password command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author))
            await ctx.author.send(
                content="{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
                    user=ctx.message.author.mention))
        await ctx.message.delete()

    @commands.command(description="microphone fix")
    async def micfix(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Mic Fix command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user.mention} To get your microphone working in Shadow please follow this guide: "
                    "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                                   user=user))
            else:
                await ctx.send(
                    "From: {author.name}\nTo get your microphone working in Shadow please follow this guide: "
                    "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                                   user=user))
        else:
            self.bot.logger.info("Mic Fix command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
            await ctx.author.send(content="""{user} To get your microphone working in Shadow please follow this guide: "
                          "https://wiki.shadow.pink/index.php/Using_a_Microphone""".format(user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="ghost manual")
    async def ghostmanual(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Ghost manual command received from {author.name} with argument of {user}".format(
                    author=ctx.message.author,
                    user=user))
            if user is not None:
                await ctx.send(
                    "From: {author.name}\n{user} Ghost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
                        author=ctx.message.author, user=user))
            else:
                await ctx.send("From: {author.name}\nGhost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
                    author=ctx.message.author))
        else:
            self.bot.logger.info("Ghost Manual command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
            await ctx.author.send("""{user} Shadow Ghost Manual http://core.stavlor.net/Ghost_Manual.pdf""".format(
                user=ctx.author.mention))
        await ctx.message.delete(ctx.message)

    @commands.command(description="Latency command")
    async def latency(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Latency command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
            if user is not None:
                await ctx.send(
                    """From {author.name}\n{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                        author=ctx.author, user=user.mention))
            else:
                await ctx.send(
                    """From {author.name}\nCommon steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                        author=ctx.author))
        else:
            await ctx.author.send(
                """{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                    user=ctx.author.mention))
            self.bot.logger.info("Latency command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.author,
                user=user))
        await ctx.message.delete()

    @commands.command(description="Speedtest-Links")
    async def speedtest(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Speedtest command received from {author.name} with argument of {user}".format(
                author=ctx.message.author,
                user=user))
            if user is not None:
                await ctx.send("""From {author.name}\n{user} Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/22774>
    West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author, user=user.mention))
            else:
                await ctx.send("""From {author.name}\nSpeedtest.net links
                NORTH AMERICA
                Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
                Central DC(Texas): <http://www.speedtest.net/server/12190>
                East DC(NY): <http://www.speedtest.net/server/22774>
                West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author))
        else:
            await ctx.author.send("""{user} Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/22774>
    West DC(CA): <http://www.speedtest.net/server/11599>""".format(user=ctx.author.mention))
            self.bot.logger.info("Speedtest command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author,
                user=user))
        await ctx.message.delete()

    @commands.command(description="Send the Terms of Service info")
    async def tos(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send("""From: {author.name}\n{user}  **__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
    __READ THE TOS__
    https://shadow.tech/usen/terms
    https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(author=ctx.author,
                                                                                            user=user.mention))
            else:
                await ctx.send("""From: {author.name}\n**__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
                __READ THE TOS__
                https://shadow.tech/usen/terms
                https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(
                    author=ctx.author))
        await ctx.message.delete()

    @commands.command(description="Nvidia Drivers")
    async def nvidiadrivers(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                    author=ctx.author,
                    user=user))
            if user is not None:
                await ctx.send(
                    """From: {author.name}\n{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                        author=ctx.author, user=user.mention))
            else:
                await ctx.send(
                    """From: {author.name}\nCurrent recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                        author=ctx.author))
        else:
            self.bot.logger.info(
                "NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM".format(
                    ctx=ctx))
            await ctx.author.send(
                "{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Nvidia Drivers")
    async def drivers(self, ctx, *, user: discord.Member = None):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                    author=ctx.author,
                    user=user))
            if user is not None:
                await ctx.send(
                    """From: {author.name}\n{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                        author=ctx.author, user=user.mention))
            else:
                await ctx.send(
                    """From: {author.name}\nCurrent recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                        author=ctx.author))
        else:
            self.bot.logger.info(
                "NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM".format(
                    ctx=ctx))
            await ctx.author.send(
                "{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10".format(
                    user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command(description="Send Ghost Purchase info")
    async def buyghost(self, ctx, *, user: discord.Member = None):
        if user is None:
            self.bot.logger.info("Ghost purchase info command processed for {author.name}".format(author=ctx.message.author))
            await ctx.send(
                "{author.mention} you can purchase ghost from your account page, https://account.shadow.tech/subscription".format(
                    author=ctx.mention))
            await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info("Ghost purchase info command processed for {author.name} and args {user}".format(
                    author=ctx.author, user=user))
                await ctx.send(
                    """From: {author.name}\n{user} you can purchase Shadow Ghost from your account page,  https://account.shadow.tech/subscription""".format(
                        author=ctx.author, user=user.mention))
                await ctx.message.delete()

    @commands.command(description="Send ghost informational link")
    async def ghostinfo(self, ctx, *, user: discord.Member = None):
        if user is None:
            self.bot.logger.info("Ghost info command processed for {author.name}.".format(author=ctx.author))
            await ctx.send(
                "{author.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost".format(
                    author=ctx.author))
            await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info(
                    "Ghost info command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                             user=user))
                await ctx.send(
                    """From: {author.name}\n{user.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost""".format(
                        author=ctx.author, user=user))
                await ctx.message.delete()

    @commands.command(description="Status command")
    async def status(self, ctx, *, user: discord.Member = None):
        if user is None:
            self.bot.logger.info("Status command processed for {author.name}.".format(author=ctx.message.author))
            if await self.bot.admin.get_status() == "Normal":
                embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
                embed.add_field(name="All Systems Normal",
                                value="For additional status information please see the status page", inline=True)
                await ctx.send(embed=embed)
                await ctx.message.delete()
            else:
                status = await self.bot.admin.get_status()
                embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0xff8040)
                embed.add_field(name=status,
                                value="For additional status information please see the status page", inline=True)
                await ctx.send(embed=embed)
                await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info("Status command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                                 user=user))
                await ctx.send(
                    "From {author.name}\n{user.mention} Current Shadow network status is {status}. For more info see https://status.shadow.tech".format(
                        author=ctx.author, user=user, status=await self.bot.admin.get_status()))
                await ctx.message.delete()

    @commands.command(description="Bot Logs")
    async def logs(self, ctx):
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderator']):
            fname = 'discord.log'
            lines = await self.bot.admin.tail(filename=fname, lines=20)
            lines = lines.split("\n")
            paginator = commands.Paginator(prefix="```python")
            for line in lines:
                paginator.add_line(line)
            if "gurus-lab" not in ctx.message.channel.name or "bot-talk" not in ctx.message.channel.name:
                await ctx.author.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.author.send(page)
                self.bot.logger.info(
                    "Sending last few log entries to {ctx.author.name} via PM as its not in gurus-lab".format(ctx=ctx))
            else:

                await ctx.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.send(page)
                await ctx.message.delete()
                self.bot.logger.info("Sending last few log entries to Channel Requestor:{ctx.author}.".format(ctx=ctx))
        else:
            await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
            await ctx.message.delete()
            self.bot.logger.info("Unauthorized log request from {ctx.author}".format(ctx=ctx))

    @commands.command(description="PM test")
    async def pmtest(self, ctx):
        if self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderator']):
            await ctx.author.send("Test")
            await ctx.message.delete()
        else:
            await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
            await ctx.message.delete()
            self.bot.logger.info("Unauthorized pmtest request from {ctx.author}".format(ctx=ctx))


def setup(bot):
    bot.add_cog(General(bot))