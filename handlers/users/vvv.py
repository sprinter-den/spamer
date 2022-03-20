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

api_id = 16746278
api_hash = "ca3a465d4b961e137addeb2e4f9b6581" 

file_list = os.listdir('sessions')
acaunt = file_list[2]
cli = open(f"sessions/{acaunt}").read()
client = TelegramClient(StringSession(cli), api_id, api_hash)
client.connect()
client.send_message('satanasat', 'fffff')
