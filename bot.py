import sys
import logging
import discord
import aiohttp
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


async def can_send_message(last_message):
    import datetime
    difference = last_message - datetime.datetime.now()
    if difference.total_seconds() < 120:
        return False
    else:
        return True


async def check_last_message(message):
    import datetime
    if message.channel.name not in bot.last_message.keys():
        bot.last_message[message.channel.name] = datetime.datetime.now()
        return True
    elif await can_send_message(bot.last_message[message.channel.name]):
        bot.last_message[message.channel.name] = datetime.datetime.now()
        return True
    else:
        return False


async def auto_response_message(ctx, message: str=None, trigger: str=None):
    if isinstance(ctx, discord.DMChannel):
        await ctx.author.send(content=message.format(ctx=ctx))
    elif await check_last_message(message=ctx):
        logger.info("Auto-Response Triggered, Trigger: {trigger} sending to channel {ctx.channel.name} Triggering-Message: {ctx.content}".format(trigger=trigger, ctx=ctx))
        await ctx.channel.send(content=message.format(ctx=ctx))
    else:
        logger.info(
            "Auto-Response Triggered, Trigger: {trigger} sending via PM to {ctx.author.name} Triggering-Message: {ctx.content} Last Message: {last}".format(
                trigger=trigger, ctx=ctx, last=bot.last_message[ctx.channel.name]))
        await ctx.author.send(content=message.format(ctx=ctx))
        await ctx.add_reaction("📬")


async def can_run_command(role_check, allowed=None):
    if allowed is None:
        allowed = ['Shadow Guru', 'Moderators', 'Shadow Staff', 'Clay\'s Lieutenants', 'Admin', 'Silent Admin',
                   'Administrator', 'Bot User']
    for item in allowed
        if item in role_check:
            return True
    return False


async def tail(filename, lines):
    import subprocess
    output = subprocess.getoutput("tail -n {lines} {filename}".format(filename=filename, lines=lines))
    return output


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_status():
    import lxml.html
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://status.shadow.tech')
        doc = lxml.html.fromstring(html)
        status_text = doc.xpath('//strong[@id="statusbar_text"]')[0].text_content()
    if "All Systems Operational" == status_text:
        return "Normal"
    else:
        return status_text


@bot.event
async def on_ready():
    logger.info("Bot Starting up.. Logged in as:" + str(bot.user.name) + " ID: " + str(bot.user.id))


@bot.event
async def on_command_error(ctx, exception):
    await ctx.message.add_reaction("😢")
    logger.info("Error encountered processing command enacting message: {ctx.message} enacting user: {ctx.author.name} Exception: {exception}".format(ctx=ctx, exception=exception))


@bot.event
async def on_message(message):
    logger.debug("Recieved message from {message.author} Content {message.content}".format(message=message))
    author = message.author
    if not hasattr(author, 'roles'):
        role_names = []
    else:
        role_names = [role.name for role in author.roles]
    if message.author.id == bot.user.id:
        pass
    elif str(message.content).startswith('.'):
        await bot.process_commands(message)
    elif "good bot" in message.content.lower():
        await message.add_reaction("🍪")
        await message.add_reaction("👍")
    elif "bad bot" in message.content.lower():
        await message.add_reaction("😢")
        await message.add_reaction("🖕🏼")
    elif "error 102" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message, message="{ctx.author.mention} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png", trigger="error 102")
    elif "102 error" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message, message="{ctx.author.mention} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png", trigger="102 error")
    elif "800x600" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message,
                                    message="{ctx.author.mention} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png",
                                    trigger="800x600")
    elif "input lag" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message,
                                    message="{ctx.author.mention} Please see the following tips for solving input lag issues http://core.stavlor.net/inputlag.png",
                                    trigger="input lag")
    elif "password expired" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message,
                                    message="{ctx.author.mention} Please see the following for expired password messages http://core.stavlor.net/password.png",
                                    trigger="password expired")
    elif "expired password" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message,
                                    message="{ctx.author.mention} Please see the following for expired password messages http://core.stavlor.net/password.png",
                                    trigger="password expired")
    elif "waiting for video" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message, message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png", trigger="waiting for video")
    elif "video error" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message, message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png", trigger="waiting for video")
    elif "long to boot up" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message, message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png", trigger="waiting for video")
    elif "3/3" in message.content.lower() and not await can_run_command(role_names):
        await auto_response_message(ctx=message,
                                    message="{ctx.author.mention} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png",
                                    trigger="3/3")


