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
        self.bot = bot
        self.bot.admin = self
        self._last_member = None
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self
        bot.logger.info("Initialized Admin Cog")

    def cog_unload(self):
        self.bot.help_command = self._original_help_command

    @commands.command(hidden=True)
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def load(self, ctx, *, module):
        """Loads a module."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))
            return
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('```py\n{traceback}\n```'.format(traceback=traceback.format_exc()))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))
            return
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send('```py\n{traceback}\n```'.format(traceback=traceback.format_exc()))
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(name='reload', hidden=True)
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        if not module.startswith('cogs.'):
            module = f'cogs.{module}'
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
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
            allowed = ['Shadow Guru', 'Moderators', 'Shadow Staff', 'Clay\'s Lieutenants', 'Admin', 'Silent Admin',
                       'Administrator', 'Bot User']
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

    @staticmethod
    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()

    @commands.command(description="Auto-Responders debug", name="timertest")
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def _timertest(self, ctx):
        """Auto-responder timer debug tool"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderator']):
            timers = " "
            for item in self.bot.last_message.keys():
                timers += "{:10s} - {:10s}\n".format(item, self.bot.last_message[item].isoformat())
            await ctx.send("Timer debug:\n```{timers}```".format(timers=timers))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(name='ar')
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def add_role(self, ctx, user: discord.Member, *,  role: typing.Optional[discord.Role] = None):
        """Adds a role to a User default is Shadowers."""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            if role is None:
                role = ctx.guild.get_role(461298541978058769)
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
    @commands.has_any_role('Shadow Guru', 'Moderator', 'Admin')
    async def add_role_bot(self, ctx, user: typing.Optional[discord.Member] = None):
        """Grant Bot User Role to a user - Admin"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            if user is None:
                await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
            else:
                if "Bot User" not in [role.name for role in user.roles]:
                    shadowers = ctx.guild.get_role(551917324949651477)
                    await user.add_roles(shadowers)
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.send("{author} User {user.mention} appears to already have this role.".format(
                        author=ctx.author.mention, user=user))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(description="Revoke a user bot access", name='revokebot')
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def revoke_role_bot(self, ctx, user: typing.Optional[discord.Member] = None):
        """Revoke Bot User Role from a user - Admin"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            if user is None:
                await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
            else:
                if "Bot User" in [role.name for role in user.roles]:
                    shadowers = ctx.guild.get_role(551917324949651477)
                    await user.remove_roles(shadowers)
                    await ctx.message.add_reaction('✅')
                else:
                    await ctx.send("{author} User {user.mention} appears to not have this role.".format(author=ctx.author.mention, user=user))
        else:
            await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))

    @commands.command(description="Roles test", name='roletest')
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def _roletest(self, ctx):
        """Admin - Role ID Listing tool"""
        if await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
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
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def gitref(self, ctx):
        """Refresh git repo content."""
        if not await self.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send(f"{ctx.author.mention} You aren't authorized to do that.")
        else:
            cmd = "cd ~/Shadow-Shortcuts/; git pull"
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

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def userinfo(self, ctx, user: commands.Greedy[discord.Member] = None):
        """Look up general user info."""
        if not await self.bot.admin.can_run_command(ctx.author.roles, ['Shadow Guru', 'Moderators']):
            await ctx.send(f"{ctx.author.mention} your not authorized to do that.")
            return
        elif user is None:
            await ctx.send(
                f"{ctx.author.mention} Could not locate Guild Member, note this command requires the user to be a member of the Discord Guild.")
        for users in user:
            paginator = discord.ext.commands.Paginator(prefix='```css', suffix='```')
            paginator.add_line(f"User-ID: {users.id}\tUsername+discriminator: {users}\tDisplay name: {users.display_name}")
            rolelist = ""
            for role in users.roles:
                rolelist += f"{role.name}({role.id}) "
            paginator.add_line(f"Has roles: {rolelist}")
            joinedat = users.joined_at.strftime('%Y-%m-%d %H:%M:%S')
            createdat = users.created_at.strftime('%Y-%m-%d %H:%M:%S')
            paginator.add_line(f"Joined on: {joinedat}\tCreated at: {createdat}")
            paginator.add_line(f"Status: {users.status}\tActivity: {users.activity}")
            for page in paginator.pages:
                await ctx.send(page)

    @commands.command()
    @commands.has_any_role('Shadow Guru', 'Moderators', 'Admin')
    async def rr(self, ctx, user: discord.Member, role: typing.Optional[discord.Role] = None, all_roles: bool = False):
        """Remove Roles - remove role from a user  defa- Optional True/False for all_roles will remove all roles from a user."""
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
    @commands.has_any_role('Shadow Guru', 'Moderators')
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


def setup(bot):
    bot.add_cog(Admin(bot))
