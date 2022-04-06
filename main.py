import telethon
import os
import asyncio
import sys
import shutil
import time
import psutil
import firebase_admin
import logging
import datetime
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, FloodWaitError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, SessionPasswordNeededError
from telegraph import upload_file
from firebase_admin import credentials, db
from datetime import datetime, date

default_app = firebase_admin.initialize_app(
    credentials.Certificate(
        {
            "type": "service_account",
            "project_id": "about-ishan",
            "private_key_id": "f3ad57b9e6ad0bc574274530d4ba30353c748124",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDAJXWrsSiFf8Uy\nn5xS2OiOeQnCG+4XpUas+yMnHfVBT4H2sZaCFqMDXfT+bFdKB+lGZ6DvSmJgP2aj\nAoiFsqUW6Aku+i0LKTTYM8iT0P6z+7j/Ey2QKhfv3FaONjl0eRcVdONsUrU96uvP\nRUv1a4TOXNjINRUc8LWGp3Wy7390+T74u5KKnGnv/SnJrUN+o6nn2sDzAL6PCmtZ\nYHkznTuDKvTFSQ868pS3pAcsZICqqBLykBqDq2sMZ7osW7MLcucY3zWykjSxVP5s\n/ZMAB1cR/v32o0wOLz/yGjRYwJQv44oAvDF42HO+g/TfhBqcZUPOteOL0B9+B/PE\nexgtu0GJAgMBAAECggEACjezuy6PhhHWTavZJzqrmy/qiezsS0uZp4cvRlw8d32f\n3ptw8nf7sSkk5wah2aj0Ca9nCnJ9KrsUXSS8V8e5Ka+rFVluXcKSMdEHIH0jnjSL\nkNzXNmxWm4WvAJ73jS8HQDfYBCGdy64bXglEUcem50ZerL7N4Z0XOhLbmmlL8M9c\nktgoU+IKAWBK94P2Jo2J7rZbQ2cmwIgF94M+v9o3CD/y9rgAnfa61W2ixf+IuIcw\nWOv9kaQLQZzILiugkdeK+EAkasAz7nDArv06WtO+JNoo11ITCdHyF4ktJj4yRsjT\nx8dr+LA5Ye2ErLE4DxXKYznffRgq3uERm7g7GMNfxQKBgQDxVNnKaG9onEWugayy\nR7EfyLkY0OqmvM18/bVJo0PJugD2oTwnFNhBcgN30GkiYgp29GHaFtDuHwUeDRme\n1K1+nRYN/jlj7dnEAXvayM+JOX7tu932U46Z2lmB2xabQo+Hq1K2/6m7ilYZR0zv\naVsKFsV812+1e2HYS3XZdtLxLwKBgQDL00grTGMUBzmyY3sLtEn98id2MxkX6wJ+\n4id0+WWAAKA+cNDw0b95F1B578GT5zeoxDKfgauhKssCKIcl9MxA56/WLKAE8ds6\ncFyGVXmyn2a+Ny14s97fuMCSzMCh9F9agwOvNThDirg1Mo7ScK6WycUn08Svt9+W\nwBDdYi0axwKBgF+Ak5t9DrGYPh8b5Aq9QkPwvActDd8kEjGneSmF+ZqICD+ReOuC\nXT4w71xn1mMr5zZB6cNTiiThk7Xbu0rWoT3czlCFTZLVGnttluTy2OZWIXvU/7au\nRF1wQkGYQO76PTCUROx0amf0C7R/Odv4lnV8o3SPEP8Br6vX2PBRDJMzAoGBAI0R\n8548JUrkYVONNMl6A8gmRJezcAe02SpWfnagclawmDf/Py2eDkbSExoCDdm/Ky+8\nc0kgp1hJ1O3ufPORRZkaggHbKvmhJ1mAERnMqQku+B5o9CjZXUU8itRPsHenOiPc\nD73BOOrOZQY0stMFuGCWz8Tr9fKkcbTVxBZlb9BbAoGBAM9q2D4wNwvp3NL33IvF\nVtmpO+29wpzFNHOJooQC7OdHt0ITuv1SY6FZQKfRNk5UURK6sbb+HewYdsgCiyW1\ndkDd/rlpzv4K0ou+sClt46aBkBW340KWtXBIOa0KZyMtKy8nokNUMg1Sw+wPjDd0\ndxd9N1muHK6h3wxBNNQYRFHE\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-dfpb9@about-ishan.iam.gserviceaccount.com",
            "client_id": "112851093465815915774",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dfpb9%40about-ishan.iam.gserviceaccount.com"
        }
    ),
    {
        'databaseURL': "https://about-ishan-default-rtdb.asia-southeast1.firebasedatabase.app/"
    }
)
API_ID = 18716656
API_HASH = "9e9cc830e0b2abb3b305a27e3fe295a5"
BOT_TOKEN = "5180127494:AAH876Hx-5WP9IqPNtFO4EvkozVmO-BjMY8"
OWNERS = [1303790979, 1854668908]
Premium = [1303790979, 1854668908]
Sub = (db.reference(f"/Admin/Premium/")).get()
if Sub == None:
    Sub = []
