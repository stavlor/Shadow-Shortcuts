from discord.ext import commands
import discord


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    @commands.command(description="Send instructions on how to get Verified")
    async def verify(self, ctx, *, user: discord.Member = None):
        """How to get verified command."""
        text = """Certain channels like <#463782843898658846> require the Shadower role to allow you to view or chat in them, which is only given to people who verify that they are a current Shadow subscriber. To get verified, please DM any Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role.
Note: Discord settings may prevent you from sending messages to those not on your friends list. Adjust this to allow messages to those you share a server with in order to be able to send the DM
- For help with Discord Privacy settings see these images:
    - <http://core.stavlor.net/verify1.png>
    - <http://core.stavlor.net/verify2.png>"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Verify command received from {author.name} with argument of {user}".format(author=ctx.author,
                                                                                            user=user))
            if user is not None:
                await ctx.send(f"From {ctx.author.name}\n{user.mention} {text}")
            else:
                await ctx.send(f"From {ctx.author.name}\n{text}")
        await ctx.message.delete()

    @commands.command(description="800x600 instructions", name="800x600")
    async def _800x600(self, ctx, *, user: discord.Member = None):
        """800x600 Information (red square)"""
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

    @commands.command(description="Waiting for video instructions", aliases=['waitingforvideo', 'wfv'])
    async def waitingvideo(self, ctx, *, user: discord.Member = None):
        """Waiting for Video information"""
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

    @commands.command(description="Error 102 Fix.", aliases=['error102'])
    async def fix102(self, ctx, *, user: discord.Member = None):
        """Error 102 Information"""
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
        """Default Password help for Ready-to-Go Shadow Images"""
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
            self.bot.logger.info("Password command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author))
            await ctx.author.send(
                content="{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
                    user=ctx.message.author.mention))
        await ctx.message.delete()

    @commands.command(description="microphone fix")
    async def micfix(self, ctx, *, user: discord.Member = None):
        """Microphone fix information."""
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
            await ctx.author.send("""{user} To get your microphone working in Shadow please follow this guide: "
                          "https://wiki.shadow.pink/index.php/Using_a_Microphone""".format(user=ctx.author.mention))
        await ctx.message.delete()

    @commands.command()
    async def ghostmanual(self, ctx, *, user: discord.Member = None):
        """Send Link to Ghost Manual"""
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
        await ctx.message.delete()

    @commands.command(description="Latency command")
    async def latency(self, ctx, *, user: discord.Member = None):
        """Input lag/Latency Information"""
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
        """Speedtest Links"""
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

    @commands.command()
    async def tos(self, ctx, *, user: discord.Member = None):
        """Send Terms of Service information"""
        text = """__READ THE TOS__
    https://shadow.tech/usen/terms
    https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow
    **__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(f"""From: {ctx.author.name}\n{user.mention} {text}""")
            else:
                await ctx.send(f"""From {ctx.author.name}\n{text}""")
        await ctx.message.delete()

    @commands.command(aliases=['drivers'])
    async def nvidiadrivers(self, ctx, *, user: discord.Member = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia Drivers for P5000** -- [__*US has only P5000s*__] [__*Non-US users may have GTX1080*__]
          - Stable Drivers *(**Recommended**)*:  <https://www.nvidia.com/Download/driverResults.aspx/145260/en-us>
          - Vulkan Drivers *(**Optional**)*: <https://developer.nvidia.com/vulkan-beta-41962-windows-78>

        **Notes:**
          - Vulkan drivers will generally have the best performance but may have issues.
          - Driver installation can potentially glitch the streamer, so __***prior to installation***__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher.
          - Under no circumstances should GameStream be enabled as it will break your streamer and prevent connection to your Shadow.
          - GeForce Experience other than providing the latest recommended drivers, is not needed just use the provided links."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                    author=ctx.author,
                    user=user))
            if user is not None:
                await ctx.send(f"""From {ctx.author.name}\n{user.mention} {text}""")
            else:
                await ctx.send(f"""From {ctx.author.name}\n{text}""")
        else:
            self.bot.logger.info(f"NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM")
            await ctx.author.send(f"{ctx.author.mention} {text}")
        await ctx.message.delete()

    @commands.command(aliases=['purchaseghost'])
    async def buyghost(self, ctx, *, user: discord.Member = None):
        """Ghost Purchase information."""
        if user is None:
            self.bot.logger.info("Ghost purchase info command processed for {author.name}".format(author=ctx.message.author))
            await ctx.send(
                "{author.mention} you can purchase ghost from your account page, https://account.shadow.tech/subscription".format(
                    author=ctx.author))
            await ctx.message.delete()
        else:
            if await self.bot.admin.can_run_command(ctx.author.roles):
                self.bot.logger.info("Ghost purchase info command processed for {author.name} and args {user}".format(
                    author=ctx.author, user=user))
                await ctx.send(
                    """From: {author.name}\n{user} you can purchase Shadow Ghost from your account page,  https://account.shadow.tech/subscription""".format(
                        author=ctx.author, user=user.mention))
                await ctx.message.delete()


    @commands.command(description="Status command")
    async def status(self, ctx, *, user: discord.Member = None):
        """Reports current shadow status"""
        if user is None:
            self.bot.logger.info("Status command processed for {author.name}.".format(author=ctx.message.author))
            if await self.bot.admin.get_status() == "All Systems Operational":
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
        """Logs Command"""
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            fname = 'discord.log'
            lines = await self.bot.admin.tail(filename=fname, lines=50)
            lines = lines.split("\n")
            paginator = commands.Paginator(prefix="```python")
            for line in lines:
                paginator.add_line(line)
            if not (ctx.channel.name == 'gurus-lab') and not (ctx.channel.name == 'bot-talk'):
                await ctx.author.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.author.send(page)
                self.bot.logger.info(f"Sending last few log entries to {ctx.author.name} via PM as its not in gurus-lab channel was {ctx.channel.name}")
            else:
                await ctx.send("Here is the last few lines of the log:")
                for page in paginator.pages:
                    await ctx.send(page)
                await ctx.message.delete()
                self.bot.logger.info(f"Sending last few log entries to Channel Requestor:{ctx.author}.")
        else:
            await ctx.send(f"Sorry {ctx.author.mention} your not authorized to do this.")
            await ctx.message.delete()
            self.bot.logger.info(f"Unauthorized log request from {ctx.author}")

    @commands.command(description="PM test")
    async def pmtest(self, ctx):
        """PM Debug command"""
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.author.send("Test")
            await ctx.message.delete()
        else:
            await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
            await ctx.message.delete()
            self.bot.logger.info("Unauthorized pmtest request from {ctx.author}".format(ctx=ctx))

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member):
        """Look up general user info."""
        rolelist = ""
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send(f"{ctx.author.mention} your not authorized to do that.")
            return
        paginator = discord.ext.commands.Paginator(prefix='```css', suffix='```')
        paginator.add_line(f"User-ID: {user.id}\tUsername+discriminator: {user}\tDisplay name: {user.display_name}")
        for role in user.roles:
            rolelist += f"{role.name}({role.id}) "
        paginator.add_line(f"Has roles: {rolelist}")
        joinedat = user.joined_at.strftime('%Y-%m-%d %H:%M:%S')
        createdat = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        paginator.add_line(f"Joined on: {joinedat}\tCreated at: {createdat}")
        paginator.add_line(f"Status: {user.status}\tActivity: {user.activity}")
        for page in paginator.pages:
            await ctx.send(page)

    @commands.command()
    async def minreq(self, ctx, *, user=None):
        """Give Shadow Minimum requirements"""
        self.bot.logger.info(
            "Minreq received from {author.name} with argument of {user}".format(
                author=ctx.author,
                user=user))
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        **Windows**
        - Windows 7 - 32 bits or above
        - Processor from 2011-2012 or more recent
        - Integrated GPU recommended
        - AMD GPU from 2013 or more recent (to disable if older)
        - Nvidia GPU from 2011 and more recent (to disable if older)
        
        **Mac**
        - Mac OS 10.10 Yosemite or above
        - Mac device from 2012 or more recent"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{user.mention} {text}"
            await ctx.send(text)
            await ctx.message.delete()
        elif user is None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{text}"
            await ctx.send(text)
            await ctx.message.delete()
        else:
            ctx.author.send(text)
            await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        """Ping command"""
        import datetime
        now = datetime.datetime.now()
        delta = (now - ctx.message.created_at).total_seconds()*1000
        await ctx.send('Pong! Server ping {:.3f}ms API ping: {:.3f}ms :ping_pong:'.format(delta, self.bot.latency*1000))

    @commands.command(aliases=['apps', 'beta', 'update'])
    async def applications(self, ctx, *, user: discord.Member = None):
        """Link to Shadow Applications download."""
        text = """You can download the Shadow client from the Appplications section of your account page: https://account.shadow.tech/apps
 Stable versions include: Windows 32/64 bit, macOS, Android, iOS
 Beta versions include: Windows 64 bit, macOS, Ubuntu
 Each version has a designated channel in Discord. To view these channels, you will need the Shadower role. Feedback on the beta versions should be left in the proper channels."""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{user.mention} {text}"
            await ctx.send(text)
            await ctx.message.delete()
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{text}"
            await ctx.send(text)
            await ctx.message.delete()
        else:
            text = f"{ctx.author.mention} {text}"
            await ctx.author.send(text)
            await ctx.message.delete()

    @commands.command(aliases=['hotkeys', 'keys'])
    async def keybinds(self, ctx, *, user: discord.Member = None):
        """Send Keybinding information"""
        self.bot.logger.info(f"Processed keybinds command for {ctx.author.name} with parameter {user}.")
        text = """:keyboard: Stable Hotkeys
        - <:WindowsShadow:555856447691292736>/**⌘** + **Ctrl** + **S** = Restart Streaming
        - <:WindowsShadow:555856447691292736>/**⌘** + **Ctrl** + **F** = Toggle Fullscreen
        - <:WindowsShadow:555856447691292736>/**⌘** + **Ctrl** + **G** = Toggle Mouse lock/Gamer Mode
        - <:WindowsShadow:555856447691292736>/**⌘** + **Ctrl** + **Q** = Quit Application

:keyboard: Beta Hotkeys
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **M** = Change mouse mode
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **Q** = Quit Application
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **F** = Toggle fullscreen"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{user.mention} {text}"
            await ctx.send(text)
            await ctx.message.delete()
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{text}"
            await ctx.send(text)
            await ctx.message.delete()
        else:
            text = f"{ctx.author.mention} {text}"
            await ctx.author.send(text)
            await ctx.message.delete()


    @commands.command(aliases=['ips','geoip'])
    async def ip(self, ctx, *, user: discord.Member = None):
        text = """Trying to find the geographic location of your Shadow using websites which detect it via your IP address will likely be inaccurate, because Blade occasionally moves IP addresses around between its datacenters.
 If you suspect your Shadow is on the wrong datacenter, first find your Shadow's public IP using http://bot.whatismyipaddress.com/:
            - **Europe**
                - If your IP begins with **185.161.** you are on the **Amsterdam** datacenter
                - If your IP begins with **85.190.** you are on the **France** datacenter
            - **North America**
                - If your IP begins with **185.231.** you are on the **California** datacenter
                - If your IP begins with **162.213.** you are on the **New York** datacenter
                - If your IP begins with **216.180.[128-135]** you are on the **Texas** datacenter
                - If your IP begins with **216.180.[136-143]** you are on the **Chicago** datacenter"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{user.mention} {text}"
            await ctx.send(text)
            await ctx.message.delete()
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{text}"
            await ctx.send(text)
            await ctx.message.delete()
        else:
            text = f"{ctx.author.mention} {text}"
            await ctx.author.send(text)
            await ctx.message.delete()

    @commands.command()
    async def support(self, ctx, *, user: discord.Member = None):
        text = """Note while this is a community Discord and the community may be able to assist in <#463782843898658846>, 
        Most folks here aren't Blade Employees and though they do occasionally interact here this isn't an official support channel. 
            - How to contact support:

            - Support Page: https://account.shadow.tech/support

            - Help Desk: https://help.shadow.tech/hc/en-gb/requests/new"""
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{user.mention} {text}"
            await ctx.send(text)
            await ctx.message.delete()
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"From {ctx.author.name}\n{text}"
            await ctx.send(text)
            await ctx.message.delete()
        else:
            text = f"{ctx.author.mention} {text}"
            await ctx.author.send(text)
            await ctx.message.delete()


def setup(bot):
    bot.add_cog(General(bot))
