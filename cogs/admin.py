from discord.ext import commands
import discord
import asyncio

class Admin(commands.cog):
    """Admin level bot commands cog"""

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(hidden=True)
    async def load(self, ctx, *, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(hidden=True)
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')

    @commands.command(name='reload', hidden=True)
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(f'```py\n{traceback.format_exc()}\n```')
        else:
            await ctx.send('\N{OK HAND SIGN}')

    async def can_run_command(self, role_check):
        if 'Shadow Guru' in role_check:
            return True
        elif 'Moderators' in role_check:
            return True
        elif 'Shadow Staff' in role_check:
            return True
        elif 'Clay\'s Lieutenants' in role_check:
            return True
        elif 'Admin' in role_check:
            return True
        elif 'Silent Admin' in role_check:
            return True
        elif 'Administrator' in role_check:
            return True
        elif 'Bot User' in role_check:
            return True
        else:
            return False

    async def tail(filename, lines):
        import subprocess
        output = subprocess.getoutput("tail -n {lines} {filename}".format(filename=filename, lines=lines))
        return output


def setup(bot):
    bot.add_cog(Admin(bot))