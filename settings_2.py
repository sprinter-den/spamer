import os
import asyncio
import random


ti = open('time.txt', 'r').read()
api_id_x = 16746278
api_hash_x = "ca3a465d4b961e137addeb2e4f9b6581"  
path = f'pics/broadcast/cicada.jpg'
sessions = os.listdir('sessions')
file_list = open('ussers.txt', 'r').readlines()
uzik = len(file_list)
ssm = open('sms.txt', 'r').read()
zz = ssm.split('|')
sms = random.choice(zz)


async def photo():
    with open(path, 'rb') as f:
        photo = f.read()
        return photo