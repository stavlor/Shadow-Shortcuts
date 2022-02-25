from discord.ext import commands
import discord
import typing


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    async def text_command_process(self, ctx: commands.Context, user: discord.Member, text: str, command_name: str, suppress_from: bool = False):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(f"{command_name} recieved from {ctx.author.name} with argument of {user}")
            if suppress_from and user is not None:
                await ctx.send(f"{user.mention} {text}")
            elif suppress_from and user is None:
                await ctx.send(f"{text}")
            elif user is not None:
                await ctx.send(f"From {ctx.author.name}\n{user.mention} {text}")
            else:
                await ctx.send(f"From {ctx.author.name}\n{text}")
        else:
            self.bot.logger.info(f"{command_name} command received from un-privileged user {ctx.author.name} Responding Via PM")
            await ctx.author.send(f"{ctx.author.mention} {text}")
        await ctx.message.delete()


    @commands.command(description="Send instructions on how to get Verified", aliases=['v'])
    async def verify(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to get verified command."""
        text = """The <:shadow1:495254769288609802> Shadower role (green name) grants access to <#463782843898658846> and many other channels that are not visible to unverified users (white name).

Send a clear **screenshot** of <https://account.shadow.tech/home> (click the Subscription link or this link again after you log in) to a Moderator or Shadow Guru to verify you are a subscriber.

**Note:** Do not send a friend request. If you are unable to send a DM, adjust your Privacy Settings for this server (you can change it back after). See here for more info: <https://support.discordapp.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="verify")


    @commands.command(description="L:104 Error Troubleshooting tips.", aliases=['fix104', '104', 'l104', 'errorl104', 'rebootshadow', 'restartshadow', 'sd', 'error104'])
    async def shutdown(self, ctx, user: typing.Optional[discord.Member] = None, min_time_to_wait=2, max_time_to_wait=5):
        text = f"""Please access your help menu :grey_question: then scroll down and hit ***Shutdown Shadow***, then wait {min_time_to_wait}-{max_time_to_wait} minutes and restart your client to resolve your issue http://botrexford.shdw.info/reboot.gif"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="shutdown")

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

    @commands.command(description="L203 Forum Page", aliases=['l203'])
    async def l203forum(self, ctx, user: typing.Optional[discord.Member] = None):
        text = "For additional information on Error L:203 Please see the following forum article: https://l.shdw.info/l203"
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="micfix")

    @commands.command(description="microphone fix", aliases=['mic', 'micguide'])
    async def micfix(self, ctx, user: typing.Optional[discord.Member] = None):
        """Microphone fix information."""
        text = """To get your microphone working in Shadow please follow this guide: https://wiki.shdw.info/w/Microphone"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="micfix")

    @commands.command(description="Speedtest-Links")
    async def speedtest(self, ctx, user: typing.Optional[discord.Member] = None):
        """Speedtest Links"""
        text = """For Shadows Official Speedtest please see here: <https://shadow.tech/requirements/internet-speed-test>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="speedtest")

    @commands.command(aliases=['terms', 'tou'])
    async def tos(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Terms of Service information"""
        text = """__Terms of Use__
- See the official Terms of Use here: <https://shadow.tech/terms-of-use>
- For a simple breakdown of what's not allowed on shadow, see here: <https://help.shadow.tech/hc/en-gb/articles/360000455174>
 **Note:** ***Whether it's in the above links or not,*** we ask that you respect others' intellectual properties while using Shadow, and that covers piracy and cheating."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="tos")

    @commands.command(aliases=['nvidiadrivers', 'drovers'])
    async def drivers(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia For Quadro Family Devices (Shadow, Shadow Ultra and Shadow Infinite.)
                    
          - Stable Drivers (ODE)  *(**Recommended**)*: <https://www.nvidia.com/Download/driverResults.aspx/184785/en-us>
          - Beta Drivers (QNF) (**Not always current**): <https://www.nvidia.com/Download/driverResults.aspx/182231/en-us>
          - GTX 1080 (GRD) (**For 1080 cards only**): <https://www.nvidia.com/Download/driverResults.aspx/185108/en-us>
          - GTX 1080 (Studio) (**Only if the GRD driver does not work**): <https://www.nvidia.com/Download/driverResults.aspx/184781/en-us>

        **Notes:**
          - If running NVidia Drivers prior to 511.09 please ensure you update your drivers as there are critical CPU and other bugs in older drivers.
          - Driver installation can potentially glitch the streamer, so __**prior to installation**__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher.
          - Geforce/Quadro Experience and Gamestream features have the capability to brick your Shadow use Care..
          - Quadro Experience works well and can help with keeping Quadro Drivers updated: <https://www.nvidia.com/en-us/design-visualization/software/quadro-experience/>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="drivers")

    @commands.command(aliases=['purchaseghost', 'buyghost', 'ghostinfo', 'ghostmanual'])
    async def ghost(self, ctx, user: typing.Optional[discord.Member] = None):
        """Ghost Purchase information."""
        text = """Ghosts can no longer be purchased from your account page.
        For the Ghost user manual, see here: http://botrexford.shdw.info/Ghost_Manual.pdf"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ghost")

    @commands.command(aliases=['raz', 'wipe', 'clear'])
    async def reset(self, ctx, user: typing.Optional[discord.Member] = None):
        """Reset Shadow Information"""
        text = """You can reset your shadow via <https://account.shadow.tech/home/my-shadow>, *Note:* This doesn't clear additional storage."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="reset")

    @commands.command()
    async def beta(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send beta download links for desktop platforms."""
        text = """Access the Beta apps at the links below
Windows 64-bit Beta: https://shdw.me/winbeta
Windows 32-bit Beta: https://shdw.me/win32beta
Mac Intel Beta: https://shdw.me/macbeta
Mac Silicon Beta: https://shdw.me/macsiliconbeta
Linux Beta: https://shdw.me/linuxbeta
iOS/tvOS Beta: <https://shdw.me/iosbeta_uk>
Android OS Beta: <https://shdw.me/androidbeta>
Oculus Quest: <https://shdw.me/vrbeta>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="beta")

    @commands.command()
    async def alpha(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send alpha download links (if run in <#593516344415354880>) or link to corresponding channel (if run outside of <#593516344415354880>)."""
        if ctx.message.channel.id == 593516344415354880:
            text = f"""Access the alpha apps at the links below
Windows 64-bit Alpha: https://shdw.me/winalpha
Windows 32-bit Alpha: https://shdw.me/winalpha32
Mac Intel Alpha: https://shdw.me/macalpha
Mac ARM Alpha: https://shdw.me/macarmalpha
Linux Alpha: https://shdw.me/linuxalpha"""
        else:
            text = f"""Access the alpha apps (and receive community support) in our <#593516344415354880> Discord channel.
            Note You will need to get the appropriate (Alpha) role from <#752944295153238136> to see the channel for Alpha.. 

**Please note that there is no official support provided for alpha versions.  The only source of community support for alpha is the <#593516344415354880> channel.**"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="alpha")

    @commands.group(name="account")
    async def account(self, ctx):
        pass

    @account.command(aliases=['account'])
    async def myaccount(self, ctx, user: typing.Optional[discord.Member] = None):
            text = f"""You can access your account page via <https://account.shadow.tech/home>."""
            await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account")

    @account.command()
    async def myshadow(self, ctx, user: typing.Optional[discord.Member] = None):
            text = f"""You can reset your shadow via <https://account.shadow.tech/home/my-shadow>."""
            await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account reset")

    @account.command()
    async def security(self, ctx, user: typing.Optional[discord.Member] = None):
            text = f"""You can access the security page via <https://account.shadow.tech/home/security>."""
            await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account security")

    @account.command()
    async def billing(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""You can access the billing page via <https://account.shadow.tech/home>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account financial")

    @account.command()
    async def subscription(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""From: {ctx.author.name}\n{user.mention}, You can access the subscription page via <https://account.shadow.tech/home>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account subscription")

    @account.command(aliases=['apps'])
    async def applications(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""You can get the current stable and beta applications from <https://account.shadow.tech/home/applications>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account apps")

    @account.command()
    async def refer(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""Want to earn credit for referring your friends to Shadow? see  <https://account.shadow.tech/home/referral>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account apps")

    @account.command(name='support')
    async def support(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""Having an issue with your Shadow? Can't seem to solve the issue here? Ask Support: <https://help.shadow.tech/hc/en-gb/articles/360018626660-Support-Request-Form>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account apps")

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
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        **Windows**
            - OS: Windows 10 or Windows 8.1 (Older versions are not supported)
            - CPU: 
                - Intel Sandy Bridge range (2011), Core™ i7 / i5 / i3, Pentium™, Celeron™, Xeon 1.60 GHz
                - AMD AM2+ range (2008), Athlon™, Sempron™, Phenom™, Opteron™
            - RAM: 2 GB
            - Additional Software: DirectX 9c or higher

        **Mac**
        - OS: OS X 10.12.2 Sierra or higher
        - CPU x86-64 (Intel Core 2 Duo processor, Intel Core i3 / i5 / i7, or Xeon) or ARM M1
        - Firmware System EFI 64-bit
        - RAM: 2 GB
        - Hard Drive Space: 8GB

        **Linux**
        - Ubuntu: Bionic Beaver (18.04), Eoan Ermine (19.10)
        - CPU: 
            - Intel Sandy Bridge range (2011), Core™ i7 / i5 / i3, Pentium™, Celeron™, Xeon 1.60 GHz
            - AMD AM2+ range (2008), Athlon™, Sempron™, Phenom™, Opteron™
        RAM: 2 GB
        Required additional software libva-glx2"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="minreq")

    @commands.command()
    async def ping(self, ctx):
        """Ping command"""
        import datetime
        if await self.bot.admin.can_run_command(ctx.author.roles):
            now = datetime.datetime.utcnow().replace(tzinfo=None)
            delta = (now - ctx.message.created_at.replace(tzinfo=None)).total_seconds()*1000
            await ctx.send('Pong! Server ping {:.3f}ms API ping: {:.3f}ms :ping_pong:'.format(delta, self.bot.latency*1000))

    @commands.command(aliases=['applications', 'application', 'app'])
    async def apps(self, ctx, user: typing.Optional[discord.Member] = None):
        """Link to the download page for Shadow Applications."""
        text = """You can download the Shadow client from the Appplications section of your account page: https://account.shadow.tech/home/applications
 Stable versions include: Windows 32/64 bit, macOS Intel/Silicon, Android, iOS, Linux
 Beta versions include: Windows 32/64 bit, macOS Intel/Silicon, Android, iOS, Linux
 Each version has a designated channel in Discord. To view these channels, you will need to select the proper role from the <#752944295153238136> channel. Feedback on the beta versions should be left in the proper channels."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="apps")

    @commands.command(aliases=['official'])
    async def stable(self, ctx, user: typing.Optional[discord.Member] = None):
        """Provide links to stable clients for desktop applications."""
        text = """Access the Official apps at the links below
Windows 64-bit: https://shdw.me/windows
Windows 32-bit: https://shdw.me/windows32
Mac Intel: https://shdw.me/mac
Mac M1: https://shdw.me/macsilicon
Linux: https://shdw.me/linux
iOS/tvOS: <https://shdw.me/iosApp>
Android OS: <https://shdw.me/android>
Oculus Quest: <https://shdw.me/vr_earlyaccess>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="stable")


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
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="keys")


    @commands.command(aliases=['vralpha', 'vr'])
    async def vrforum(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send VR Forum Links"""
        text = """Download the Shadow VR application from Sidequest at <https://shdw.me/vr_earlyaccess>.
        """
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="vr")

    @commands.command(aliases=['val','valorant'])
    async def _valorant(self, ctx, user: typing.Optional[discord.Member] = None):
        """Valorant Command"""
        self.bot.logger.info(f"Processed valorant command for {ctx.author.name} with parameter {user}.")
        text = """Like so many gamers around the world, we're excited for the official release of Valorant!
         
Due to Riot Games' anti-cheat system, Vanguard, it is currently not possible to play on virtual machines, like Shadow. We are currently looking into potential solutions so all of you at #TeamShadow can get in some sweet competitive MP action.
 
As soon as we have more information, you will be the first to know. To stay up-to-date, you can also refer to our Help Center article.

__Games with Issues Identified on Shadow__
<https://help.shadow.tech/hc/en-gb/articles/360013641620-Games-with-Issues-Identified-on-Shadow>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="valorant")

    @commands.command(aliases=['gen','genshin','genshit'])
    async def _genshin(self, ctx, user: typing.Optional[discord.Member] = None):
        """Valorant Command"""
        self.bot.logger.info(f"Processed genshit command for {ctx.author.name} with parameter {user}.")
        text = """Shadow is aware of this concern. The Shadow team has contacted Genshin Impact's developers about this issue. For now, it is considered incompatible.

__Games with Issues Identified on Shadow__
<https://help.shadow.tech/hc/en-gb/articles/360013641620-Games-with-Issues-Identified-on-Shadow>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="genshin")

    @commands.command(aliases=['act', 'activation'])
    async def activationupdates(self, ctx, user: typing.Optional[discord.Member] = None):
        """Activation updates"""
        text = """:rocket: For the latest activation updates please see your Shadow account page."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="activationupdates")

    @commands.command(aliases=['storage', 'stor', 'sto'])
    async def _storage(self, ctx, user: typing.Optional[discord.Member] = None):
        """Storage tutorial command"""
        text = """**How to add storage**:
First Sign in to your account page via https://sso.shadow.tech/
<https://botrexford.shdw.info/sso.png>
Then go to your Subscription/Billing Section:
<https://botrexford.shdw.info/sub-billing.png>
Hit Add Storage:
<https://botrexford.shdw.info/storage-dialog.png>
Choose how much you want and follow prompts, when adding storage ensure your ***Shadow is OFF***"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="storage")


    @commands.command(aliases=['ips','geoip'])
    async def ip(self, ctx, user: typing.Optional[discord.Member] = None):
        """IP/Geoip Information"""
        self.bot.logger.info(f"Processed ip command for {ctx.author.name} with parameter {user}.")
        text = """Trying to find the geographic location of your Shadow using websites which detect it via your IP address will likely be inaccurate, because Blade occasionally moves IP addresses around between its datacenters.
 If you suspect your Shadow is on the wrong datacenter, first find your Shadow's public IP using http://ipv4bot.whatismyipaddress.com/:
            - **Europe**
                - If your IP begins with **185.161.** you are on the **Amsterdam** datacenter
                - If your IP begins with **85.190.** you are on the **France** datacenter
            - **North America**
                - If your IP begins with **170.249.[92-95].** you are on the **California** datacenter
                - If your IP begins with **162.213.[48-55].** you are on the **New York** datacenter
                - If your IP begins with **216.180.[128-143]** you are on the **Texas** datacenter"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ip")

    @commands.command(aliases=['sup'])
    async def _support(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send details for how to reach support."""
        text = """  This is a community-based Discord where other members of the community may be able to assist with your issues in <#752963617627963412>, however please be aware that most folks here aren't Shadow Employees, and although Shadow employees do occasionally interact here, this isn't an official support channel.
  Therefore if the troubleshooting provided here does not resolve your issue, or to leave feedback directly to Shadow, you will need to contact Shadow Support:
  - From your account page, click Support: https://account.shadow.tech/home/support
  - If you are unable to access your account page, use the Help Desk: https://help.shadow.tech/hc/en-gb/articles/360018626660-Support-Request-Form"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="sup")

    @commands.command(aliases=['appletv', 'appletvbeta'])
    async def atv(self, ctx, user: typing.Optional[discord.Member] = None):
        """Apple TV Testflight invite link"""
        text = """You can download the Apple TV app here: <https://shdw.me/AppleTV>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="atv")

    @commands.command(aliases=['iphone', 'ios'])
    async def _apps_ios(self, ctx, user: typing.Optional[discord.Member] = None):
        """iOS apps"""
        text = """You can download the iOS app here: <https://shdw.me/iOSApp>
You can join the iOS app beta here: <https://shdw.me/iosbeta_uk>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ios")

    @commands.command(aliases=['map', 'coveragemap', 'locations'])
    async def coverage(self, ctx, user: typing.Optional[discord.Member] = None):
        """Coverage Maps"""
        text = """**Shadow Coverage maps:**
            North America - <https://shdw.me/NACoverage>
            Europe - <https://shdw.me/EUCoverage>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="coverage")

    @commands.command(aliases=['ltt', 'linus'])
    async def linustechtips(self, ctx, user: typing.Optional[discord.Member] = None):
        """Linus Tech Tips"""
        self.bot.logger.info(f"Processed linustechtips command for {ctx.author.name} with parameter {user}.")
        text = """Check out the Linus Tech Tips video exploring what's inside a Shadow's server at https://shdw.me/LTTVideo
See the video where Linus visted the Mountain View office and datacenter tour at <https://www.youtube.com/watch?v=0BQ4bXNdEQI>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="linustechtips")

    @commands.command(aliases=['dct', 'datacentertour'])
    async def dctour(self, ctx, user: typing.Optional[discord.Member] = None):
        """AMS1 Datacenter Tour"""
        text = """Check Out a tour of one of our datacenters found here: https://youtu.be/0BQ4bXNdEQI?t=157"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="dctour")

    @commands.command(aliases=['hstats', 'statspage', 'sscp', 'scps'])
    async def stats(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to access Shadow Control panel stats pane."""
        text = """The Stats page in the shadow control panel can provide useful troubleshooting information (IPS, 
        Bitrate, Ping and Packet Loss) to access it please this http://botrexford.shdw.info/how_to_access_stats.png """
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="hstats")

    @commands.command(aliases=['language'])
    async def changelang(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to Change language from FR to EN."""
        text = """How to change the language of your Shadow: https://help.shadow.tech/hc/en-gb/articles/360000902673-Change-the-Language-for-Windows-10"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="changelang")

    @commands.command(aliases=['virtualhere', 'vhere'])
    async def vh(self, ctx, user: typing.Optional[discord.Member] = None):
        """Virtual Here Information"""
        text = """**Get VirtualHere** -- **VirtualHere** works to share ***a single USB device*** (without paying, get a license for more than one) over *your local network*. 

**VirtualHere** *server* on your local machine (you'll have to run it every time you get on Shadow).

**VirtualHere** *client* on the Shadow (again, you'll have to run it each time to get on Shadow, running it as an automatic Windows service is a paid feature).

When prompted, VirtualHere will ask you to install **Bonjour**; do this. It makes life easier by making the VH client find the VH server hub automagically. Do this on both client and server installations when prompted.

Next step is getting Shadow on your local area network (LAN).

You can use **Hamachi** (Guide) <https://documentation.logmein.com/documentation/EN/pdf/Hamachi/LogMeIn_Hamachi_UserGuide.pdf> or **ZeroTier** (Guide) <https://docs.google.com/document/d/1NcVK11lcS8m2G_0fsqMcXvkcdLWdaU2O4Vc_qyJrnng/edit?usp=sharing>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="vh")


    @commands.command()
    async def usbdk(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send USB Dev Kit Downloads/info"""
        text = """USB Development Kit Drivers are needed for proper functioning of USB over IP on Windows
        Normally the Shadow client will install these drivers however sometimes this install fails you can manually download and install them from here
         - **Windows 32bit** - http://botrexford.shdw.info/UsbDk_1.0.21_x86.msi
         - **Windows 64bit** - http://botrexford.shdw.info/UsbDk_1.0.21_x64.msi
        Once installed reboot your local system and USB over IP should function normally, ***___Note Install these on your local PC not your shadow.___***"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="usbdk")

    @commands.command()
    async def ghc(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Ghost CS Message for AMA."""
        text = """Today our European team announced limited availability of the Shadow Ghost for sale in their territories. Here in the US, we’re still finalizing our plans to make the Shadow Ghost available for our community, but until then, please sign up on the official waiting list to indicate your interest. If you’ve already signed up, no need to do so again. Just to be up front about things, the quantities we’re talking about, both in the US and Europe are pretty small, so it’s possible that not everyone on the waiting list will be able to get a Shadow Ghost in the next round.

Thanks for your interest, and we’ll have more information as soon as we can lock down details.

<https://shdw.me/NA-waiting-list-SGDC>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ghc")

    @commands.command()
    async def cake(self, ctx):
        await ctx.message.add_reaction("🍰")

    @commands.command()
    async def math(self, ctx, *, parameters):
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(f"{ctx.author.mention} Your not authorized to do that...")
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
        """Teach a person to fish."""
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(f"{ctx.author.mention} Your not authorized to do that...")
            return
        args2 = args.replace(' ', '+')
        url = "https://lmgtfy.com/?q=" + str(args2)
        await ctx.send(embed=discord.Embed(description="**[Look here!](%s)**" % url, color=discord.Color.gold()))
        await ctx.message.delete()

    @commands.command(aliases=['rm', 'roadmap'])
    async def _roadmap(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Shadow roadmap: <https://forum.shadow.tech/roadmap-release-notes-24?sort=dateline.desc>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="roadmap")

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
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="s101")

    @commands.command(aliases=['windows'])
    async def win(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Access the Windows apps at the links below
Official: https://shdw.me/windows
Beta: https://shdw.me/winbeta
Alpha: Accessible at <#593516344415354880>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="win")
        
    @commands.command(aliases=['windows32'])
    async def win32(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Access the Windows 32 bit apps at the links below
**WARNING**: Limited features in these versions, only download if you have a 32 bit device!
Official: https://shdw.me/windows32
Beta: https://shdw.me/win32beta
Alpha: Accessible at <#593516344415354880>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="win32")

    @commands.command(aliases=['macos'])
    async def mac(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Access the macOS apps at the links below
__Intel__
Official: https://shdw.me/mac
Beta: https://shdw.me/macbeta

__ARM__
Official: https://shdw.me/macsilicon
Beta: https://shdw.me/macsiliconbeta
Alpha: Accessible at <#593516344415354880>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="mac")

    @commands.command(aliases=['ubuntu'])
    async def linux(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Access the Linux apps at the links below
Official: https://shdw.me/linux
Beta: https://shdw.me/linuxbeta
Alpha: Accessible at <#593516344415354880>

__Known Issues with Linux Application__
View these helpful sources if you are having issues installing Shadow on Linux
<https://nicolasguilloux.github.io/blade-shadow-beta/setup>
<https://help.shadow.tech/hc/en-gb/articles/360011233839-Known-Issues-for-Shadow>

__Other Resources__
Other resources and applications to help you with your Shadow journey
Shadowcker (Run Shadow in Docker): <https://gitlab.com/aar642/shadowcker>
Shadow liveOS (Shadow on a portable drive): <https://gitlab.com/NicolasGuilloux/shadow-live-os>
Shadow Shades (Linux Support Server): <https://discord.gg/9HwHnHq>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="linux")

    @commands.command(aliases=['pixel'])
    async def android(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """You can download the Android app here: <https://shdw.me/android>
You can join the Android app beta here: <https://shdw.me/androidbeta>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="android")

    @commands.command(aliases=['_ask'])
    async def ask(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """https://www.dontasktoask.com/"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ask")

    @commands.command(aliases=['contribute'])
    async def github(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Access the GitHub for Bot Rexford <https://github.com/stavlor/Shadow-Shortcuts> 
Contribute to Bot Rexford by submitting your ideas and bugs here! <https://github.com/stavlor/Shadow-Shortcuts/issues?"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="github")

    @commands.command(aliases=[])
    async def copypasta(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""If you could perhaps consider this optimal strategy, which could facilitate about your own reward. There exists a contraption that enables one to - with a few strokes of the fingers to depress buttons in a sequence of letters to formulate a word, and then a sentence. Which if phrased as a question, could result in an answer. I believe you know of this contraption called the computer, if - when in use with the internet, one could maneuver oneself onto a place referred to as a website; I will help you in this prospect for I know of the address: www.google.com. When you find yourself in this place, you will see a box in which you could - once again, maneuver your fingers in the correct sequence in order to arrange an assortment of questions that would result in the delivery of your much needed answer.

Sincerely,
Your friend,
{ctx.author.mention}"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="copypasta")

    @commands.command(aliases=['shaduwu'])
    async def shadowo(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """https://cdn.discordapp.com/attachments/550519535606956032/739318032022634566/shadowo_wallpaper.png"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="shadowo", suppress_from=True)

    @commands.command(aliases=['specs', 'tiers'])
    async def _specs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """
***___Shadow___***
**GPU:** Quadro P5000 (GeForce GTX 1080 Equiv.)
**VRAM:** 16 GB
**CPU:** Intel Xeon E5-2678v3 Processor
**CPU Clock Speed:** 2.5 GHz Turbo @ 4 cores - Turbo to 3.2 GHz
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
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="_specs")

    @commands.command(aliases=['ntfs', 'xbox', 'gamepass'])
    async def vhdx(self, ctx, user: typing.Optional[discord.Member] = None):
        """Provide workarounds for installation of XBox Game Pass titles."""
        text = """Microsoft Store/XBox Game Pass apps/games cannot be installed on a vanilla Shadow instance due to a UWP disk format limitation, however...

***...there are two popular solutions to allow these apps/games to be installed on Shadow.***

**Solution 1: Reformat Storage**
Please see the relevant Reddit post for details: https://www.reddit.com/r/ShadowPC/comments/h0pifp/xbox_game_pass_and_ntfs_error_workaround/
*Note that the above solution also details some of the reasons for the incompatibility and is a good read even if you decide to go with option 2.*

**Solution 2: Create a VHDX (virtual hard disk) file**
Please see the instructions at: https://www.windowscentral.com/how-create-and-set-vhdx-or-vhd-windows-10

***Note that you **must** set the allocation size to 4 kB for either option to work!***

*Note: You may have to change the location within Windows settings, put in the Windows search "Storage Settings" then Change where new content is saved > New apps will save to.

Then within the Xbox Beta app go to Settings > General > Drive Selection. If not changed, change it.*
"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="vhdx")

            
    @commands.command(aliases=['sendlogs', 'slogs'])
    async def _sendlogs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """To Send client logs to Shadow Support please see the following: 
        https://botrexford.shdw.info/Send_Logs.png"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="sendlogs")


def setup(bot):
    bot.add_cog(General(bot))
