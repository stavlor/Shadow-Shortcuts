from discord.ext import commands
import discord
import typing


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.general = self
        bot.logger.info("Initialized General Cog")

    async def text_command_process(self, ctx: commands.Context, user: discord.Member, text: str, command_name: str):
        if await self.bot.admin.can_run_command(ctx.author.roles):
            self.bot.logger.info(f"{command_name} recieved from {ctx.author.name} with argument of {user}")
            if user is not None:
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

Send a clear **screenshot** of <https://account.shadow.tech/subscription> (click the Subscription link or this link again after you log in) to a Moderator or Shadow Guru to verify you are a subscriber.

**Note:** Do not send a friend request. If you are unable to send a DM, adjust your Privacy Settings for this server (you can change it back after). See here for more info: <https://support.discordapp.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="verify")


    @commands.command(description="L:104 Error Troubleshooting tips.", aliases=['fix104', '104', 'l104', 'rebootshadow', 'restartshadow', 'sd', 'error104'])
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

    @commands.command(description="microphone fix", aliases=['mic', 'micguide'])
    async def micfix(self, ctx, user: typing.Optional[discord.Member] = None):
        """Microphone fix information."""
        text = """To get your microphone working in Shadow please follow this guide: https://wiki.shadow.pink/index.php/Using_a_Microphone"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="micfix")

    @commands.command(description="Speedtest-Links")
    async def speedtest(self, ctx, user: typing.Optional[discord.Member] = None):
        """Speedtest Links"""
        text = """Speedtest.net links
    NORTH AMERICA
    Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
    Central DC(Texas): <http://www.speedtest.net/server/12190>
    East DC(NY): <http://www.speedtest.net/server/14855>
    West DC(CA): <http://www.speedtest.net/server/11613>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="micfix")

    @commands.command(aliases=['terms', 'tou'])
    async def tos(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send Terms of Service information"""
        text = """__Terms of Use__
- See the official Terms of Use here: <https://shadow.tech/usen/terms>
- For a simple breakdown of what's not allowed on shadow, see here: <https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow>
 **Note:** ***Whether it's in the above links or not,*** we ask that you respect others' intellectual properties while using Shadow, and that covers piracy and cheating."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="tos")

    @commands.command(aliases=['nvidiadrivers', 'drovers'])
    async def drivers(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send current NVidia Drivers Info."""
        text = """**Current Nvidia Drivers for P5000** -- [__*US has only P5000s*__] [__*Non-US users may have GTX1080*__]
          - Stable Drivers (ODE)  *(**Recommended**)*: <https://www.nvidia.com/Download/driverResults.aspx/162431/en-us>

        **Notes:**
          - If running NVidia Drivers prior to 430.64 please ensure you update your drivers as there are critical CPU and other bugs in older drivers.
          - Driver installation can potentially glitch the streamer, so __***prior to installation***__ ensure you have an alternate way to access Shadow. Chrome Remote Desktop is recommended for this <https://remotedesktop.google.com/access/>
          - If the stream cuts out, your first attempt to fix the issue should be to restart streaming from the launcher.
          - GeForce Experience is not recommended as all it can do is give you the latest stable driver which is already linked above. Game settings recommendations do not work, and GameStream and broadcast functions will break your streamer and prevent connection to your Shadow."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="drivers")

    @commands.command(aliases=['purchaseghost', 'buyghost', 'ghostinfo', 'ghostmanual'])
    async def ghost(self, ctx, user: typing.Optional[discord.Member] = None):
        """Ghost Purchase information."""
        text = """Ghosts can be purchased from your account page under Subscription: https://account.shadow.tech/subscription

For the Ghost user manual, see here: http://botrexford.shdw.info/Ghost_Manual.pdf"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ghost")

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
        text = """:warning:  MINIMUM REQUIREMENTS :warning: 

        **Windows**
        - Windows 8.1, Windows 10 Recommended - 32 bits or above (Note: 64 bit required for USBoIP)
        - Processor from 2011-2012 or more recent
        - Integrated GPU recommended
        - AMD GPU from 2013 or more recent (disable if older)
        - Nvidia GPU from 2011 and more recent (disable if older)
        
        **Mac**
        - Mac OS 10.10 Yosemite or above
        - Mac device from 2012 or more recent"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="minreq")

    @commands.command()
    async def ping(self, ctx):
        """Ping command"""
        import datetime
        if await self.bot.admin.can_run_command(ctx.author.roles):
            now = datetime.datetime.utcnow()
            delta = (now - ctx.message.created_at).total_seconds()*1000
            await ctx.send('Pong! Server ping {:.3f}ms API ping: {:.3f}ms :ping_pong:'.format(delta, self.bot.latency*1000))

    @commands.command(aliases=['applications', 'beta', 'update', 'app'])
    async def apps(self, ctx, user: typing.Optional[discord.Member] = None):
        """Link to Shadow Applications download."""
        text = """You can download the Shadow client from the Appplications section of your account page: https://account.shadow.tech/apps
 Stable versions include: Windows 32/64 bit, macOS, Android, iOS
 Beta versions include: Windows 64 bit, macOS, Ubuntu
 Each version has a designated channel in Discord. To view these channels, you will need the Shadower role. Feedback on the beta versions should be left in the proper channels."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="apps")

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

    @commands.command(aliases=['act', 'activation'])
    async def activationupdates(self, ctx, user: typing.Optional[discord.Member] = None):
        """Activation updates"""
        text = """:boom: For the latest activation updates please see the Forum Activation Thread :boom:  
https://shdw.me/activation_updates"""
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
                - If your IP begins with **216.180.[128-135]** you are on the **Texas** datacenter
                - If your IP begins with **216.180.[136-143]** you are on the **Chicago** datacenter"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ip")

    @commands.command(aliases=['sup'])
    async def _support(self, ctx, user: typing.Optional[discord.Member] = None):
        """Send details for how to reach support."""
        text = """  This is a community-based Discord where other members of the community may be able to assist with your issues in <#463782843898658846>, however please be aware that most folks here aren't Blade Employees, and although Blade employees do occasionally interact here, this isn't an official support channel.
  Therefore if the troubleshooting provided here does not resolve your issue, or to leave feedback directly to Shadow, you will need to contact Shadow Support:
  - From your account page, click Support: https://account.shadow.tech/support
  - If you are unable to access your account page, use the Help Desk: https://help.shadow.tech/hc/en-gb/requests/new optionally, e-mail support at **support-us@shadow.tech** note Tickets are generally quicker."""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="sup")

    @commands.command(aliases=['appletv', 'appletvbeta'])
    async def atv(self, ctx, user: typing.Optional[discord.Member] = None):
        """Apple TV Testflight invite link"""
        text = """You can join the Apple TV Testflight via this link from any iOS Device once Testflight is installed: <https://testflight.apple.com/join/h9H54DqA>"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="atv")

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
        text = """Check Out a tour of one of our datacenters found here: https://youtube.com/watch?v=DD3WNXkc7F0"""
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
        text = """How to change the language of your Shadow: https://w.shdw.info/wiki/Change_Language"""
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
        if not await self.bot.admin.can_run_command(ctx.author.roles):
            await ctx.author.send(f"{ctx.author.mention} Your not authorized to do that...")
            return
        args2 = args.replace(' ', '+')
        url = "https://lmgtfy.com/?q=" + str(args2)
        await ctx.send(embed=discord.Embed(description="**[Look here!](%s)**" % url, color=discord.Color.gold()))
        await ctx.message.delete()

    @commands.command(aliases=['rm', 'roadmap'])
    async def _roadmap(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """Shadow roadmap: <https://shdw.me/roadmap>"""
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

    @commands.command(aliases=['ask'])
    async def _ask(self, ctx, user: typing.Optional[discord.Member] = None):
        text = "https://www.dontasktoask.com/"
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="ask")

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
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="_specs")

            
    @commands.command(aliases=['sendlogs', 'slogs'])
    async def _sendlogs(self, ctx, user: typing.Optional[discord.Member] = None):
        text = """To Send client logs to Shadow Support please see the following: 
        https://botrexford.shdw.info/Send_Logs.png"""
        await self.bot.general.text_command_process(ctx=ctx, user=user, text=text, command_name="sendlogs")


def setup(bot):
    bot.add_cog(General(bot))
