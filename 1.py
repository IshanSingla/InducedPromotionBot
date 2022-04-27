import telethon

client = telethon.TelegramClient(None, 18716656, "9e9cc830e0b2abb3b305a27e3fe295a5").start(
    bot_token="5286961271:AAG40BkIaOL5ZjsHhUCsB-LswX02Al27UAs")


@client.on(telethon.events.NewMessage(incoming=True, pattern='/start', func=lambda e: e.is_private))
async def _(e):
    await client.send_message(
        "TeamInduced", 
        "Induced: All Linked Channels.", 
        buttons=
            [
                [
                    telethon.Button.url("Bots", url="https://t.me/TheInduced"),
                    telethon.Button.url("Updates", url="https://t.me/InducedBots"),
                    telethon.Button.url("Support", url="https://t.me/InducedBotsSupport"),
                ],
                [
                    telethon.Button.url("Developers / DevOp", url="https://t.me/InducedDevOp"),
                ],
                [
                    telethon.Button.url("Network", url="https://t.me/InducedNetwork"),
                    telethon.Button.url("Giveaway", url="https://t.me/InducedGiveaways"),
                    telethon.Button.url("Earning", url="https://t.me/InducedEarning"),

                ],
                [
                    telethon.Button.url("Spaming", url="https://t.me/InducedSpaming"),
                    telethon.Button.url("Selling", url="https://t.me/InducedSelling"),
                    telethon.Button.url("Chating", url="https://t.me/InducedChating"),

                ],
                [
                    telethon.Button.url("YouTube", url="https://www.youtube.com/c/InducedOfficial"),
                    telethon.Button.url("InstaGram", url="https://www.instagram.com/inducedofficial/"),
                    telethon.Button.url("Twitter", url="https://twitter.com/InducedOfficial/"),
                ],
            ],)

@client.on(telethon.events.NewMessage(incoming=True, pattern='/ish', func=lambda e: e.is_private))
async def _(e):
    await client.send_message(
        "https://t.me/InducedBotsSupport", 
        "Induced: Bots List", 
        buttons=
            [
                [
                    telethon.Button.url("Scraping Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYTU8lLRiVJkStZTfYyXvX7h")
                ],
                [

                    telethon.Button.url("Promotion Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYQtw6Acj2gvFEpZNvUATHKp")
                ],
                [

                    telethon.Button.url("UserBot Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYRpmiCRpAME3W_d__fDXlir")
                ],
                [

                    telethon.Button.url("Spam Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYSt_XpWn8dU39zlHSDxpIMJ")
                ],
                [

                    telethon.Button.url("Otp Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYS48IKPFNO2e3oepTpM9rC5")
                ],
                [

                    telethon.Button.url("Views Bot", url="https://youtube.com/playlist?list=PLkgZrmKoUMYQYQA-nI5M8sjxkFyzYiP1s")
                ],
                [
                    telethon.Button.url("DM To Buy Subscribtion", url="https://t.me/IshanDevOp")
                ]
            ])
print("hi")
client.run_until_disconnected()
