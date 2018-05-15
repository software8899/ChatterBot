from wxpy import *
import urllib3
import requests
import json
from chatterbot import ChatBot
bot = Bot()
my_friend = bot.friends().search('AI')[0]
boring_group = bot.groups().search('test')[0]
@bot.register()
def just_print(msg):
    res = chatbot.get_response(msg.text).text
    # 打印消息
    print(msg)

#Bot.register(chats=None, msg_types=None, except_self=True, run_async=True, enabled=True)
@bot.register(boring_group,except_self=False,run_async=True)
def ignore(msg):
    # 啥也不做
    return '收到消息: {} ({})'.format(msg.text, msg.type)

embed()