@bot.command(description="Auto-Responders debug", name="timertest")
async def _timertest(ctx):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        timers = " "
        for item in bot.last_message.keys():
            timers += "{:10s} - {:10s}\n".format(item, bot.last_message[item].isoformat())
        await ctx.send("Timer debug:\n```{timers}```".format(timers=timers))
    else:
        await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))



@bot.command(description="Send instructions on how to get Verified")
async def verify(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Verify command received from {author.name} with argument of {user}".format(author=ctx.author,
                                                                                        user=user))
        if user is not None:
            await ctx.send(
                "From: {author.name}\n{user} To get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                author=ctx.message.author, user=user.mention))
        else:
            await ctx.send("From: {author.name}\nTo get verified Please DM a Shadow Guru or a Moderator a screenshot of https://account.shadow.tech/subscription to get your Shadower role".format(
                author=ctx.message.author))
    await ctx.message.delete()


@bot.command(description="Add Shadower role to a user", name='ar')
async def add_role(ctx, *, user: discord.Member = None):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        if user is None:
            await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
        else:
            if "Shadowers" not in [role.name for role in user.roles]:
                shadowers = ctx.guild.get_role(461298541978058769)
                await user.add_roles(shadowers)
                await ctx.message.add_reaction('✅')
            else:
                await ctx.send("{author} User {user.mention} appears to already have this role.".format(author=ctx.author.mention, user=user))
    else:
        await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))


@bot.command(description="Grant a user bot access", name='grantbot')
async def add_role_bot(ctx, *, user: discord.Member = None):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        if user is None:
            await ctx.send("{author} User is a required parameter.".format(author=ctx.author.mention))
        else:
            if "Bot User" not in [role.name for role in user.roles]:
                shadowers = ctx.guild.get_role(551917324949651477)
                await user.add_roles(shadowers)
                await ctx.message.add_reaction('✅')
            else:
                await ctx.send("{author} User {user.mention} appears to already have this role.".format(author=ctx.author.mention, user=user))
    else:
        await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))


@bot.command(description="Revoke a user bot access", name='revokebot')
async def revoke_role_bot(ctx, *, user: discord.Member = None):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
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


@bot.command(description="Roles test", name='roletest')
async def _roletest(ctx):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        guild = ctx.guild
        await ctx.send("Beginning role debug")
        for role in guild.roles:
            await ctx.send("{role.id}: {role.name}".format(role=role))
    else:
        await ctx.send("{author} You aren't authorized to do that.".format(author=ctx.author.mention))


@bot.command(description="Waiting for video instructions", name="800x600")
async def _800x600(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
            author=ctx.message.author, user=user))
        if user is not None:
            await ctx.send(
            "From {author.name}\n{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                author=ctx.message.author, user=user.mention))
        else:
            await ctx.send(
            "From {author.name}\nPlease see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png".format(
                author=ctx.message.author))
    else:
        logger.info("Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
            author=ctx.message.author,
            user=user))
        await ctx.author.send(content="""{user} Please see the following to fix issues with 800x600 resolution http://core.stavlor.net/800x600.png""".format(
            user=ctx.author.mention))
    await ctx.message.delete()

