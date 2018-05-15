# coding: utf-8

from wxpy import *
import urllib3  
import requests
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
		"deepThought",
		storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
		database='chatbot'
	)
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("/home/tankh/chatbot/novel.yml")


tuling = Tuling(api_key='b85476cd869f416ba5af3e5f30e53fb2')

def http_response(msg):
	requests.packages.urllib3.disable_warnings()
	http = urllib3.PoolManager()
	data = {"text": msg}
	encode_data= json.dumps(data).encode()
	url = "http://124.202.155.72:60001/nlp/chatbotReply"

	r = http.request('POST',
	                     url,
	                     body=encode_data,
	                     headers={'Content-Type':'application/json'}
	                 )
	return json.loads(r.data.decode('utf-8'))['data']

# bot = Bot(cache_path = True)
bot = Bot()
group1 = ensure_one(bot.groups().search("测试邵接口"))
group2 = ensure_one(bot.groups().search("测试chatterbot"))
group3 = ensure_one(bot.groups().search("测试图灵"))

@bot.register(group1, TEXT)
def print_group1_msg(msg):
  # if msg.is_at:
  print(msg.text)
  res = http_response(msg.text)
  print(res)
  return res

@bot.register(group2, TEXT)
def print_group2_msg(msg):
  # if msg.is_at:
  print(msg.text)
  res = chatbot.get_response(msg.text).text
  print(res)
  return res


@bot.register(group3, TEXT)
def print_group3_msg(msg):
  # if msg.is_at:
  print(msg.text)
  tuling.do_reply
  res = chatbot.get_response(msg.text).text
  print(res)
  return res

bot.join()
#embed()
