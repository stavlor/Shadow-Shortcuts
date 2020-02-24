from discord.ext import commands
import discord
import typing


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    @commands.command(description="Send instructions on how to get Verified", aliases=['v'])
    async def verify(self, ctx, user: typing.Optional[discord.Member] = None):
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


    @commands.command(description="L:104 Error Troubleshooting tips.", aliases=['fix104', '104', 'l104', 'rebootshadow', 'restartshadow', 'sd', 'shutdown'])
    async def errorl104(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""Please access your help menu :grey_question: then scroll down and hit ***Shutdown Shadow***, then wait 2-5 minutes and restart your client to resolve your issue http://botstatic.stavlor.net/reboot.gif"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "104 command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(f"From {ctx.author.name}\n{user.mention} {text}")
            else:
                await ctx.send(f"From {ctx.author.name}\n{text}")
        else:
            await ctx.author.send(f"{ctx.author.mention} {text}")
        await ctx.message.delete()

    @commands.command(aliases=['expired', 'pass', 'pw'])
    async def password(self, ctx, user: discord.Member = None):
        """Default Password help for Ready-to-Go Shadow Images"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Password command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                              user=user))
            if user is not None:
                embed = discord.Embed(color=0x3d8023)
                embed.add_field(name="Ready to go password Update", value="If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903)" , inline=True)
                embed.add_field(name='Default Password', value="If you encounter issues the default password for your shadow is blank meaning nothing in the password field \"\"", inline=True)
                await ctx.send(f"From: {ctx.author.name}\n{user.mention} please see the following regarding Ready to Go Shadow and Password expiring:\n", embed=embed)
            else:
                embed = discord.Embed(color=0x3d8023)
                embed.add_field(name="Ready to go password Update",
                                value="If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903)",
                                inline=True)
                embed.add_field(name='Default password',
                                value="If you encounter issues the default password for your shadow is blank meaning nothing in the password field \"\"",
                                inline=True)
                await ctx.send(
                    f"From: {ctx.author.name}\nPlease see the following regarding Ready to Go Shadow and Password expiring:\n",
                    embed=embed)
        else:
            self.bot.logger.info("Password command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author))
            embed = discord.Embed(color=0x3d8023)
            embed.add_field(name="Ready to go password Update",
                            value="If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903)",
                            inline=True)
            embed.add_field(name='Default password',
                            value="If you encounter issues the default password for your shadow is blank meaning nothing in the password field \"\"",
                            inline=True)
            await ctx.author.send(
                f"{ctx.author.mention} please see the following regarding Ready to Go Shadow and Password expiring:\n",
                embed=embed)
        await ctx.message.delete()

    @commands.command(description="microphone fix", aliases=['mic', 'micguide'])
    async def micfix(self, ctx, user: typing.Optional[discord.Member] = None):
        """Microphone fix information."""
        text = """To get your microphone working in Shadow please follow this guide: https://wiki.shadow.pink/index.php/Using_a_Microphone"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Mic Fix command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
            if user is not None:
                await ctx.send(f"From: {ctx.author.name}\n{user.mention} {text}")
            else:
                await ctx.send(f"From: {ctx.author.name}\n{text}")
        else:
            self.bot.logger.info(f"Mic Fix command received from unauthorized user {ctx.author.name}, replied via PM. ")
            await ctx.author.send(f"""{ctx.author.mention} {text}""")
        await ctx.message.delete()

    @commands.command(description="Speedtest-Links")
    async def speedtest(self, ctx, user: typing.Optional[discord.Member] = None):
        """Speedtest Links"""
        text = """Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/14855>
    West DC(CA): <http://www.speedtest.net/server/11613>"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info("Speedtest command received from {author.name} with argument of {user}".format(
                author=ctx.message.author,
                user=user))
            if user is not None:
                await ctx.send(f"From {ctx.author.name}\n{user.mention}\n{text}")
            else:
                await ctx.send(f"From {ctx.author.name}\n{text}")

        else:
            await ctx.author.send(f"{ctx.author.mention}\n{text}")
            self.bot.logger.info("Speedtest command received from unauthorized user {author.name}, replied via PM. ".format(
                author=ctx.message.author,
                user=user))
        await ctx.message.delete()

    @commands.command(aliases=['terms', 'tou'])
    async def tos(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Terms of Service information"""
        text = """__Terms of Use__
- See the official Terms of Use here: <https://shadow.tech/usen/terms>
- For a simple breakdown of what's not allowed on shadow, see here: <https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow>
 **Note:** ***Whether it's in the above links or not,*** we ask that you respect others' intellectual properties while using Shadow, and that covers piracy and cheating."""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
            if user is not None:
                await ctx.send(f"""From: {ctx.author.name}\n{user.mention} {text}""")
            else:
                await ctx.send(f"""From {ctx.author.name}\n{text}""")
        await ctx.message.delete()

    @commands.command(aliases=['nvidiadrivers', 'drovers'])
    async def drivers(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia Drivers for P5000** -- [__*US has only P5000s*__] [__*Non-US users may have GTX1080*__]
          - Stable Drivers (ODE)  *(**Recommended**)*: <https://www.nvidia.com/Download/driverResults.aspx/156767/en-us>

        **Notes:**
          - If running NVidia Drivers prior to 430.64 please ensure you update your drivers as there are critical CPU and other bugs in older drivers.
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
    async def ghost(self, ctx, user: typing.Optional[discord.Member] = None):
        """Ghost Purchase information."""
        text = """Ghosts can be purchased from your account page under Subscription: https://account.shadow.tech/subscription

For the Ghost user manual, see here: http://botstatic.stavlor.net/Ghost_Manual.pdf"""
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

    @commands.group(name="account")
    async def account(self, ctx):
        pass

    @account.command(aliases=['account'])
    async def myaccount(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can access your account page via <https://account.shadow.tech/>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can access your account page via <https://account.shadow.tech/>."""
            await ctx.send(text)
        else:
            text = f"""You can access your account page via <https://account.shadow.tech/>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command(aliases=['reset'])
    async def myshadow(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can reset your shadow via <https://account.shadow.tech/myshadow>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can reset your shadow via <https://account.shadow.tech/myshadow>."""
            await ctx.send(text)
        else:
            text = f"""You can reset your shadow via <https://account.shadow.tech/myshadow>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command()
    async def security(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can access the security page via <https://account.shadow.tech/security>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can access the security page via <https://account.shadow.tech/security>."""
            await ctx.send(text)
        else:
            text = f"""You can access the security page via <https://account.shadow.tech/myshadow>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command()
    async def billing(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can access the billing page via <https://account.shadow.tech/financial>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can access the billing page via <https://account.shadow.tech/financial>."""
            await ctx.send(text)
        else:
            text = f"""You can access the billing page via <https://account.shadow.tech/financial>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command()
    async def subscription(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can access the subscription page via <https://account.shadow.tech/subscription>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can access the subscription page via <https://account.shadow.tech/subscription>."""
            await ctx.send(text)
        else:
            text = f"""You can access the subscription page via <https://account.shadow.tech/subscription>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command(aliases=['apps'])
    async def applications(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, You can get the current stable and beta applications from <https://account.shadow.tech/apps>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\nYou can get the current stable and beta applications from <https://account.shadow.tech/apps>."""
            await ctx.send(text)
        else:
            text = f"""You can get the current stable and beta applications from <https://account.shadow.tech/apps>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command()
    async def refer(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, Want to earn credit for referring your friends to Shadow? see  <https://account.shadow.tech/share>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\n, Want to earn credit for referring your friends to Shadow? see  <https://account.shadow.tech/share>."""
            await ctx.send(text)
        else:
            text = f"""Want to earn credit for referring your friends to Shadow? see  <https://account.shadow.tech/share>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @account.command(name='support')
    async def support(self, ctx, user: typing.Optional[discord.Member] = None):
        if user is not None and await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From: {ctx.author.name}\n{user.mention}, Having an issue with your Shadow? Can't seem to solve the issue here? Ask Support: <https://account.shadow.tech/support>."""
            await ctx.send(text)
        elif await self.bot.admin.can_run_command(ctx.author.roles):
            text = f"""From {ctx.author.name}\n, Having an issue with your Shadow? Can't seem to solve the issue here? Ask Support: <https://account.shadow.tech/support>."""
            await ctx.send(text)
        else:
            text = f"""Having an issue with your Shadow? Can't seem to solve the issue here? Ask Support: <https://account.shadow.tech/support>."""
            await ctx.author.send(text)
        await ctx.message.delete()

    @commands.command(description="Status command")
    async def status(self, ctx, user: typing.Optional[discord.Member] = None):
        """Reports current shadow status"""
        if user is None:
            self.bot.logger.info("Status command processed for {author.name}.".format(author=ctx.message.author))
            if await self.bot.admin.get_status() == "All services operating normally":
                embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
                embed.add_field(name="All services operating normally",
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
    async def minreq(self, ctx, user: typing.Optional[discord.Member] = None):
        """Give Shadow Minimum requirements"""
        self.bot.logger.info(
            "Minreq received from {author.name} with argument of {user}".format(
                author=ctx.author,
                user=user))
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        **Windows**
        - Windows 8 (Windows 7 is no longer supported), Windows 10 Recommended - 32 bits or above
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

    @commands.command(aliases=['applications', 'beta', 'update', 'app'])
    async def apps(self, ctx, user: typing.Optional[discord.Member] = None):
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
    async def keys(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Keybinding information"""
        self.bot.logger.info(f"Processed keys command for {ctx.author.name} with parameter {user}.")
        text = """:keyboard: Keybinds
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **M** = Change mouse mode (Locked/Unlocked) (Locked is suggested for gaming)
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **Q** = Quit Application
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **F** = Toggle fullscreen
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **O** = Toggle Quick menu
        - <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **R** = Restart Streaming"""

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
    async def ip(self, ctx, user: typing.Optional[discord.Member] = None):
        """IP/Geoip Information"""
        self.bot.logger.info(f"Processed ip command for {ctx.author.name} with parameter {user}.")
        text = """Trying to find the geographic location of your Shadow using websites which detect it via your IP address will likely be inaccurate, because Blade occasionally moves IP addresses around between its datacenters.
 If you suspect your Shadow is on the wrong datacenter, first find your Shadow's public IP using http://bot.whatismyipaddress.com/:
            - **Europe**
                - If your IP begins with **185.161.** you are on the **Amsterdam** datacenter
                - If your IP begins with **85.190.** you are on the **France** datacenter
            - **North America**
                - If your IP begins with **170.249.[92-95].** you are on the **California** datacenter
                - If your IP begins with **162.213.[48-55].** you are on the **New York** datacenter
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
    async def _support(self, ctx, user: typing.Optional[discord.Member] = None):
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
    async def atv(self, ctx, user: typing.Optional[discord.Member] = None):
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
    async def coverage(self, ctx, user: typing.Optional[discord.Member] = None):
        """Coverage Maps"""
        self.bot.logger.info(f"Processed coverage command for {ctx.author.name} with parameter {user}.")
        text = """**Shadow Coverage maps:**
            North America - <https://shdw.me/NACoverage>
            Europe - <https://shdw.me/EUCoverage>"""
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
    async def stats(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to access Shadow Control panel stats pane."""
        self.bot.logger.info(f"Processed hstats command for {ctx.author.name} with parameter {user}.")
        text = """The Stats page in the shadow control panel can provide useful troubleshooting information (IPS, 
        Bitrate, Ping and Packet Loss) to access it please this http://botstatic.stavlor.net/how_to_access_stats.png """
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
    async def changelang(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to Change language from FR to EN."""
        self.bot.logger.info(f"Processed changelang command for {ctx.author.name} with parameter {user}.")
        text = """How to change the language of your Shadow: http://wiki.stavlor.net/ChangeLanguage%20FR%20to%20EN"""
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
    async def vh(self, ctx, user: typing.Optional[discord.Member] = None):
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

    @commands.command()
    async def usbdk(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send USB Dev Kit Downloads/info"""
        text = """USB Development Kit Drivers are needed for proper functioning of USB over IP on Windows
        Normally the Shadow client will install these drivers however sometimes this install fails you can manually download and install them from here
         - **Windows 32bit** - http://botstatic.stavlor.net/UsbDk_1.0.21_x86.msi
         - **Windows 64bit** - http://botstatic.stavlor.net/UsbDk_1.0.21_x64.msi
        Once installed reboot your local system and USB over IP should function normally, ***___Note Install these on your local PC not your shadow.___***"""
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
    async def ghc(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Ghost CS Message for AMA."""
        text = """Today our European team announced limited availability of the Shadow Ghost for sale in their territories. Here in the US, we’re still finalizing our plans to make the Shadow Ghost available for our community, but until then, please sign up on the official waiting list to indicate your interest. If you’ve already signed up, no need to do so again. Just to be up front about things, the quantities we’re talking about, both in the US and Europe are pretty small, so it’s possible that not everyone on the waiting list will be able to get a Shadow Ghost in the next round.

Thanks for your interest, and we’ll have more information as soon as we can lock down details.

<https://shdw.me/NA-waiting-list-SGDC>"""
        self.bot.logger.info(f"Processed ghc command for {ctx.author.name} with parameter {user}.")
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
    async def cake(self, ctx):
        await ctx.message.add_reaction("🍰")

    @commands.command()
    async def math(self, ctx, *, parameters):
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.send(f"{ctx.author.mention} Your not authorized to do that...")
            return
        env = {}
        env["locals"] = None
        env["globals"] = None
        env["__name__"] = None
        env["__file__"] = None
        env["__builtins__"] = None

        result = eval(str(parameters), env, None)
        await ctx.send(f"Result: {result}")

    @commands.command(aliases=['google'])
    async def lmgtfy(self, ctx, *, args):
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.send(f"{ctx.author.mention} Your not authorized to do that...")
            return
        args2 = args.replace(' ', '+')
        url = "https://lmgtfy.com/?q=" + str(args2)
        await ctx.send(embed=discord.Embed(description="**[Look here!](%s)**" % url, color=discord.Color.gold()))
        await ctx.message.delete()

    @commands.command(aliases=['rm', 'roadmap'])
    async def _roadmap(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Shadow roadmap: <https://shadow.tech/usen/features-roadmap>"""
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(text)
            await ctx.message.delete()
        if not user:
            await ctx.send(f"From: {ctx.author.name}\n{text}")
            await ctx.message.delete()
        else:
            await ctx.send(f"From: {ctx.author.name}\n{user.mention} {text}")
            await ctx.message.delete()

    @commands.command()
    async def _writelog(self, ctx):
        file = "/tmp/logging-test.txt"
        fp = open(file, 'w+')
        messages = await ctx.channel.history(limit=250).flatten()
        for item in messages:
            fp.write(f"{item.system_content} - {item.created_at} - \"{item.author}\"\n")
        fp.close()

    @commands.command(aliases=['s101', 'S101'])
    async def _s101(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """To fix S:101 please see the following Shadow help article: 
        https://help.shadow.tech/hc/en-gb/articles/360010559860-S-101-An-Issue-Happened-with-the-Streaming-Services """
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(text)
            await ctx.message.delete()
        if not user:
            await ctx.send(f"From: {ctx.author.name}\n{text}")
            await ctx.message.delete()
        else:
            await ctx.send(f"From: {ctx.author.name}\n{user.mention} {text}")
            await ctx.message.delete()

    @commands.command(aliases=['ask'])
    async def _ask(self, ctx, user: typing.Optional[discord.Member] = None):
        text = "https://www.dontasktoask.com/"
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(text)
            await ctx.message.delete()
        if not user:
                await ctx.send(f"From: {ctx.author.name}\n{text}")
                await ctx.message.delete()
        else:
            await ctx.send(f"From: {ctx.author.name}\n{user.mention} {text}")
            await ctx.message.delete()

    @commands.command(aliases=['specs', 'tiers'])
    async def _specs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """
***___Shadow Legacy/Shadow Boost___***
**GPU:** Quadro P5000 (GeForce GTX 1080 Equiv.)
**VRAM:** 16 GB
**CPU:** Intel Xeon E5-2667v3 Processor
**CPU Clock Speed:** 2.5 GHz Turbo to 3.2 GHz
**RAM:** 12 GB
**Storage:** 256 GB

***___Shadow Ultra___***
**GPU:** Quadro RTX 5000 (GeForce RTX 2080 SUPER Equiv.)
**VRAM:** 16 GB
**CPU:** Intel Xeon W-3235 Processor
**CPU Clock Speed:** 3.3 GHz @ 4 cores - Turbo to 4 GHz
**RAM:** 16 GB
**Storage:** 512 GB

***___Shadow Infinite___***
**GPU:** Quadro RTX 6000 (Nvidia TITAN RTX Equiv.)
**VRAM:** 24 GB
**CPU:** Intel Xeon W-3235 Processor
**CPU Clock Speed:** 3.3 GHz @ 6 cores - Turbo to 4 GHz
**RAM:** 32 GB
**Storage:** 1024 GB"""
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(text)
            await ctx.message.delete()
        if not user:
            await ctx.send(f"From: {ctx.author.name}\n{text}")
            await ctx.message.delete()
        else:
            await ctx.send(f"From: {ctx.author.name}\n{user.mention} {text}")
            await ctx.message.delete()



def setup(bot):
    bot.add_cog(General(bot))
