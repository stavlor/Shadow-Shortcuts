from discord.ext import commands
import discord
import typing


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    ### Remove the "From {ctx.author.name} blame the bot" from the text command process.
    async def text_command_process(self, ctx: commands.Context, user: discord.Member, text: str, command_name: str,
                                   suppress_from: bool = False):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(f"{command_name} recieved from {ctx.author.name} with argument of {user}")
            if suppress_from and user is not None:
                await ctx.send(f"{user.mention} {text}")
            elif suppress_from and user is None:
                await ctx.send(f"{text}")
            elif user is not None:
                await ctx.send(f"\n{user.mention} {text}")
            else:
                await ctx.send(f"\n{text}")
        else:
            self.bot.logger.info(
                f"{command_name} command received from un-privileged user {ctx.author.name} Responding Via PM")
            await ctx.author.send(f"{ctx.author.mention} {text}")
        await ctx.message.delete()

    @commands.command(description="Send instructions on how to get Verified",
                      aliases=['v', 'welcome', 'intro', 'reception'])
    async def verify(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to get verified command."""
        text = """Welcome to the Shadow-ENG Discord server! We’re happy to have you join us here!

First things first, to get access to the rest of the server, please react to a role in <#983433497530216448> and <#983443571078221885>  . Then, should you so choose, you can add any additional roles you may want through <#983450525292978186>  !

We hope you enjoy your stay!"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="verify")

    @commands.command(description="L:104 Error Troubleshooting tips.",
                      aliases=['fix104', '104', 'l104', 'errorl104', 'rebootshadow', 'restartshadow', 'sd', 'error104'])
    async def shutdown(self, ctx, user: typing.Optional[discord.Member] = None, min_time_to_wait=2, max_time_to_wait=5):
        text = f"""Please access your help menu :grey_question: then scroll down and hit ***Shutdown Shadow***, then wait {min_time_to_wait}-{max_time_to_wait} minutes and restart your client to resolve your issue http://botrexford.shdw.info/reboot.gif"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="shutdown")

    @commands.command(aliases=['expired', 'pass', 'pw', 'pin'])
    async def password(self, ctx, user: discord.Member = None):
        """Default Password help for Ready-to-Go Shadow Images"""
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(
                "Password command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                              user=user))
            if user is not None:
                embed = discord.Embed(color=0x3d8023)
                embed.add_field(name="Ready to go password Expired, Default Password and Workaround",
                                value="If you used the Ready-To-Go setting when setting up your account, you may have an expired password notice approximately 1-3 months after activation. To resolve the issue leave the \"Password\" (first) field empty or blank, you'll be able to specify a new password or you can leave it blank.",
                                inline=True)
                embed.add_field(name='Custom setup - PIN Code - Just a moment... screen',
                                value="If you used the Custom setup and have a PIN code, you may encounter a \"Just a moment...\" screen. To resolve the issue, press ALT-TAB, select the PIN code screen from the Task Switcher and blindly type in your four digit pin, hit TAB, then confirm your four digit PIN, and hit ENTER. ",
                                inline=True)
                await ctx.send(
                    f"\n{user.mention} Please see the following regarding Passwords and PINs:\n",
                    embed=embed)
            else:
                embed = discord.Embed(color=0x3d8023)
                embed.add_field(name="Ready to go password Expired, Default Password and Workaround",
                                value="If you used the Ready-To-Go setting when setting up your account, you may have an expired password notice approximately 1-3 months after activation. To resolve the issue leave the \"Password\" (first) field empty or blank, you'll be able to specify a new password or you can leave it blank.",
                                inline=True)
                embed.add_field(name='Custom setup - PIN Code - Just a moment... screen',
                                value="If you used the Custom setup and have a PIN code, you may encounter a \"Just a moment...\" screen. To resolve the issue, press ALT-TAB, select the PIN code screen from the Task Switcher and blindly type in your four digit pin, hit TAB, then confirm your four digit PIN, and hit ENTER. ",
                                inline=True)
                await ctx.send(
                    f"From: {ctx.author.name}\nPlease see the following regarding Passwords and PINs:\n",
                    embed=embed)
        else:
            self.bot.logger.info(
                "Password command received from unauthorized user {author.name}, replied via PM. ".format(
                    author=ctx.message.author))
            embed = discord.Embed(color=0x3d8023)
            embed.add_field(name="Ready to go password Expired, Default Password and Workaround",
                                value="If you used the Ready-To-Go setting when setting up your account, you may have an expired password notice approximately 1-3 months after activation. To resolve the issue leave the \"Password\" (first) field empty or blank, you'll be able to specify a new password or you can leave it blank.",
                                inline=True)
            embed.add_field(name='Custom setup - PIN Code - Just a moment... screen',
                                value="If you used the Custom setup and have a PIN code, you may encounter a \"Just a moment...\" screen. To resolve the issue, press ALT-TAB, select the PIN code screen from the Task Switcher and blindly type in your four digit pin, hit TAB, then confirm your four digit PIN, and hit ENTER. ",
                                inline=True)
            await ctx.author.send(
                f"{ctx.author.mention} Please see the following regarding Passwords and PINs:\n",
                embed=embed)
        await ctx.message.delete()

    @commands.command(description="L203 Forum Page", aliases=['l203'])
    async def l203forum(self, ctx, user: typing.Optional[discord.Member] = None):
        text = "For additional information on Error L:203 Please see the following forum article: https://shdw.me/HC-B2C-L203"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="l203forum")

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
For a simple breakdown of what's not allowed on shadow, see this help center article: https://shdw.me/HC-B2C-Rules
This article also contains links to the Terms of Use.
 **Note:** ***Whether it's in the above links or not,*** we ask that you respect others' intellectual properties while using Shadow, and that covers piracy and cheating.
If you have a business plan, please contact your business account manager should you have a legitimate use case."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="tos")

    @commands.command(aliases=['nvidiadrivers', 'drovers'])
    async def drivers(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia RTX Quadro Family Devices** (Shadow PC, Shadow Ultra, and Shadow Infinite)
          - RTX Experience is recommended to keep your drivers up to date: <https://www.nvidia.com/en-us/design-visualization/software/rtx-experience/>          

        **Notes:**
          - Game Optimzation is not supported on the following Shadow plans (Shadow PC w/ Power Upgrade, Zenith, Zenith for Makers, Zenith for Enterprise)
          - If running NVidia Drivers prior to 511.09 please ensure you update your drivers as there are critical CPU and other bugs in older drivers.
          - Driver installation can potentially glitch the streamer, so __prior to installation__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher.
          - Geforce/Quadro Experience and Gamestream features have the capability to brick your Shadow use with care...
          """
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="drivers")

    @commands.command(aliases=['purchaseghost', 'buyghost', 'ghostinfo', 'ghostmanual'])
    async def ghost(self, ctx, user: typing.Optional[discord.Member] = None):
        """Ghost Purchase information."""
        text = """Ghosts can no longer be purchased from your account page and are depreciated.
        For the Ghost user manual, see here: http://botrexford.shdw.info/Ghost_Manual.pdf"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ghost")

    @commands.command(aliases=['raz', 'wipe', 'clear'])
    async def reset(self, ctx, user: typing.Optional[discord.Member] = None):
        """Reset Shadow Information"""
        text = """You can reset your shadow via <https://eu.shadow.tech/account/>, on the Shadow PC tab > "Manage my subscription" *Note:* This doesn't clear additional storage and your Shadow PC should be shutdown before resetting."""
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
            Note You will need to get the appropriate (Alpha) role from <#983450525292978186> to see the channel for Alpha.. 

