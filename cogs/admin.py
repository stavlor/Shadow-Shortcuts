from discord.ext import commands
import discord
import aiohttp
import traceback
import asyncio
import typing


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.context.prefix}{1.qualified_name} {1.signature}'.format(self, command)


class Admin(commands.Cog):
    """Admin level bot commands cog"""

    def __init__(self, bot):
        import datetime
        self.bot = bot
        self.bot.admin = self
        self._last_member = None
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self
        bot.logger.info("Initialized Admin Cog")
        self.bot.admin.last_bot_users_sm = datetime.datetime.now() - datetime.timedelta(hours=2)

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    @commands.command(hidden=True)
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin')
    async def load(self, ctx, *, module):
        """Loads a module."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators']):
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))
            return
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('```py\n{traceback}\n```'.format(traceback=traceback.format_exc()))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff', 'Code Approvers')
    async def logout(self, ctx):
        await ctx.send(f"{ctx.author.mention} begining bot shutdown..")
        await self.bot.logout()

    @commands.command(hidden=True)
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Code Approvers')
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators']):
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))
            return
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send('```py\n{traceback}\n```'.format(traceback=traceback.format_exc()))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(name='reload', hidden=True)
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin','Shadow Staff', 'Code Approvers')
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        if not module.startswith('cogs.'):
            module = f'cogs.{module}'
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators','Shadow Staff', 'Code Approvers']):
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))
            return
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('```py\n{traceback}\n```'.format(traceback=traceback.format_exc()))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @staticmethod
    async def can_run_command(role_check, allowed=None):
        role_check = [role.name for role in role_check]
        if allowed is None:
            allowed = ['Shadow Guru', 'Community Manager', 'Moderators', 'Shadow Staff', 'Code Approvers', 'Admin', 'Greeters']
        for item in allowed:
            if item in role_check:
                return True
        return False

    @staticmethod
    async def tail(filename, lines):
        import subprocess
        output = subprocess.getoutput("tail -n {lines} {filename}".format(filename=filename, lines=lines))
        return output

    async def get_status(self):
        import lxml.html
        async with aiohttp.ClientSession() as session:
            html = await self.bot.admin.fetch(session, 'https://status.shadow.tech')
            doc = lxml.html.fromstring(html)
            status_text = doc.xpath('//strong[@id="statusbar_text"]')[0].text_content()
            return status_text

    async def get_excuse(self):
        import json
        async with aiohttp.ClientSession() as session:
            html = await self.bot.admin.fetch(session, 'https://pe-api.herokuapp.com')
            doc = json.loads(html)
            return doc

    @staticmethod
    async def fetch(session, url, timeout=10):
        async with session.get(url, timeout=timeout) as response:
            return await response.text()


    @commands.command(aliases=['excuse'])
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff', 'Bot User')
    async def _excuse(self, ctx, user: typing.Optional[discord.Member] = None):
        excuse = await self.get_excuse()
        if user is None:
            await ctx.send(excuse['message'])
        else:
            await ctx.send(f"Sent by: {ctx.author.name}\n{user.mention} {excuse['message']}")
        await ctx.message.delete()

    @commands.command(aliases=['latency', 'trace', 'tr', 'tracert', 'traceroute', 'traces', 'lg', 'guru'])
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def _latency(self, ctx, user: typing.Optional[discord.Member] = None):
        text = '''To diagnose latency or packet loss on your Shadow, check out this wiki page https://wiki.shdw.info/w/PingPlotter'''
        await self.bot.general.text_command_process(ctx, user, text, "latency")

    @commands.command(aliases=['slo', 'sm'])
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def slowmode(self, ctx, timer: int = 5):
        """Change Channel Slowmode"""
        await ctx.channel.edit(slowmode_delay=timer, reason=f"Requested change by {ctx.author}")
        await ctx.send(f"{ctx.author.mention} Slowmode timer updated to {timer} seconds.")


    @commands.command(aliases=['botsm', 'bsm'])
    @commands.has_role('Bot User')
    async def _bot_user_slowmode(self, ctx, timer: int = 10, *, reason: str):
        """Bot User Slowmode"""
        import datetime
        last_time_diff = datetime.datetime.now() - datetime.timedelta(minutes=30)
        if self.bot.admin.last_bot_users_sm < last_time_diff and timer in ['10', '20', '30', '40', '50', '60'] and timer > ctx.channel.slowmode_delay:
            self.bot.admin.last_bot_users_sm = datetime.datetime.now()
            await ctx.channel.edit(slowmode_delay=timer, reason=f"Requested change by {ctx.author} {reason}")
            await ctx.send(f"{ctx.author.mention} Slowmode timer increased to {timer}")
            dest_channel = await self.bot.fetch_channel(462170485787066368)
            embed = discord.Embed(title=f"Altered Slowmode for #{ctx.channel.name}", color=0xeb1291)
            embed.add_field(name="Requested by:", value=ctx.author)
            embed.add_field(name="Slowmode Delay:", value=str(timer))
            embed.add_field(name="Reason", value=reason)
            await dest_channel.send(embed=embed)
            await ctx.message.delete()
        else:
            await ctx.author.send(f"{ctx.author.mention} this command is limited to once every 30 minutes shared across all bot users and with a requirement that timer is in  ['10', '20', '30', '40', '50', '60']; and that a reason be properly supplied. Something did not meet these requirements.")
            await ctx.message.delete()


    @commands.command(description="Auto-Responders debug", name="timertest")
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin')
    async def _timertest(self, ctx):
        """Auto-responder timer debug tool"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderator']):
            timers = " "
            for item in self.bot.last_message.keys():
                timers += "{:10s} - {:10s}\n".format(item, self.bot.last_message[item].isoformat())
            await ctx.send("Timer debug:\n```{timers}```".format(timers=timers))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(name='ar')
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def add_role(self, ctx, user: discord.Member, *,  roles: commands.Greedy[discord.Role] = None):
        """Adds a role to a User default is Shadowers."""
        if roles is None:
            roles = list()
            roles.append(ctx.guild.get_role(461298541978058769))
        elif isinstance(roles, discord.Role):
            oroles = roles
            roles = list()
            roles.append(oroles)
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff']):
            for role in roles:
                if user is None:
                    await ctx.send(f"{ctx.author.mention} User is a required parameter.")
                else:
                    if role not in user.roles:
                        await user.add_roles(role)
                        await ctx.message.add_reaction('✅')
                        await user.send(f"{user.mention} You have been granted the role {role.name} by {ctx.author}")
                    else:
                        await ctx.send(f"{ctx.author.mention} User {user.mention} appears to already have the {role.name} role.")
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(description="Grant a user bot access", name='grantbot')
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def add_role_bot(self, ctx, user: typing.Optional[discord.Member] = None):
        """Grant Bot User Role to a user - Admin"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators']):
            if user is None:
                await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
            else:
                if "Greeters" not in [role.name for role in user.roles]:
                    shadowers = ctx.guild.get_role(551917324949651477)
                    await user.add_roles(shadowers)
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.send("{author} User {user.mention} appears to already have this role.".format(
                        author=ctx.author.mention, user=user))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(description="Revoke a user bot access", name='revokebot')
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def revoke_role_bot(self, ctx, user: typing.Optional[discord.Member] = None):
        """Revoke Bot User Role from a user - Admin"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Shadow Staff']):
            if user is None:
                await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
            else:
                if "Greeters" in [role.name for role in user.roles]:
                    shadowers = ctx.guild.get_role(551917324949651477)
                    await user.remove_roles(shadowers)
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.send("{author} User {user.mention} appears to not have this role.".format(author=ctx.author.mention, user=user))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(description="Roles test", name='roletest')
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def _roletest(self, ctx):
        """Admin - Role ID Listing tool"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators']):
            paginator = discord.ext.commands.Paginator()
            guild = ctx.guild
            paginator.add_line("Beginning role debug")
            for role in guild.roles:
                paginator.add_line("{role.id}: {role.name}".format(role=role))
            for page in paginator.pages:
                await ctx.send(page)
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff', 'Code Approvers')
    async def gitref(self, ctx):
        """Refresh git repo content."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Shadow Staff', 'Code Approvers']):
            await ctx.send(f"{ctx.author.mention} You aren't authorized to do that.")
        else:
            cmd = "git pull"
            proc = await asyncio.create_subprocess_shell(
                cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            stdout, stderr = await proc.communicate()
            await ctx.send(f'{ctx.author.mention} [{cmd!r} exited with {proc.returncode}]')
            if stdout:
                await ctx.send(f'[stdout]\n{stdout.decode()}')
            if stderr:
                await ctx.send(f'[stderr]\n{stderr.decode()}')

    async def find_message_history(self, user: discord.Member, guild: discord.Guild, message_count: int = 10):
        import queue
        final_messages = list()
        messages = queue.Queue(maxsize=message_count)
        async for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=5000):
                    if message.author == user:
                        if not messages.full():
                            messages.put(message)
            except:
                continue
        while not messages.empty():
            rec = messages.get()
            final_messages.append(rec)
        return final_messages


    @commands.command(aliases=['ui', 'uinfo'])
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def userinfo(self, ctx, user: commands.Greedy[discord.Member] = None):
        """Look up general user info."""
        import datetime
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Shadow Staff']):
            await ctx.send(f"{ctx.author.mention} your not authorized to do that.")
            return
        elif user is None:
            await ctx.send(
                f"{ctx.author.mention} Could not locate Guild Member, note this command requires the user to be a member of the Discord Guild.")
        for users in user:
            avi = users.avatar_url_as(static_format='png')
            em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
            if isinstance(users, discord.Member):
                role = users.top_role.name
            if role == '@everyone':
                role = "N/A"
            em.add_field(name='Nick', value=users.nick, inline=True)
            em.add_field(name='User ID', value=users.id, inline=True)
            em.add_field(name='Status', value=users.status, inline=True)
            em.add_field(name='Activity', value=users.activity, inline=True)
            em.add_field(name='Highest Role', value=role, inline=True)
            voice_state = None if not users.voice else users.voice.channel
            em.add_field(name='In Voice', value=str(voice_state), inline=True)
            rolelist = ""
            for role in users.roles:
                if rolelist is not "":
                    rolelist += f", {role.name}"
                else:
                    rolelist += f"{role.name}"
            em.add_field(name='Roles', value=rolelist, inline=True)
            now = datetime.datetime.now()
            joined_delta = now - users.joined_at
            createdat_delta = now - users.created_at
            joinedat = users.joined_at.strftime('%A, %d. %B %Y @ %H:%M:%S')
            createdat = users.created_at.strftime('%A, %d. %B %Y @ %H:%M:%S')
            created_str = f"{createdat} ({createdat_delta})"
            joined_str = f"{joinedat} ({joined_delta})"
            mobile = users.is_on_mobile()
            em.add_field(name='Joined at', value=joined_str, inline=True)
            em.add_field(name='Created at', value=created_str, inline=True)
            em.add_field(name='Mobile', value=mobile, inline=True)
            em.set_thumbnail(url=avi)
            em.set_author(name=users, icon_url='https://i.imgur.com/RHagTDg.png')
            await ctx.send(embed=em)
            

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators', 'Admin', 'Shadow Staff')
    async def rr(self, ctx, user: discord.Member, role: typing.Optional[discord.Role] = None, all_roles: bool = False):
        """Remove Roles - remove role from a user defa- Optional True/False for all_roles will remove all roles from a user."""
        if role is None:
            role = ctx.guild.get_role(461298541978058769)
        if all_roles:
            for role in user.roles:
                if role.name != "@everyone":
                    role = ctx.guild.get_role(int(role.id))
                    await user.remove_roles(role, reason=f"Requested removal by {ctx.author.name}")
        else:
            await user.remove_roles(role, reason=f"Requested removal by {ctx.author.name}")
        await ctx.message.add_reaction('✅')

    @commands.command(description="Bot Logs")
    @commands.has_any_role('Shadow Guru', 'Community Manager', 'Moderators', 'Shadow Staff')
    async def logs(self, ctx):
        """Logs Command"""
        if await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Community Manager', 'Moderators', 'Shadow Staff']):
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

    @commands.command(aliases=['openth', 'startth'])
    @commands.has_any_role('Shadow Staff', 'Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators')
    async def begin_town_hall(self, ctx):
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        overwrite.send_messages = True
        if ctx.guild.id != 460948857304383488:
            await ctx.send(f"{ctx.author.mention} this isn't in the correct guild.")
            return
        shadowers = ctx.guild.get_role(461298541978058769)
        channel = ctx.guild.get_channel(543131120355770378)
        everyone = ctx.guild.default_role
        await channel.set_permissions(everyone, overwrite=overwrite, reason=f'Townhall requested by {ctx.author}')
        await channel.set_permissions(shadowers, overwrite=overwrite, reason=f'Townhall requested by {ctx.author}')
        await ctx.send(f"{ctx.author.mention} completed, new permissions should be in effect for {str(channel)}")

    @commands.command(aliases=['endth', 'closeth'])
    @commands.has_any_role('Shadow Staff', 'Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators')
    async def end_town_hall(self, ctx):
        overwrite = discord.PermissionOverwrite()
        overwrite.read_messages = True
        overwrite.send_messages = False
        if ctx.guild.id != 460948857304383488:
            await ctx.send(f"{ctx.author.mention} this isn't in the correct guild.")
            return
        shadowers = ctx.guild.get_role(461298541978058769)
        channel = ctx.guild.get_channel(543131120355770378)
        everyone = ctx.guild.default_role
        await channel.set_permissions(everyone, overwrite=overwrite, reason=f'Townhall requested by {ctx.author}')
        await channel.set_permissions(shadowers, overwrite=overwrite, reason=f'Townhall requested by {ctx.author}')
        await ctx.send(f"{ctx.author.mention} completed, new permissions should be in effect for {str(channel)}")

    @commands.command(aliases=['sayin'])
    @commands.has_any_role('Admin', 'Shadow Staff', 'Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators')
    async def say_in_channel(self, ctx, channel: discord.TextChannel, *,  message: str):
        await channel.send(message)
        await ctx.send(f"{ctx.author.mention} Completed")

    @commands.command()
    @commands.has_any_role('Admin', 'Shadow Staff', 'Shadow Guru', 'Community Manager', 'Head of Community', 'Shadow Support Lead', 'Shadow Customer Support', 'Moderators')
    async def strings(self, ctx):
        import json
        paginator = discord.ext.commands.Paginator()
        paginator.add_line("Current Database Strings:")
        async with self.bot.dbpool.acquire() as connection:
            async with connection.transaction():
                async for record in connection.cursor(f"SELECT string_id, string_name, data from strings ORDER by string_id ASC;"):
                    id = record['string_id']
                    name = record['string_name']
                    data = json.loads(record['data'])
                    paginator.add_line(f"{id}: {name}:: {data}")
            for page in paginator.pages:
                await ctx.send(page)




def setup(bot):
    bot.add_cog(Admin(bot))
