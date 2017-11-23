#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests
import json
from random_dog import rand_dog
from bit_api import bit_usd
global last_update_id 

last_update_id = 0
token = '487463607:AAEGtNO3wFSa2c9oIWoFMu9fF9w5xlkbsxc'

def main():
    while True:
        answer = recive_messages()
        if answer != None: 
            chat_id = answer['chat_id']
            text = answer['message']
            if text == "dog":
                send_message(chat_id,rand_dog())
            elif text == "bitcoin":
                send_message(chat_id,bit_usd())
            elif text == "dolar" :
                send_message(chat_id,dollar())
            #write json 
            #with open('update.json', 'w') as file:
            #    json.dump(u, file, indent=2 , ensure_ascii=False)
        else:
            continue

def send_message(chat_id, text = 'wait a moment please ...'):
    requests.get('https://api.telegram.org/bot' + token + '/sendmessage?chat_id='+str(chat_id)+'&text='+ text)


def recive_messages():
    
    
    global last_update_id
    u = update()
    current_update_id = u["result"][-1]["update_id"]
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = u["result"][-1]["message"]["chat"]["id"]
        text    = u['result'][-1]['message']['text']
        print(u)
        current_update_id = u["result"][-1]["update_id"]
        #print(current_update_id)
        message = {'chat_id' : chat_id , 'message' : text }
        return message
    return None
def update():
    response = requests.get('https://api.telegram.org/bot' + token + '/getupdates' )
    update = response.json()
    return update

def dollar():
    url = 'http://www.o-xe.com/'
    html = requests.get(url)
    html = html.text
    html.encode('utf-8')
    dollar = re.search("<!-- Menu Part -->",html)
    start=dollar.start()+5810
    end = dollar.end()+5797
    return (html[start:end])

if __name__ == '__main__':
    main()
    