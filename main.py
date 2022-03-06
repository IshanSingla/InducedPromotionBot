import telethon,os,asyncio,sys,shutil,time,psutil
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, FloodWaitError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, UserBannedInChannelError, PeerFloodError, UserPrivacyRestrictedError, UserAlreadyParticipantError,  UserBannedInChannelError, UserAlreadyParticipantError,  UserPrivacyRestrictedError, ChatAdminRequiredError, ChatWriteForbiddenError, UserChannelsTooMuchError, UserNotParticipantError,ChannelPrivateError, SessionPasswordNeededError, UserBannedInChannelError

from telegraph import upload_file 
API_ID= 12468937
API_HASH= "84355e09d8775921504c93016e1e9438"
BOT_TOKEN = "5180127494:AAH876Hx-5WP9IqPNtFO4EvkozVmO-BjMY8"
OWNERS=[1303790979,1854668908]
Premium=[1303790979,1854668908]
start_time=time.time()
STUFF={}
rar={}
client = telethon.TelegramClient(None, api_id=API_ID , api_hash=API_HASH).start(bot_token=BOT_TOKEN)
acc =[1303790979,1854668908]

async def get_user_join(e):
    try:
        await client(telethon.tl.functions.channels.GetParticipantRequest(channel="InducedBots", participant=e.chat.id))
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        await client.send_message(e.chat.id,"You have not Joined Our Channel\nJoin to Use me For Free\n\nMade with ❤️ By @InducedBots", buttons=[[telethon.Button.url("🎁 Channel1", url=f"https://t.me/InducedBots"),telethon.Button.inline("Check☑️", b"Home"),]])
        return False


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    if not await get_user_join(e):
        return
    but=[
            [
                telethon.Button.inline("Gcast", b"Gcast"),
                telethon.Button.inline("Ucast", b"Ucast"),
            ],

            [
                telethon.Button.inline("🤑 BuyNow", b"Ishan"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
    await e.reply(f"**Welcome Sir!\n\nI'm Induced Peomotion Bot \nMade for Promoting Your Ads\n\nMade with ❤️ By @InducedBots**", buttons=but)

@client.on(telethon.events.CallbackQuery)
async def _(e):
    global rar
    if e.data == b"Ishan":
        await e.answer('Terms & Condition: 24/7 Support Will Be Given To Premium User. If Find Any Fake SS then Direct Ban. No Refund will be given if no valid reason will be given.', alert=True)
        await e.client.send_message(e.chat.id, "250Rs Per Month Cost\n📑 Payment Options\n\n🔸 Paytm\n\n🔸 UPI\n\n🔸 Crypto Currency\n\nNote: Don't forget to send payment screenshot to @InducedSupportBot for plan activation.", buttons=[[telethon.Button.url("Paytm", url=f"https://paytm.me/pxvn-Tr"),telethon.Button.url("UPI", url="https://induced-service-bot.web.app"),telethon.Button.url("Crypto", url=f"https://t.me/InducedSupportBot"),],[telethon.Button.url(": Tutorial Here :", url=f"https://youtu.be/iyz5ky3Mkkc")]])

    elif e.data== b"Gcast":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user",buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with client.conversation(e.chat_id) as xmr:
                await xmr.send_message("Send PhoneNumber")
                try:
                    Zip= await xmr.get_response(timeout=300)
                    try:
                        if Zip.text=="/start" or Zip.text=="/help":
                            return
                        pphone=phone = (telethon.utils.parse_phone(Zip.text))
                        cl=telethon.TelegramClient(None, API_ID, API_HASH)
                        await cl.connect()
                        await cl.send_code_request(phone)
                        await xmr.send_message((f"Please enter OTP of Phone No {pphone} in `1 2 3 4 5` format. __(Space between each numbers!)__"))
                        otp= await xmr.get_response(timeout=300)
                        if otp.text=="/start" or otp.text=="/help":
                            return
                        await cl.sign_in(phone=phone, code=' '.join(str(otp.text)))
                    except FloodWaitError as h:
                            await xmr.send_message(f"{pphone}You Have Floodwait of {h.x} Seconds")
                            return
                    except PhoneNumberInvalidError:
                            await xmr.send_message(f"Your Phone Number {pphone} is Invalid.")
                            return
                    except PhoneNumberBannedError:
                            await xmr.send_message(f"{phone} is Baned")
                            return
                    except TimeoutError:
                            await xmr.send_message("Time Limit Reached of 5 Min.")
                            return
                    except PhoneCodeInvalidError:
                            await xmr.send_message(f"{pphone} Invalid Code.")
                            return
                    except PhoneCodeExpiredError:
                            await xmr.send_message(f"{pphone} Code is Expired.")
                            return
                    except SessionPasswordNeededError:
                            try:
                                await xmr.send_message("Your Account Have Two-Step Verification.\nPlease Enter Your Password.")
                                two_step_code= await xmr.get_response(timeout=300)
                                if two_step_code.text=="/start" or two_step_code.text=="/help":
                                    return
                            except TimeoutError:
                                await xmr.send_message("`Time Limit Reached of 5 Min.`")
                                return
                            try:
                                await cl.sign_in(password=two_step_code.text)
                            except Exception as h:
                                await xmr.send_message(f"{pphone}\n\n**ERROR:** `{str(h)}`")
                                return
                    k = await cl.get_me()
                    red=telethon.utils.get_peer_id(k)
                    acc.append(red)
                    await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                    await cl.send_message('SpamBot', '/start')
                    await asyncio.sleep(2)
                    async for xr in cl.iter_messages("@SpamBot", limit=1):
                        stats=str(xr.text)
                    mess=await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{pphone}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**")
                except TimeoutError:
                    await xmr.send_message("Time Limit Reached of 5 Min.")
                    return
        async with client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Your Ads Message")
            try:
                message= await x.get_response(timeout=600)
                if message.text=="/start" or message.text=="/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            await x.send_message(f"Send Send Your Ads Image Or No in case you Not wants to set image")
            try:
                image= await x.get_response(timeout=600)
                if image.text=="/start" or image.text=="/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            if image.photo or image.video or image.gif:
                getit = await image.download_media(f'{e.query.user_id}/')
                try:
                    variable = upload_file(getit)
                    os.remove(getit)
                    nn = "https://telegra.ph" + variable[0]
                except Exception as e:
                    nn="https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg"
            else:
                nn="https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg"
            num = len(STUFF) + 1
            STUFF.update({num: {"msg": message.text, "media": nn}})
            await x.send_message("Message Sending Start",buttons=[[telethon.Button.inline("🛰 Stop", b"Stop")]])
            rar[f'{e.query.user_id}'] = False
            while True:
                done=0
                er=0
                async for xr in cl.iter_dialogs():
                    if rar[f'{e.query.user_id}']==True:
                        rar[f'{e.query.user_id}'] = False
                        return
                    if xr.is_group:
                        try:
                            res = await cl.inline_query('@inducedpromotionbot', f"ish{num}")
                            await res[0].click(xr.entity.id ,
                                    hide_via=True,
                                    silent=False,
                                    )
                            done+=1
                            await asyncio.sleep(1)
                            
                        except Exception as h:
                            await asyncio.sleep(1)
                            er+=1
                await x.send_message(f"Done in {done} chats, error in {er} chat(s)")
                await asyncio.sleep(600)
            
    elif e.data == b"Stop":
        await e.answer('\nPromotion Stop',alert=True)
        rar[f'{e.query.user_id}'] = True

    elif e.data == b"Home":
        await e.answer('\nWelcome Back to Home',)
        but=[
            [
                telethon.Button.inline("Gcast", b"Gcast"),
                telethon.Button.inline("Ucast", b"Ucast"),
            ],

            [
                telethon.Button.inline("🤑 BuyNow", b"Ishan"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id,f"**Welcome Sir!\n\nI'm Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)
    

    elif e.data == b"Admin":
        if e.query.user_id in OWNERS:
            but=[
                    [
                        telethon.Button.inline("Sudo", b"Sudo"),
                        telethon.Button.inline("📊 Staus", b"Stat"),
                    ],
                    [
                        telethon.Button.inline("🔄 Restart", b"Restart"),
                        telethon.Button.inline("Back", b"Home")
                    ]
                ]
            await client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)
    
    elif e.data == b"Stat":
            start = time.time()
            await e.answer('\nWait Checking Stats', alert=True)
            end = round((time.time() - start) * 1000)
            def time_formatter():
                minutes, seconds = divmod(int(time.time() - start_time), 60)
                hours, minutes = divmod(minutes, 60)
                days, hours = divmod(hours, 24)
                weeks, days = divmod(days, 7)
                tmp = (
                    ((str(weeks) + "w:") if weeks else "")
                    + ((str(days) + "d:") if days else "")
                    + ((str(hours) + "h:") if hours else "")
                    + ((str(minutes) + "m:") if minutes else "")
                    + ((str(seconds) + "s") if seconds else "")
                )
                if tmp != "":
                    if tmp.endswith(":"):
                        return tmp[:-1]
                    else:
                        return tmp
                else:
                    return "0 s"
            total, used, free = shutil.disk_usage(".")
            cpuUsage = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage("/").percent
            upload = humanbytes(psutil.net_io_counters().bytes_sent)
            down = humanbytes(psutil.net_io_counters().bytes_recv)
            TOTAL = humanbytes(total)
            USED = humanbytes(used)
            FREE = humanbytes(free)
            tex=f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
            await client.send_message(e.chat.id,tex,buttons=[[telethon.Button.inline("📊 Staus", b"Stat"),]])

    elif e.data == b"Restart":
        if not await get_user_join(e):
            return
        if e.query.user_id in OWNERS:
            await e.answer('\nRestarting Bot Wait', alert=True)
            os.execl(sys.executable, sys.executable, "-m", "main")

    elif e.data == b"Sudo":
        if not await get_user_join(e):
            return
        async with client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Userid of To Give Sudo")
            try:
                id= await x.get_response(timeout=600)
                if id.text=="/start" or id.text=="/help":
                    return
                
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            Premium.append(int(id.text))
            await x.send_message(f"Sudo Given To `{id.text}`")
            await client.send_message(int(id.text),f"Sudo Given To `{id.text}`")


def humanbytes(size):

    if size in [None, ""]:
        return "0 B"
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"

@client.on(telethon.events.InlineQuery)
async def inline_alive(o):
    if o.original_update.user_id in acc :
        return
    """
    ishan=[
        await o.builder.article(
                text="• **Induced Promotion Bot \nSubscribtion Cost: 200Rs per Month •**",
                buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]],
                title="Induced Promotion Bot",
                description="Use Our To Promote your self For Selling\nAuto Post Sender In Multiple groups",
                thumb=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
                content=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
        )
    ]
    """
    ishan=[
        await o.builder.photo(
                "https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg",
                text="**• Induced Promotion Bot •**",
                buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]],
                link_preview=False,
        )
    ]
    await o.answer(
        ishan,
        cache_time=300,
        switch_pm="👥 Induced Promotion Bot",
        switch_pm_param="start",
    )


@client.on(telethon.events.InlineQuery(pattern="ish(.*)"))
async def inline_alive(o):
    n = o.pattern_match.group(1)
    if not (n and n.isdigit()):
        return
    ok = STUFF.get(int(n))
    txt = ok.get("msg")
    pic = ok.get("media")
    """
    ishan=[
        await o.builder.article(
                text="• **Induced Promotion Bot \nSubscribtion Cost: 200Rs per Month •**",
                buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]],
                title="Induced Promotion Bot",
                description="Use Our To Promote your self For Selling\nAuto Post Sender In Multiple groups",
                thumb=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
                content=telethon.tl.types.InputWebDocument("https://telegra.ph/file/8ff763cebfe2af1a3ce45.jpg", 0, "image/jpg", []),
        )
    ]
    """
    ishan=[
        await o.builder.photo(
                pic,
                text=txt,
                buttons=[[telethon.Button.url("• Power By Induced •", url="t.me/InducedBots")]],
                link_preview=False,
        )
    ]
    await o.answer(
        ishan,
        cache_time=300,
        switch_pm="👥 Induced Promotion Bot",
        switch_pm_param="start",
    )

print("""
╔════╗
╚═╗╔═╝
╔═╣╠═╗
║╔╣╠╗║
║╚╣╠╝║
╚═╣╠═╝
╔═╝╚═╗
╚════╝""")
if len(sys.argv) not in (1, 3, 4):
    try:
        client.disconnect()
    except:
            os.execl(sys.executable, sys.executable, "-m", "main")
else:

    try:
        client.run_until_disconnected()
    except:
        os.execl(sys.executable, sys.executable, "-m", "main")
