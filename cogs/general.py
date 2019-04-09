from discord.ext import commands
import discord


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    @commands.command(description="Send instructions on how to get Verified", aliases=['v'])
    async def verify(self, ctx, *, user: discord.Member = None):
        """How to get verified command."""
        text = """The <:shadow1:495254769288609802> Shadower role (green name) grants access to <#463782843898658846> and many other channels that are not visible to unverified users (white name).

Send a clear **screenshot** of <https://account.shadow.tech/subscription> (click the Subscription link or this link again after you log in) to a Moderator or Shadow Guru to verify you are a subscriber.

**Note:** Do not send a friend request. If you are unable to send a DM, adjust your Privacy Settings for this server (you can change it back after). See here for more info: <https://support.discordapp.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings>"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Verify command received from {author.name} with argument of {user}".format(author=ctx.author,
                                                                                            user=user))
            if user is not None:
                await ctx.send(f"From {ctx.author.name}\n{user.mention} {text}")
            else:
                await ctx.send(f"From {ctx.author.name}\n{text}")
        await ctx.message.delete()

    @commands.command(description="800x600 instructions", name="800x600", aliases=['8x6', 'nogpu'])
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

    @commands.command(aliases=['expired', 'pass'])
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

    @commands.command(description="microphone fix", aliases=['mic', 'micguide'])
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

    @commands.command(aliases=['latency', 'inputlag'])
    async def lag(self, ctx, *, user: discord.Member = None):
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

    @commands.command(aliases=['terms', 'tou'])
    async def tos(self, ctx, *, user: discord.Member = None):
        """Send Terms of Service information"""
        text = """__Terms of Use__
    - See the official Terms of Use here: https://shadow.tech/usen/terms
    - For a simple breakdown of what's not allowed on shadow, see here: https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow
    **Note:** *** Whether it's in the above links or not,*** we ask that you respect others' intellectual properties while using Shadow, and that covers piracy and cheating."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(f"""From: {ctx.author.name}\n{user.mention} {text}""")
            else:
                await ctx.send(f"""From {ctx.author.name}\n{text}""")
        await ctx.message.delete()

    @commands.command(aliases=['nvidiadrivers'])
    async def drivers(self, ctx, *, user: discord.Member = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia Drivers for P5000** -- [__*US has only P5000s*__] [__*Non-US users may have GTX1080*__]
          - Stable Drivers *(**Recommended**)*:  <https://www.nvidia.com/Download/driverResults.aspx/145259/en-us>
          - Vulkan Drivers *(**Optional**)*: <https://developer.nvidia.com/vulkan-beta-41962-windows-10>

        **Notes:**
          - Vulkan drivers will generally have the best performance but may have issues.
          - Driver installation can potentially glitch the streamer, so __***prior to installation***__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher.
          - GeForce Experience is not recommended as all it can do is give you the latest stable driver which is already linked above. Game settings recommendations do not work, and GameStream and broadcast functions will break your streamer and prevent connection to your Shadow."""
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

    @commands.command(aliases=['purchaseghost', 'buyghost', 'ghostinfo', 'ghostmanual'])
    async def ghost(self, ctx, *, user: discord.Member = None):
        """Ghost Purchase information."""
        text = """Ghosts can be purchased from your account page under Subscription: https://account.shadow.tech/subscription

For the Ghost user manual, see here: http://core.stavlor.net/Ghost_Manual.pdf"""
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

    @commands.command(aliases=['minimums', 'minimalreq', 'requirements', 'reqs'])
    async def minreq(self, ctx, *, user: discord.Member = None):
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
        - Mac device from 2012 or more recent
        
        *** CPU Family support diagram: *** http://core.stavlor.net/cpu_decode_support.png"""
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

    @commands.command(aliases=['applications', 'beta', 'update', 'app'])
    async def apps(self, ctx, *, user: discord.Member = None):
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

    @commands.command(aliases=['hotkeys', 'keybinds'])
    async def keys(self, ctx, *, user: discord.Member = None):
        """Send Keybinding information"""
        self.bot.logger.info(f"Processed keys command for {ctx.author.name} with parameter {user}.")
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
        """IP/Geoip Information"""
        self.bot.logger.info(f"Processed ip command for {ctx.author.name} with parameter {user}.")
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

    @commands.command(aliases=['sup'])
    async def support(self, ctx, *, user: discord.Member = None):
        """Send details for how to reach support."""
        self.bot.logger.info(f"Processed support command for {ctx.author.name} with parameter {user}.")
        text = """  This is a community-based Discord where other members of the community may be able to assist with your issues in <#463782843898658846>, however please be aware that most folks here aren't Blade Employees, and although Blade employees do occasionally interact here, this isn't an official support channel.
  Therefore if the troubleshooting provided here does not resolve your issue, or to leave feedback directly to Shadow, you will need to contact Shadow Support:
  - From your account page, click Support: https://account.shadow.tech/support
  - If you are unable to access your account page, use the Help Desk: https://help.shadow.tech/hc/en-gb/requests/new"""
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

    @commands.command(aliases=['appletv', 'appletvbeta'])
    async def atv(self, ctx, *, user: discord.Member = None):
        """Apple TV Testflight invite link"""
        self.bot.logger.info(f"Processed atv command for {ctx.author.name} with parameter {user}.")
        text = """You can join the Apple TV Testflight via this link from any iOS Device once Testflight is installed: <https://testflight.apple.com/join/h9H54DqA>"""
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

    @commands.command(aliases=['map', 'coveragemap', 'locations'])
    async def coverage(self, ctx, *, user: discord.Member = None):
        """Coverage Maps"""
        self.bot.logger.info(f"Processed coverage command for {ctx.author.name} with parameter {user}.")
        text = """Shadow Coverage map: https://www.google.com/maps/d/u/0/edit?mid=1F65uzzfo5GicmBg4h-UJ9lB7rHCUnQFe&ll=15.811693684367462%2C-55.29886565000004&z=2"""
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

    @commands.command(aliases=['hstats', 'statspage', 'sscp', 'scps'])
    async def stats(self, ctx, *, user: discord.Member = None):
        """How to access Shadow Control panel stats pane."""
        self.bot.logger.info(f"Processed hstats command for {ctx.author.name} with parameter {user}.")
        text = """The Stats page in the shadow control panel can provide useful troubleshooting information (IPS, Bitrate, Ping and Packet Loss) to access it please this http://core.stavlor.net/how_to_access_stats.png"""
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

    @commands.command(aliases=['language'])
    async def changelang(self, ctx, *, user: discord.Member = None):
        """How to Change language from FR to EN."""
        self.bot.logger.info(f"Processed changelang command for {ctx.author.name} with parameter {user}.")
        text = """How to change the language of your Shadow: https://docs.google.com/document/d/10P6MqbIYqi_ITDczfi_DUeTkmsuBWlTsi-PFY_fqbBw/edit"""
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

    @commands.command(aliases=['virtualhere', 'vhere'])
    async def vh(self, ctx, *, user: discord.Member = None):
        """Virtual Here Information"""
        text = """**Get VirtualHere** -- **VirtualHere** works to share ***a single USB device*** (without paying, get a license for more than one) over *your local network*. 

**VirtualHere** *server* on your local machine (you'll have to run it every time you get on Shadow).

**VirtualHere** *client* on the Shadow (again, you'll have to run it each time to get on Shadow, running it as an automatic Windows service is a paid feature).

When prompted, VirtualHere will ask you to install **Bonjour**; do this. It makes life easier by making the VH client find the VH server hub automagically. Do this on both client and server installations when prompted.

Next step is getting Shadow on your local area network (LAN).

You can use **Hamachi** (Guide) <https://documentation.logmein.com/documentation/EN/pdf/Hamachi/LogMeIn_Hamachi_UserGuide.pdf> or **ZeroTier** (Guide) <https://docs.google.com/document/d/1NcVK11lcS8m2G_0fsqMcXvkcdLWdaU2O4Vc_qyJrnng/edit?usp=sharing>"""
        self.bot.logger.info(f"Processed vh command for {ctx.author.name} with parameter {user}.")
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
