from wxpy import *
#Key：TLAFnsDZyN7j
#Secret：A7xCsp2KZ02VfDpuMVIq

bot = Bot()
my_friend = ensure_one(bot.search('雅典'))
xiaoi = XiaoI('TLAFnsDZyN7j', 'A7xCsp2KZ02VfDpuMVIq')

# 使用小 i 机器人自动与指定好友聊天
@bot.register(chats=None,msg_types=TEXT)
def auto_reply(msg):
    xiaoi.do_reply(msg)
# 堵塞线程
embed()