channel = "InducedBots"
for row in Sub:
    row = str(row).split()
    d = datetime.today() - datetime.strptime(f"{row[1]}", '%Y-%m-%d')
    r = datetime.strptime("2021-12-01", '%Y-%m-%d') - \
        datetime.strptime("2021-11-03", '%Y-%m-%d')
    if d <= r:
        Premium.append(int(row[0]))
start_time = time.time()
rar = {}

logging.basicConfig(
    level=logging.WARNING,
    handlers=[logging.FileHandler('log.txt')],
    format="\n\n%(asctime)s:    %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("telethon").setLevel(logging.WARNING)
start_time = time.time()
STUFF = {}
rar = {}
client = telethon.TelegramClient(
    None, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)
acc = []


async def get_user_join(e):
    try:
        await client(telethon.tl.functions.channels.GetParticipantRequest(channel="InducedBots", participant=e.chat.id))
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        await client.send_message(e.chat.id, "You have not Joined Our Channel\nJoin to Use me For Free\n\nMade with ❤️ By @InducedBots", buttons=[[telethon.Button.url("🎁 Channel1", url=f"https://t.me/InducedBots"), telethon.Button.inline("Check☑️", b"Home"), ]])
        return False


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    if not await get_user_join(e):
        return
    but = [
        [
            telethon.Button.inline("Gcast", b"Gcast"),
            telethon.Button.inline("Ucast", b"Ucast"),
            telethon.Button.inline("Gadd", b"Gadd"),
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
        await e.client.send_message(e.chat.id, "250Rs Per Month Cost\n📑 Payment Options\n\n🔸 Paytm\n\n🔸 UPI\n\n🔸 Crypto Currency\n\nNote: Don't forget to send payment screenshot to @InducedSupportBot for plan activation.", buttons=[[telethon.Button.url("Paytm", url=f"https://paytm.me/pxvn-Tr"), telethon.Button.url("UPI", url="https://induced-service-bot.web.app"), telethon.Button.url("Crypto", url=f"https://t.me/InducedSupportBot"), ], [telethon.Button.url(": Tutorial Here :", url=f"https://youtu.be/iyz5ky3Mkkc")]])

    elif e.data == b"Gcast":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user", buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send PhoneNumber")
            try:
                Zip = await xmr.get_response(timeout=300)
                try:
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    pphone = phone = (telethon.utils.parse_phone(Zip.text))
                    cl = telethon.TelegramClient(None, API_ID, API_HASH)
                    await cl.connect()
                    await cl.send_code_request(phone)
                    await xmr.send_message((f"Please enter OTP of Phone No {pphone} in `1 2 3 4 5` format. __(Space between each numbers!)__"))
                    otp = await xmr.get_response(timeout=300)
                    if otp.text == "/start" or otp.text == "/help":
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
                        two_step_code = await xmr.get_response(timeout=300)
                        if two_step_code.text == "/start" or two_step_code.text == "/help":
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
                red = telethon.utils.get_peer_id(k)
                acc.append(red)
                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                await cl.send_message('SpamBot', '/start')
                await asyncio.sleep(2)
                async for xr in cl.iter_messages("@SpamBot", limit=1):
                    stats = str(xr.text)
                mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{pphone}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**")
            except TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return
        async with client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Your Ads Message")
            try:
                message = await x.get_response(timeout=600)
                if message.text == "/start" or message.text == "/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            await x.send_message(f"Send Send Your Ads Image Or No in case you Not wants to set image")
            try:
                image = await x.get_response(timeout=600)
                if image.text == "/start" or image.text == "/help":
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
                    nn = "https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg"
            else:
                nn = "https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg"
            num = len(STUFF) + 1
            STUFF.update({num: {"msg": message.text, "media": nn}})
            await x.send_message("Message Sending Start", buttons=[[telethon.Button.inline("🛰 Stop", b"Stop")]])
            rar[f'{e.query.user_id}'] = False
            while True:
                done = 0
                er = 0
                async for xr in cl.iter_dialogs():
                    if rar[f'{e.query.user_id}'] == True:
                        rar[f'{e.query.user_id}'] = False
                        return
                    if xr.is_group:
                        try:
                            res = await cl.inline_query('@inducedpromotionbot', f"ish{num}")
                            await res[0].click(xr.entity.id,
                                               hide_via=True,
                                               silent=False,
                                               )
                            done += 1
                            await asyncio.sleep(1)

                        except Exception as h:
                            await asyncio.sleep(1)
                            er += 1
                await x.send_message(f"Done in {done} chats, error in {er} chat(s)")
                await asyncio.sleep(500)

    elif e.data == b"Gcast":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user", buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send PhoneNumber")
            try:
                Zip = await xmr.get_response(timeout=300)
                try:
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    pphone = phone = (telethon.utils.parse_phone(Zip.text))
                    cl = telethon.TelegramClient(None, API_ID, API_HASH)
                    await cl.connect()
                    await cl.send_code_request(phone)
                    await xmr.send_message((f"Please enter OTP of Phone No {pphone} in `1 2 3 4 5` format. __(Space between each numbers!)__"))
                    otp = await xmr.get_response(timeout=300)
                    if otp.text == "/start" or otp.text == "/help":
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
                        two_step_code = await xmr.get_response(timeout=300)
                        if two_step_code.text == "/start" or two_step_code.text == "/help":
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
                red = telethon.utils.get_peer_id(k)
                acc.append(red)
                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                await cl.send_message('SpamBot', '/start')
                await asyncio.sleep(2)
                async for xr in cl.iter_messages("@SpamBot", limit=1):
                    stats = str(xr.text)
                await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{pphone}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**")
            except TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return
        async with client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Username of Account to Add members")
            try:
                message = await x.get_response(timeout=600)
                if message.text == "/start" or message.text == "/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            user = await cl.get_entity(message.text)
            xx = await x.send_message(f"Adding... {user.first_name}()tg://user?id={user.id}")
            async for xr in cl.iter_dialogs():
                if xr.is_group:
                    try:
                        await cl(telethon.functions.channels.InviteToChannelRequest(xr, users=[user]))
                        done += 1
                        await asyncio.sleep(1)

                    except Exception as h:
                        await asyncio.sleep(1)
                        er += 1
            await xx.edit(f"#GADDED {user.first_name}()tg://user?id={user.id})\nDone: {done}chats\nError: {er}chats")

    elif e.data == b"Stop":
        await e.answer('\nPromotion Stop', alert=True)
        rar[f'{e.query.user_id}'] = True

    elif e.data == b"Home":
        await e.answer('\nWelcome Back to Home',)
        but = [
            [
                telethon.Button.inline("Gcast", b"Gcast"),
                telethon.Button.inline("Ucast", b"Ucast"),
                telethon.Button.inline("Gadd", b"Gadd"),
            ],

            [
                telethon.Button.inline("🤑 BuyNow", b"Ishan"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)

    elif e.data == b"Admin":
        if e.query.user_id in OWNERS:
            but = [
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

        def humanbytes(size):

            if size in [None, ""]:
                return "0 B"
            for unit in ["B", "KB", "MB", "GB"]:
                if size < 1024:
                    break
                size /= 1024
            return f"{size:.2f} {unit}"

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
        tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
        await client.send_message(e.chat.id, tex, buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])

    elif e.data == b"Restart":
        if not await get_user_join(e):
            return
        if e.query.user_id in OWNERS:
            await e.answer('\nRestarting Bot Wait', alert=True)
            os.execl(sys.executable, sys.executable, "-m", "main")

    elif e.data == b"Sudo":
        async with e.client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Userid of To Give Sudo")
            try:
                id = await x.get_response(timeout=600)
                if id.text == "/start" or id.text == "/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            re = date.today()
            suib = re+(datetime.strptime("2021-12-01", '%Y-%m-%d') -
                       datetime.strptime("2021-11-03", '%Y-%m-%d'))
            Premium.append(int(id.text))
            Sub.append(f"{id.text} {re}")
            ref = (db.reference(f"/Admin/Premium/")).set(Sub)
            await x.send_message(f"Sudo Given To `{id.text}`")
            await e.client.send_message(int(id.text), f"Congratulation Your Subscription Has been Sucessfully started.\nYou are now Premium till {suib}\n\nMade With ❤️ By @{channel}")


@client.on(telethon.events.InlineQuery)
async def inline_alive(o):
    if o.original_update.user_id in acc:
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
    ishan = [
        await o.builder.photo(
            "https://telegra.ph/file/94a7f2073cdcf4c002a09.jpg",
            text="**• Induced Promotion Bot •**",
            buttons=[[telethon.Button.url(
                "• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]],
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
    ishan = [
        await o.builder.photo(
            pic,
            text=txt,
            buttons=[[telethon.Button.url(
                "• Power By Induced •", url="t.me/InducedBots")]],
            link_preview=False,
        )
    ]
    await o.answer(
        ishan,
        cache_time=300,
        switch_pm="👥 Induced Promotion Bot",
        switch_pm_param="start",
    )


@client.on(telethon.events.NewMessage(incoming=True, pattern='/logs', func=lambda e: e.is_private))
async def logAddee(e):
    if e.chat.id in OWNERS:
        await client.send_file(e.chat_id, "log.txt", caption="Your Logs Here", force_document=True)

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