**Please note that there is no official support provided for alpha versions.  The only source of community support for alpha is the <#593516344415354880> channel.**"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="alpha")

    ### Removing the account subcommand and merging it into General
    @commands.command(aliases=['account'])
    async def myaccount(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""You can access your account page via <https://eu.shadow.tech/account/>."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account")

    @commands.command(aliases=['security'])
    async def email(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""You can access the security page via <https://eu.shadow.tech/account/>. > Select the Account tab > Edit my email or password."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account security")

    @commands.command(aliases=['invoices'])
    async def billing(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""You can access the billing page and look at your invoices via <https://eu.shadow.tech/account/>. > Select the Account tab."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account financial")

    @commands.command()
    async def subscription(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""\n{user.mention}, You can access the subscription page via <https://eu.shadow.tech/account/>. > Select the product you want to manage."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account subscription")

    @commands.command()
    async def refer(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""Want to earn credit for referring your friends to Shadow? see <https://eu.shadow.tech/account/> in the lower left corner for your referral code. Terms and Conditions: For now it is only possible to refer someone in the same currency as you, and you are limited to 10 referrals per user"""  ### Enabled
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="account apps")

    @commands.command()
    async def helpdesk(self, ctx, user: typing.Optional[discord.Member] = None):
        text = f"""Check out the Shadow Help Desk here <https://shdw.me/HC-B2C/>"""  ### This link is dynamically changing should Shadow change their helpcenters
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
                self.bot.logger.info(
                    "Status command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                         user=user))
                await ctx.send(
                    "From {author.name}\n{user.mention} Current Shadow network status is {status}. For more info see https://status.shadow.tech".format(
                        author=ctx.author, user=user, status=await self.bot.admin.get_status()))
                await ctx.message.delete()

    @commands.command(aliases=['minimums', 'minimalreq', 'requirements', 'reqs'])
    async def minreq(self, ctx, user: typing.Optional[discord.Member] = None):
        """Give Shadow Minimum requirements"""  
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        For a full overview of the minumum requirements please see this help center article: <https://shdw.me/HC-B2C-Device_Reqs>
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
            delta = (now - ctx.message.created_at.replace(tzinfo=None)).total_seconds() * 1000
            await ctx.send(
                'Pong! Server ping {:.3f}ms API ping: {:.3f}ms :ping_pong:'.format(delta, self.bot.latency * 1000))

    @commands.command(aliases=['applications', 'application', 'app'])
    async def apps(self, ctx, user: typing.Optional[discord.Member] = None):
        """Link to the download page for Shadow Applications."""
        text = """Access the Official apps at the links below
Windows 64-bit: https://shdw.me/windows
Windows 32-bit: https://shdw.me/windows32
Mac Intel: https://shdw.me/mac
Mac M1: https://shdw.me/macsilicon
Linux: https://shdw.me/linux
iOS/tvOS: <https://shdw.me/iosApp>
Android OS: <https://shdw.me/android>
Oculus Quest: <https://shdw.me/vr_earlyaccess>
 Stable versions include: Windows 32/64 bit, macOS Intel/Silicon, Android, iOS, Linux
 Beta versions include: Windows 32/64 bit, macOS Intel/Silicon, Android, iOS, Linux
 Each version has a designated channel in Discord. To view these channels, you will need to select the proper role from the <#983450525292978186> channel. Feedback on the beta versions should be left in the proper channels."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text,
                                                    command_name="apps")  

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
        """Send VR Forum Links"""  ### Add VR Help Center guide
        text = """Download the Shadow VR application from SideQuest at <https://shdw.me/vr_earlyaccess>.
        Once done, login to your headset at the following link and make sure to type the link in all caps, <https://hydra.eu.shadow.tech/device>, 
        Note: If the link for login is <https://shadow.tech/connect> it is an old link and you should update your Shadow VR application from SideQuest.
        """
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="vr")

    @commands.command(aliases=['val', 'valorant'])
    async def _valorant(self, ctx, user: typing.Optional[discord.Member] = None):
        """Valorant Command"""
        self.bot.logger.info(f"Processed valorant command for {ctx.author.name} with parameter {user}.")
        text = """Like so many gamers around the world, we're excited for the official release of Valorant!
         
Due to Riot Games' anti-cheat system, Vanguard, it is currently not possible to play on virtual machines, like Shadow. If you installed Valorant or Vanguard will need to uninstall these applications or reset your Shadow. Please see the Help Center for more information

__Games with Issues Identified on Shadow__
<https://shdw.me/HC-B2C-Known_Issues>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="valorant")

    @commands.command(aliases=['gen', 'genshin', 'genshit'])
    async def _genshin(self, ctx, user: typing.Optional[discord.Member] = None):
        """Valorant Command"""
        self.bot.logger.info(f"Processed genshit command for {ctx.author.name} with parameter {user}.")
        text = """Shadow is aware of this concern. The Shadow team has contacted Genshin Impact's developers about this issue. For now, it is considered incompatible.

__Games with Issues Identified on Shadow__
<https://shdw.me/HC-B2C-Known_Issues>"""
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
Sign in to your account page via https://eu.shadow.tech/account
Choose how much you want and follow prompts, when adding storage ensure your ***Shadow is OFF***"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="storage")

    @commands.command(aliases=['ips', 'geoip'])
    async def ip(self, ctx, user: typing.Optional[discord.Member] = None):
        """IP/Geoip Information"""
        self.bot.logger.info(f"Processed ip command for {ctx.author.name} with parameter {user}.")
        text = """Trying to find the geographic location of your Shadow using websites which detect it via your IP address will likely be inaccurate, because Shadow assigns a local IP address in the country that you purchased in.
 If you suspect your Shadow is on the wrong datacenter, first find your Shadow's public IP using http://eth0.me/:
            - **Europe**
            - If your IP begins with **46.247.[136-140]** you are on the Frankfurt (DEFRA01) datacenter
            - If your IP begins with **46.247.[141]** you are on the Dunkirk (FRDUN02) datacenter
            - If your IP begins with **85.190.[67-91]** you are on the Dunkirk (FRDUN02) datacenter
            - If your IP begins with **185.161.[168-171]** you are on the Dunkirk (FRDUN02) datacenter
            - If your IP begins with **185.253.[168-169]** you are on the Stratsbourg (FRSBG01) datacenter
            - If your IP begins with **185.253.[170-171]** you are on the Dunkirk (FRDUN02) datacenter
            - **North America**
            - If your IP begins with **66.51.[112-115]** you are on the Washington D.C. (USWDC01) datacenter
            - If your IP begins with **66.51.[116-119]** you are on the Portland (USPOR01) data center
            - If your IP begins with **69.58.[92-93]** you are on the Montreal (CAMTL01) data center
            - If your IP begins with **216.180.[128-135]** you are on the Texas (TX1) data center
            - If your IP begins with **216.180.[136]** you are on the Montreal (CAMTL01) data center
            - If your IP begins with **216.180.[137]** you are on the Portland (USPOR01) data center"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ip")

    @commands.command(aliases=['sup'])
    async def support(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send details for how to reach support."""
        text = """This is a community-based Discord where other members of the community may be able to assist with your issues in <#1021479747823337522>, however please be aware that most folks here aren't Shadow Employees, and although Shadow employees do occasionally interact here, this isn't an official support channel.
  Therefore if the troubleshooting provided here does not resolve your issue, or to leave feedback directly to Shadow, you will need to contact Shadow Support:
  - From your account page, click Support: https://eu.shadow.tech/account/
  - If you are unable to access your account page, use the Help Desk: <https://shdw.me/HC-B2C-Support_Form>"""
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
        text = """Check out the Linus Tech Tips video exploring what's inside a Shadow Infinite server at <https://shdw.me/LTTVideo>
                See the video where Luke visited OVHCloud datacenters and factory tour at https://youtu.be/RFzirpvTiOo
                See the video where Linus visited the Mountain View office and Equinix datacenter tour at <https://www.youtube.com/watch?v=0BQ4bXNdEQI>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="linustechtips")

    @commands.command(aliases=['dct', 'datacentertour'])
    async def dctour(self, ctx, user: typing.Optional[discord.Member] = None):
        """SV2 Datacenter Tour"""
        text = """ See the video where Linus visited the Santa Clara Equinix datacenter tour at: https://youtu.be/0BQ4bXNdEQI?t=157
        See the video where Luke visited OVHCloud datacenters and factory tour at: https://youtu.be/RFzirpvTiOo?t=374"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="dctour")

    @commands.command(aliases=['hstats', 'statspage', 'sscp', 'scps', 'qm', 'quickmenu'])
    async def stats(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to access Shadow Control panel stats pane."""
        text = """The Quick Menu let's you adjust Shadow settings while streaming access using the following command
                <:WindowsShadow:555856447691292736>/**⌘** + **Alt** + **O** = Toggle Quick menu
                Note: The Quick Menu with statistics is only avaiable on Windows, Mac, Linux, and Raspberry Pi"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="hstats")

    @commands.command(aliases=['language'])
    async def changelang(self, ctx, user: typing.Optional[discord.Member] = None):
        """How to Change language from FR to EN."""
        text = """How to change the language of your Shadow: https://shdw.me/HC-B2C-Windows_Language"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="changelang")

    @commands.command(aliases=['virtualhere', 'vhere'])
    async def vh(self, ctx, user: typing.Optional[discord.Member] = None):
        """Virtual Here Information"""
        text = """**Get VirtualHere** -- **VirtualHere** works to share ***a single USB device*** (without paying, get a license for more than one) over *your local network*. 

**VirtualHere** *server* on your local machine (you'll have to run it every time you get on Shadow).

**VirtualHere** *client* on the Shadow (again, you'll have to run it each time to get on Shadow, running it as an automatic Windows service is a paid feature).

When prompted, VirtualHere will ask you to install **Bonjour**; do this. It makes life easier by making the VH client find the VH server hub automagically. Do this on both client and server installations when prompted.

Next step is getting Shadow on your local area network (LAN).

You can use **Hamachi** (Guide) <https://documentation.logmein.com/documentation/EN/pdf/Hamachi/LogMeIn_Hamachi_UserGuide.pdf>, **ZeroTier** (Guide) <https://docs.google.com/document/d/1NcVK11lcS8m2G_0fsqMcXvkcdLWdaU2O4Vc_qyJrnng/edit?usp=sharing>, or **TailScale** (Guide) <https://www.reddit.com/r/ShadowPC/comments/pwjtmt/tut_how_to_use_your_external_hard_drive_on_shadow/> """
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
        url = "https://letmegooglethat.com/?q=" + str(args2)
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
        https://shdw.me/HC-B2C-S101"""
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
<https://shdw.me/HC-B2C-Known_Issues>
<https://gitlab.com/aar642/shadow-repackaged>
<https://shadow-codex.com/shadow-linux-known-issues/>
<https://nicolasguilloux.github.io/blade-shadow-beta/setup>

__Other Resources__
Other resources and applications to help you with your Shadow journey (Some of these projects may be unsupport or deprecated by the owner)
Shadowcker (Run Shadow in Docker): <https://gitlab.com/aar642/shadowcker>
Shadow liveOS (Shadow on a portable drive): <https://gitlab.com/NicolasGuilloux/shadow-live-os>
Shadow Shades (Linux Support Server): <https://discord.gg/9HwHnHq>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="linux")

    ### When I'm drunk add RaspberryPi command ### I really need to do this ### NEEDS UPDATE
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
Shadow Bot"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="copypasta")

    @commands.command(aliases=['gpuschedule', 'gpusched', 'gpuscheds'])
    async def gpuschedules(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """**Disable Hardware Accelerated GPU Scheduling**
        1. Go to Settings (Windows Key + I)
        2. Click on System
        3. Click on Display
        4. Click on Graphics Settings (If you do not have this setting, then your graphics card does not support hardware acceleration.)
        5. Click on "Change Default Graphics Settings"
        6. Toggle Off "Hardware Accelerated GPU Scheduling" (If you do not have this setting, then your graphics card does not support hardware acceleration.)"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="shadowo",
                                                    suppress_from=True)

    @commands.command(aliases=['specs', 'tiers'])
    async def _specs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """***___Shadow (Spark)___***
**GPUs:** 
NVIDIA Quadro P5000 with 16GB GDDR5X
NVIDIA GeForce GTX 1080 with 8GB GDDR5X
NVIDIA Quadro RTX 4000 with 8GB GDDR6 (TX1/DEFRA01 only)

**CPUs:**
Intel Xeon E5-2678 v3 4 cores 8 threads at 2.5 GHz with 3.1 GHz Turbo Boost
Intel Xeon E5-2667 v3 4 cores 8 threads at 3.2 GHz with 3.6 GHz Turbo Boost
AMD EPYC 7513 4 cores 8 threads at 2.6 GHz with 3.65 GHz Max Boost Clock

**RAM  & Storage:**
RAM & Storage is variable and will depend on your plan. Please check Shadow's website for more information. *(Extra storage expandable up to 5TB)*

***__Shadow w/ Power Upgrade (Zenith)__***
**GPUs:**
NVIDIA RTX A4500 with 16GB GDDR6 
AMD Radeon RX 6700 XT with 12GB GDDR6
*Early Access Only*: NVIDIA RTX A4000 with 16GB GDDR6  (FRDUN02 only)

**CPU:**
AMD EPYC 7543P 4 cores 8 threads at 2.8 GHz with 3.7 GHz Max Boost Clock

**RAM  & Storage:**
RAM & Storage is variable and will depend on your plan. Please check Shadow's website for more information. *(Extra storage expandable up to 5TB)*

***___Shadow Ultra (Aurora)___*** EU Only
**GPU:** NVIDIA Quadro RTX 5000 with 16GB GDDR6 
**VRAM:** 16 GB

**CPU:**
Intel Xeon W-3235 Processor 3.3 GHz 4 cores 8 threads at 3.3 GHz with 4 GHz Turbo Boost

**RAM  & Storage:**
RAM & Storage is variable and will depend on your plan. Please check Shadow's website for more information. *(Extra storage expandable up to 5TB)*

***___Shadow Infinite (Lightning)___*** EU Only
**GPU:** NVIDIA Quadro RTX 6000 with 24GB GDDR6 
**VRAM:** 24 GB

**CPU:** 
Intel Xeon W-3235 Processor 6 cores 12 threads at 3.3 GHz Turbo with 4 GHz Turbo Boost

**RAM  & Storage:**
RAM & Storage is variable and will depend on your plan. Please check Shadow's website for more information. *(Extra storage expandable up to 5TB)*

__Plan Information__
Shadow PC: <https://shadow.tech/en-gb/specs>
Shadow for Makers: <https://shadow.tech/en-gb/shadow-for-makers/offers>
Shadow for Enterprise: <https://shadow.tech/en-gb/business/offers>"""
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

    @commands.command(aliases=['sendlogs', 'slogs']) ### NEEDS UPDATE
    async def _sendlogs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """To Send client logs to Shadow Support please see the following: 
        https://botrexford.shdw.info/Send_Logs.png"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="sendlogs")


def setup(bot):
    bot.add_cog(General(bot))
