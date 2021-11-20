from discord.ext import commands, tasks
import discord
import traceback


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.events = self
        bot.logger.info("Initialized Events Cog")
        self.check_status.start()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.message.add_reaction("😢")
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            await ctx.author.send("{author.mention} {exception}".format(author=ctx.author, exception=exception))
            await ctx.message.add_reaction('✋')
        elif isinstance(exception, discord.ext.commands.errors.BadArgument):
            await ctx.send(
                "{author.mention} Bad Argument exception: {exception}".format(author=ctx.author, exception=exception))
        elif isinstance(exception, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("{author.mention} Required argument missing: {exception}".format(author=ctx.author,
                                                                                            exception=exception))
        elif isinstance(exception, discord.NotFound):
            await ctx.send("{author.mention} Got a discord.NotFound error: {exception}".format(author=ctx.author,
                                                                                               exception=exception))
        elif isinstance(exception, discord.ext.commands.CheckFailure):
            await ctx.send(f"{ctx.author.mention} You are not authorized to perform this command.")
        self.bot.logger.info(
            "Error encountered processing command enacting message: {ctx.message} enacting user: {ctx.author.name} Exception: {exception}\nTraceback:{traceback}".format(
                ctx=ctx, exception=exception, traceback=traceback.format_tb(exception.__traceback__)))

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info(
            "Bot Starting up.. Logged in as:" + str(self.bot.user.name) + " ID: " + str(self.bot.user.id))
        self.bot.logger.info("Preparing to start webserver.")
        await self.bot.web.webserver()
        self.bot.logger.info("Webserver should be running.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        from tzlocal import get_localzone
        from datetime import datetime
        tz = get_localzone()
        curtime = datetime.now()
        await self.bot.database.update_leaver_roles(member)
        log_chan1 = await self.bot.fetch_channel(462170485787066368)
        log_chan2 = await self.bot.fetch_channel(464371559214219264)
        embed = discord.Embed(title=f"Member left: {member}")
        embed.add_field(name="Discord ID:", value=f"{member.id}")
        roles = list()
        guild = self.bot.get_guild(460948857304383488)
        applied_roles = list()
        SQL = f"SELECT roles FROM role_tracking WHERE discord_id='{member.id}' LIMIT 1;"
        async with self.bot.dbpool.acquire() as connection:
            res = await connection.fetch(SQL)
        if len(res) != 0:
            res = res.pop()
        res = dict(res)
        if res is not None:
            roles = res['roles']
            for item in str(roles).split(','):
                if item is not None:
                    if item == '':
                        continue
                    role = guild.get_role(int(item))
                    if role is None:
                        continue
                    if role.name == "@everyone":
                        continue
                    if role is not None:
                        applied_roles.append(role)
        embed.add_field(name="Roles Recorded:", value=f"{applied_roles}", inline=False)
        embed.set_footer(text=f"Processed at: {curtime.isoformat()} {tz}")
        await log_chan1.send(embed=embed)
        await log_chan2.send(embed=embed)



    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if before.roles != after.roles:
            await self.bot.database.update_leaver_roles(after)
            await self.bot.database.check_prisoner_roles(after)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.database.re_apply_roles(member)

    @commands.Cog.listener()
    async def on_message(self, message):
        self.bot.logger.debug(
            "Recieved message from {message.author} Content {message.content}".format(message=message))
        if isinstance(message.channel, discord.DMChannel):
            if message.author.id == self.bot.user.id:
                return
            if message.author.bot:
                return
            await self.bot.database.log_direct_messages(message)
            await message.author.send(
                "{message.author.mention} your message has been logged, This is an automated bot.".format(
                    message=message))
        if message.author.bot:
            return
        if not hasattr(message.author, 'roles'):
            role_names = []
        else:
            role_names = message.author.roles
        if message.author.id == self.bot.user.id:
            return  # Don't react to our own messages.
        elif message.role_mentions != list():
            if not await self.bot.admin.can_run_command(role_names):
                self.bot.logger.info(f"Role mentions: {message.role_mentions}")
                await message.channel.send(
                    f"{message.author.mention} Please don't mass tag, unless an absolute emergency. Thanks.")
        elif ("L:104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="L:104")
        elif ("L 104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="L 104")
        elif (" 104" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="104")
        elif ("shadow is off" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message=f"{message.author.mention} hit the :grey_question:  then scroll down and hit ***Shutdown Shadow***,  wait 2-5 minutes then restart your client http://botrexford.shdw.info/reboot.gif",
                                                             trigger="104")
        elif "800x600" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix issues with 800x600 resolution http://botrexford.shdw.info/800x600.png",
                                                             trigger="800x600")
        elif "input lag" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following tips for solving input lag issues http://botrexford.shdw.info/inputlag.png",
                                                             trigger="input lag")
        elif "shadowapples" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} This is not the ShadowApples Discord. This is a Discord for Shadow, a high performance computer in the cloud. You can find the official ShadowApples Discord in the description of their channel.",
                                                             trigger="shadowapples")
        elif "shadow apples" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} This is not the ShadowApples Discord. This is a Discord for Shadow, a high performance computer in the cloud. You can find the official ShadowApples Discord in the description of their channel.",
                                                             trigger="shadow apples")
        elif "drive" in message.content.lower() and ("slow" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} If you are currently experiencing issues with your additional storage post migration, please put in a support ticket from your account page.",
                                                             trigger="drive")
        elif "password expired" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="""{ctx.author.mention} Ready-To-Go Password Update
If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903) - 

If you have any issues updating the default password is blank “” if your password is expired.""",
                                                             trigger="password expired")
        elif "expired password" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="""{ctx.author.mention} Ready-To-Go Password Update
            If you used the Ready-To-Go setting when setting up your account, any version prior to Windows 10 1903 has an expired password notice approximately 1-3 months after activation. This bug has been fixed by Windows. To fix, simply update to the latest Windows version. (1903) - 

            If you have any issues updating the default password is blank “” if your password is expired.""",
                                                             trigger="password expired")
        elif "waiting for video" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "video error" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "long to boot up" in message.content.lower() and not await self.bot.admin.can_run_command(role_names):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="waiting for video")
        elif "3/3" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Please see the following to fix waiting for video http://botrexford.shdw.info/waiting_for_video.png",
                                                             trigger="3/3")
        elif "halo infinite crash" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Halo Infinite is currently not playable on Shadow due to detection of virtual machines. This issue is being worked on by Shadow. For more information, see: https://help.shadow.tech/hc/en-gb/articles/360011233839-Known-Issues-for-Shadow",
                                                             trigger="halo infinite crash")
        elif "halo infinite crashing" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message,
                                                             message="{ctx.author.mention} Halo Infinite is currently not playable on Shadow due to detection of virtual machines. This issue is being worked on by Shadow. For more information, see: https://help.shadow.tech/hc/en-gb/articles/360011233839-Known-Issues-for-Shadow",
                                                             trigger="halo infinite crashing")
        elif "valorant" in message.content.lower() and not (await self.bot.admin.can_run_command(role_names)):
            await self.bot.autoresponse.auto_response_message(ctx=message, message="""{ctx.author.mention} Unfortunately, Valorant is not compatible with Shadow at this time. This is due to the nature of the game's "Vanguard" anti-cheat and how it is installed. Since Riot uses a custom anti-cheat mechanism, this makes it nearly impossible to run on virtual machines, including cloud platforms. 

Check here for the current list of Shadow issues: <https://help.shadow.tech/hc/en-gb/articles/360011233839-Known-Issues-for-Shadow>""")
        elif "good bot" in message.content.lower():
            await message.add_reaction("🍪")
            await message.add_reaction("👍")
        elif "bad bot" in message.content.lower():
            await message.add_reaction("😢")
            await message.add_reaction("🖕🏼")
        elif "alpha" in message.content.lower() and ("download" in message.content.lower() or "link" in message.content.lower() or "get" in message.content.lower()) and not (await self.bot.admin.can_run_command(role_names)):
            if message.channel.id == 593516344415354880:
                await self.bot.autoresponse.auto_response_message(ctx=message,
                    message="""{ctx.author.mention}\nAccess the alpha apps at the links below
Windows Alpha: https://shdw.me/winalpha
Mac Alpha: https://shdw.me/macalpha
Linux Alpha: https://shdw.me/linuxalpha""",
                    trigger="alpha")
            else:
                await self.bot.autoresponse.auto_response_message(ctx=message,
                    message="""{ctx.author.mention}\nAccess the alpha apps (and receive community support) in our <#593516344415354880> Discord channel.

**Please note that there is no official support provided for alpha versions. The only source of community support for alpha is the <#593516344415354880> channel.**""",
                    trigger="alpha")
    
    @tasks.loop(minutes=5.0)
    async def check_status(self):
        from tzlocal import get_localzone
        from datetime import datetime
        tz = get_localzone()
        curtime = datetime.now()
        msg = await self.bot.get_channel(633713376316620829).fetch_message(734769170847105114)
        if await self.bot.admin.get_status() == "All services operating normally":
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0x00ff00)
            embed.add_field(name="All services operating normally",
                            value="For additional status information please see the status page", inline=True)
            embed.set_footer(text=f"Automatically updated message. Last Update was at {curtime.isoformat()} {tz}")
            await msg.edit(embed=embed)
        else:
            status = await self.bot.admin.get_status()
            embed = discord.Embed(title="Shadow Status", url="https://status.shadow.tech", color=0xff8040)
            embed.add_field(name=status,
                            value="For additional status information please see the status page", inline=True)
            embed.set_footer(text=f"Automatically updated message. Last Update was at {curtime.isoformat()} {tz}")
            await msg.edit(embed=embed)
    
    @check_status.before_loop
    async def before_check_status(self):
        self.bot.logger.info('Waiting for bot to start before triggering status updates...')
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        from datetime import datetime, timedelta
        files = list()
        url = str()
        attachments_present = False
        audit_user = 'self'
        ignored_channels = ['bot_users', 'mods-and-gurus', 'bot-logs', 'known-issues', 'mods']
        cur_time = datetime.utcnow().isoformat()
        cur_raw_time = datetime.utcnow()
        author = message.author
        content = message.content
        channel = message.channel
        async for entry in message.guild.audit_logs(limit=5, action=discord.AuditLogAction.message_delete, oldest_first=False):
            if entry.target.id == author.id:
                self.bot.logger.info(f"AL-Debug: E:{entry} T:{entry.target} U:{entry.user} B:{entry.before} A:{entry.after} ACT:{entry.action} ")
                if cur_raw_time - entry.created_at > timedelta(minutes=1):
                    self.bot.logger.info(f"Found possible match, but times aren't in range {entry} c:{entry.created_at} rt:{cur_raw_time} P: {cur_raw_time - entry.created_at}")
                else:
                    self.bot.logger.info(f"Match? Audit_Log_entry time: {entry.created_at}, rt: {cur_raw_time} P:{cur_raw_time-entry.created_at}")
                    audit_user = entry.user
        if audit_user == 'self':
            self.bot.logger.info(f"No match in audit logs, Self Deleted.")
        if channel in ignored_channels:
            return
        if message.author.id == self.bot.user.id:
            return
        dest_channel = await self.bot.fetch_channel(462170485787066368)
        if message.content.startswith("\\"):
            return
        for attachment in message.attachments:
            try:
                files.append(await attachment.to_file(use_cached=True))
            except discord.errors.NotFound:
                attachments_present = True
                url += f"{attachment.url} "
                continue
        embed = discord.Embed(title=f"Message was deleted in Channel: {channel}", color=0xcc66c0)
        embed.add_field(name="Message:", value=f"{message.content} sent by {message.author}", inline=False)
        if url is not str() and attachments_present:
            embed.add_field(name="Attachments-Deleted:", value=url)
        embed.add_field(name="Deleted By:", value=f"{audit_user}", inline=False)
        embed.set_footer(text=f"Message initially created at: {message.created_at} Deleted at: {cur_time}")
        await dest_channel.send(embed=embed, files=files)


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        dest_channel = await self.bot.fetch_channel(462170485787066368)
        ignored_channels = ['greeters', 'mods-and-gurus', 'bot-logs', 'known-issues', 'mods']
        if after.channel in ignored_channels:
            return
        if after.author.id == self.bot.user.id:
            return
        e = discord.Embed(title=f"Message was edited in Channel: {after.channel}", color=0xcc66c0)
        e.add_field(name="Message Author:", value=f'{after.author}', inline=False)
        e.add_field(name="Prior Content:", value=f"{before.system_content}", inline=False)
        e.add_field(name="New Content:", value=f"{after.system_content}", inline=False)
        e.add_field(name="Message URI:", value=after.jump_url, inline=False)

        e.set_footer(text=f"Message initial creation timestamp: {after.created_at} edited at {after.edited_at}.")
        await dest_channel.send(embed=e)


def setup(bot):
    bot.add_cog(Events(bot))
