from wxpy import *
bot = Bot()
#my_friend = ensure_one(bot.search('小T'))
tuling = Tuling(api_key='b85476cd869f416ba5af3e5f30e53fb2')
# 使用图灵机器人自动与指定好友聊天
#@bot.register(my_friend)
#def reply_my_friend(msg):
#    tuling.do_reply(msg)

@bot.register(chats=None,msg_types=TEXT)
def auto_reply(msg):
    tuling.do_reply(msg)
# 堵塞线程
embed()

