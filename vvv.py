from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta
from telethon.sessions import StringSession
import os
import aiogram
from aiogram.types import CallbackQuery, Message
import random, time


pat = 'AgACAgQAAxkBAAIDk2IVgXUOASy_B4yI3Z0GiPE1a5WhAALaujEbH9SoUPlxx780PB6VAQADAgADeQADIwQ'

api_id = 16746278
api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
file_list = os.listdir('sessions')
xx = len(file_list)
ss = open('ussers.txt', 'r').readlines()
i = 2
p = 0
t = 0
while xx >= i:
    acaunt = file_list[i]
    cli = open(f"sessions/{acaunt}").read()
    client = TelegramClient(StringSession(cli), api_id, api_hash)
    client.connect()
    with open("pics/broadcast/cicada.jpg", 'rb') as ph:
        tot = ph.read()
    ssm = open('sms.txt', 'r').read()
    zz = ssm.split('|')
    sms = random.choice(zz)
    file_list2 = open('ussers.txt', 'r').readlines()
    if p >= 40:
        client.disconnect()
        i = i + 1
    if len(file_list2) >= p:
        try:
            client.send_file(file_list2[t], file=tot, caption=sms)
            p = p + 1
            t = t + 1
            client.disconnect()
        except:
            client.disconnect()
            t = t + 1
    else:
        client.disconnect()
        i = i + 1