@bot.command(description="Waiting for video instructions")
async def waitingvideo(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info("Waiting for video command received from {author.name} with argument of {user}".format(
            author=ctx.message.author, user=user))
        if user is not None:
            await ctx.send(
            "From {author.name}\n{user} Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                author=ctx.message.author, user=user.mention))
        else:
            await ctx.send(
            "From {author.name}\nPlease see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png".format(
                author=ctx.message.author))
    else:
        logger.info("Waiting for video command received from unauthorized user {author.name}, replied via PM. ".format(
            author=ctx.message.author,
            user=user))
        await ctx.author.send(content="""{user}  Please see the following to fix waiting for video http://core.stavlor.net/waiting_for_video.png""".format(
            user=ctx.author.mention))
    await ctx.message.delete()


@bot.command(description="Error 102 Fix.")
async def fix102(ctx, *,  user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info("102 command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
        if user is not None:
            await ctx.send(
            "From: {author.name}\n{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                author=ctx.message.author, user=user.mention))
        else:
            await ctx.send("From: {author.name}\nPlease follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png".format(
                author=ctx.message.author))
    else:
        logger.info("Error 102 Fix command received from unauthorized user {author.name}, replied via PM. ".format(
            author=ctx.message.author,
            user=user))
        await ctx.author.send(content="""{user} Please follow the following instructions to resolve error 102: http://core.stavlor.net/fix_102.png""".format(
            user=ctx.author.mention))
    await ctx.message.delete()


@bot.command(description="Default pass")
async def password(ctx, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Password command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                          user=user))
        if user is not None:
            await ctx.send("From: {author.name}\n{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(
            author=ctx.message.author, user=user.mention))
        else:
            await ctx.send("From: {author.name}\nPlease see the following for expired password messages http://core.stavlor.net/password.png".format(
            author=ctx.message.author))
    else:
        logger.info("Password command received from unauthorized user {author.name}, replied via PM. ".format(author=ctx.message.author))
        await ctx.author.send(
                               content="{user} Please see the following for expired password messages http://core.stavlor.net/password.png".format(user=ctx.message.author.mention))
    await ctx.message.delete()


@bot.command(description="microphone fix")
async def micfix(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Mic Fix command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                         user=user))
        if user is not None:
            await ctx.send("From: {author.name}\n{user.mention} To get your microphone working in Shadow please follow this guide: "
                      "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                                     user=user))
        else:
            await ctx.send(
                "From: {author.name}\nTo get your microphone working in Shadow please follow this guide: "
                "https://wiki.shadow.pink/index.php/Using_a_Microphone".format(author=ctx.author,
                                                                               user=user))
    else:
        logger.info("Mic Fix command received from unauthorized user {author.name}, replied via PM. ".format(author=ctx.author,
                                                                                             user=user))
        await ctx.author.send(content="""{user} To get your microphone working in Shadow please follow this guide: "
                      "https://wiki.shadow.pink/index.php/Using_a_Microphone""".format(user=ctx.author.mention))
    await ctx.message.delete()


@bot.command(description="ghost manual")
async def ghostmanual(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.message.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Ghost manual command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                              user=user))
        if user is not None:
            await ctx.send("From: {author.name}\n{user} Ghost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
            author=ctx.message.author, user=user))
        else:
            await ctx.send("From: {author.name}\nGhost Manual: http://core.stavlor.net/Ghost_Manual.pdf".format(
                author=ctx.message.author))
    else:
        logger.info("Ghost Manual command received from unauthorized user {author.name}, replied via PM. ".format(author=ctx.author,
                                                                                             user=user))
        await ctx.author.send("""{user} Shadow Ghost Manual http://core.stavlor.net/Ghost_Manual.pdf""".format(user=ctx.author.mention))
    await ctx.message.delete(ctx.message)


@bot.command(description="Latency command")
async def latency(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.author.roles]
    if await can_run_command(role_names):
        logger.info("Latency command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
        if user is not None:
            await ctx.send("""From {author.name}\n{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(author=ctx.author, user=user.mention))
        else:
            await ctx.send("""From {author.name}\nCommon steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(
                author=ctx.author))
    else:
        await ctx.author.send("""{user} Common steps for fixing input latency http://core.stavlor.net/inputlag.png""".format(user=ctx.author.mention))
        logger.info("Latency command received from unauthorized user {author.name}, replied via PM. ".format(author=ctx.author,
                                                                                             user=user))
    await ctx.message.delete()


@bot.command(description="Speedtest-Links")
async def speedtest(ctx, *,  user: discord.Member = None):
    role_names = [role.name for role in ctx.author.roles]
    if await can_run_command(role_names):
        logger.info("Speedtest command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
        if user is not None:
            await ctx.send("""From {author.name}\n{user} Speedtest.net links
NORTH AMERICA
Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
Central DC(Texas): <http://www.speedtest.net/server/12190>
East DC(NY): <http://www.speedtest.net/server/22774>
West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author, user=user.mention))
        else:
            await ctx.send("""From {author.name}\nSpeedtest.net links
            NORTH AMERICA
            Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
            Central DC(Texas): <http://www.speedtest.net/server/12190>
            East DC(NY): <http://www.speedtest.net/server/22774>
            West DC(CA): <http://www.speedtest.net/server/11599>""".format(author=ctx.author))
    else:
        await ctx.author.send("""{user} Speedtest.net links
NORTH AMERICA
Midwest DC(Chicago): <http://www.speedtest.net/server/14489>
Central DC(Texas): <http://www.speedtest.net/server/12190>
East DC(NY): <http://www.speedtest.net/server/22774>
West DC(CA): <http://www.speedtest.net/server/11599>""".format(user=ctx.author.mention))
        logger.info("Speedtest command received from unauthorized user {author.name}, replied via PM. ".format(author=ctx.message.author,
                                                                                             user=user))
    await ctx.message.delete()


@bot.command(description="Send the Terms of Service info")
async def tos(ctx, *,  user: discord.Member = None):
    role_names = [role.name for role in ctx.author.roles]
    if await can_run_command(role_names):
        logger.info("TOS command received from {author.name} with argument of {user}".format(author=ctx.message.author,
                                                                                             user=user))
        if user is not None:
            await ctx.send("""From: {author.name}\n{user}  **__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
__READ THE TOS__
https://shadow.tech/usen/terms
https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(author=ctx.author,
                                                                                        user=user.mention))
        else:
            await ctx.send("""From: {author.name}\n**__whether it's in the ToS or not__**, **we ask that you respect other's intellectual properties while using Shadow, and that covers piracy and cheating.**
            __READ THE TOS__
            https://shadow.tech/usen/terms
            https://help.shadow.tech/hc/en-gb/articles/360000455174-Not-allowed-on-Shadow""".format(author=ctx.author))
    await ctx.message.delete()


@bot.command(description="Nvidia Drivers")
async def nvidiadrivers(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                author=ctx.author,
                user=user))
        if user is not None:
            await ctx.send("""From: {author.name}\n{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
            author=ctx.author, user=user.mention))
        else:
            await ctx.send("""From: {author.name}\nCurrent recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                author=ctx.author))
    else:
        logger.info("NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM".format(ctx=ctx))
        await ctx.author.send("{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10".format(
                                   user=ctx.author.mention))
    await ctx.message.delete()


@bot.command(description="Nvidia Drivers")
async def drivers(ctx, *, user: discord.Member = None):
    role_names = [role.name for role in ctx.author.roles]
    if await can_run_command(role_names):
        logger.info(
            "Nvidia Drivers command received from {author.name} with argument of {user}".format(
                author=ctx.author,
                user=user))
        if user is not None:
            await ctx.send("""From: {author.name}\n{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
            author=ctx.author, user=user.mention))
        else:
            await ctx.send("""From: {author.name}\nCurrent recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10""".format(
                author=ctx.author))
    else:
        logger.info("NVidia Drivers command received from un-privileged user {ctx.author.name} Responding Via PM".format(ctx=ctx))
        await ctx.author.send("{user} Current recommended Drivers for P5000 can be found here https://www.nvidia.com/Download/driverResults.aspx/143117/en-us please note these are the current recommended drivers others are not advised.\nVulkan Drivers are another option, if you want bleeding edge use these https://developer.nvidia.com/vulkan-beta-41909-windows-10".format(
                                   user=ctx.author.mention))
    await ctx.message.delete()


@bot.command(description="Send Ghost Purchase info")
async def buyghost(ctx, *, user: discord.Member = None):
    if user is None:
        logger.info("Ghost purchase info command processed for {author.name}".format(author=ctx.message.author))
        await ctx.send(
            "{author.mention} you can purchase ghost from your account page, https://account.shadow.tech/subscription".format(
                author=ctx.mention))
        await ctx.message.delete()
    else:
        role_names = [role.name for role in ctx.author.roles]
        if await can_run_command(role_names):
            logger.info("Ghost purchase info command processed for {author.name} and args {user}".format(
                author=ctx.author, user=user))
            await ctx.send(
                """From: {author.name}\n{user} you can purchase Shadow Ghost from your account page,  https://account.shadow.tech/subscription""".format(
                    author=ctx.author, user=user.mention))
            await ctx.message.delete()


@bot.command(description="Send ghost informational link")
async def ghostinfo(ctx, *, user: discord.Member = None):
    if user is None:
        logger.info("Ghost info command processed for {author.name}.".format(author=ctx.author))
        await ctx.send(
            "{author.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost".format(
                author=ctx.author))
        await ctx.message.delete()
    else:
        role_names = [role.name for role in ctx.author.roles]
        if await can_run_command(role_names):
            logger.info(
                "Ghost info command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                         user=user))
            await ctx.send(
                """From: {author.name}\n{user.mention} Ghost information can be found here, https://shadow.tech/usen/discover/shadow-ghost""".format(
                    author=ctx.author, user=user))
            await ctx.message.delete()


@bot.command(description="Status command")
async def status(ctx, *, user: discord.Member = None):
    if user is None:
        logger.info("Status command processed for {author.name}.".format(author=ctx.message.author))
        if await get_status() == "Normal":
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
            embed.add_field(name="All Systems Normal", value = "For additional status information please see the status page", inline = True)
            await ctx.send(embed = embed)
            await ctx.message.delete()
        else:
            status = await get_status()
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0xff8040)
            embed.add_field(name=status,
                            value="For additional status information please see the status page", inline=True)
            await ctx.send(embed = embed)
            await ctx.message.delete()
    else:
        role_names = [role.name for role in ctx.author.roles]
        if await can_run_command(role_names):
            logger.info("Status command processed for {author.name} with args {user}".format(author=ctx.author,
                                                                                             user=user))
            await ctx.send(
                "From {author.name}\n{user.mention} Current Shadow network status is {status}. For more info see https://status.shadow.tech".format(
                    author=ctx.author, user=user, status=await get_status()))
            await ctx.message.delete()


@bot.command(description="Bot Logs")
async def logs(ctx):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        fname = 'discord.log'
        if "gurus-lab" not in ctx.message.channel.name:
            lines = await tail(filename=fname, lines=10)
            await ctx.author.send("Here is the last few lines of the log\n{log}\n".format(log=lines))
            logger.info("Sending last few log entries to {ctx.author.name} via PM as its not in gurus-lab".format(ctx=ctx))
        else:
            lines = await tail(filename=fname, lines=10)
            await ctx.send("Here is the last few lines of the log\n{log}\n".format(log=lines))
            await ctx.message.delete()
            logger.info("Sending last few log entries to Channel Requestor:{ctx.author}.".format(ctx=ctx))
    else:
        await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
        await ctx.message.delete()
        logger.info("Unauthorized log request from {ctx.author}".format(ctx=ctx))


@bot.command(description="PM test")
async def pmtest(ctx):
    if ("Shadow Guru" in [role.name for role in ctx.author.roles]) or ("Moderators" in [role.name for role in ctx.author.roles]):
        await ctx.author.send("Test")
        await ctx.message.delete()
    else:
        await ctx.send("Sorry {ctx.author.mention} your not authorized to do this.".format(ctx=ctx))
        await ctx.message.delete()
        logger.info("Unauthorized pmtest request from {ctx.author}".format(ctx=ctx))


bot.run(TOKEN)
