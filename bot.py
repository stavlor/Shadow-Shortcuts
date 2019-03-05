import sys
import logging
import traceback
from discord.ext import commands

description = "Shadow US Discord helper bot.\nFor issues with this bot please contact <@151891678511235072>.\n"
TOKEN = "NTUwMDMxMzU0MDEyNzYyMTc3.D1chbg.GDk9sZ6CxAPJ7Auy8N_Cmtrya-U"
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
handler.setLevel(logging.INFO)
logger.addHandler(handler)
bot = commands.AutoShardedBot(command_prefix='.', description=description)
bot.last_message = dict()
bot.logger = logger
initial_extensions = ['cogs.admin',
                      'cogs.autoresponse',
                      'cogs.events',
                      'cogs.general']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            logger.info(f'Failed to load extension {extension}.')
            traceback.print_exc()

bot.run(TOKEN)
