import sys
import logging
from discord.ext import commands
import botconfig as cfg

description = "Shadow US Discord helper bot.\nFor issues with this bot please contact Stavlor.\n"
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
bot = commands.AutoShardedBot(command_prefix='\\', description=description)
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
                      'jishaku']

if __name__ == '__main__':
    for extension in initial_extensions:
            bot.load_extension(extension)

bot.run(TOKEN)
