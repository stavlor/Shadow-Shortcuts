from discord.ext import commands, tasks
import discord

class SchedEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.schedevent = self
        bot.logger.info("Initialized Scheduled Event Cog")
        self.bot.schedevent.night_mode = False
        self.bot.schedevent.day_mode = False
        self.bot.schedevent.night_mode_delay = 30
        self.bot.schedevent.day_mode_delay = 10
        self.loop.start()


    @tasks.loop(seconds=60)
    async def loop(self):
        from datetime import datetime
        time = datetime.now()
        if (time.hour >= 0) and (time.hour < 9) and not self.bot.schedevent.night_mode:
            self.bot.logger.info("Enacting Nightmode")
            self.bot.schedevent.night_mode = True
            self.bot.schedevent.day_mode = False
            await self.bot.get_channel(687830602317168711).edit(slowmode_delay=self.bot.schedevent.night_mode_delay, reason="Nightmode - Auto")
            await self.bot.get_channel(550519535606956032).send(f"Entering Night mode, Sleep well -- {time}")
        if (time.hour > 8) and self.bot.schedevent.night_mode:
            self.bot.schedevent.day_mode = True
            self.bot.schedevent.night_mode = False
            self.bot.logger.info("Enacting Daymode")
            await self.bot.get_channel(687830602317168711).edit(slowmode_delay=self.bot.schedevent.day_mode_delay, reason="Daymode - Auto")
            await self.bot.get_channel(550519535606956032).send(f"Entering Day mode, Good morning -- {time}")
        self.bot.logger.debug(f"Loop time: {time}")

def setup(bot):
    bot.add_cog(SchedEvent(bot))
