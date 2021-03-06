import sys
import logging
from discord.ext import commands
import discord
import botconfig as cfg

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True
description = "Shadow Discord helper bot.\nFor issues with this bot please submit a report at <https://github.com/stavlor/Shadow-Shortcuts/issues>.\n"
TOKEN = cfg.TOKEN
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler.setLevel(logging.INFO)
logger.addHandler(handler)
bot = commands.AutoShardedBot(command_prefix='\\', description=description, intents=intents)
bot.last_message = dict()
bot.logger = logger
bot.logging_root = logging
bot.config = cfg
initial_extensions = ['cogs.admin',
                      'cogs.autoresponse',
                      'cogs.database',
                      'cogs.events',
                      'cogs.general',
                      'cogs.schedevent',
                      'cogs.web',
                      'jishaku']

if __name__ == '__main__':
    for extension in initial_extensions:
            bot.load_extension(extension)

bot.run(TOKEN)
