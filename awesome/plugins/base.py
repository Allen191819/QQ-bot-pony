from nonebot import on_command, CommandSession
import random
import time
__plugin_name__="今日人品"
__plugin_usage__=r"""
快来测测你的今日人品吧！
"""

@on_command('ping', only_to_me=False)
async def ping(session: CommandSession):
    await session.send("Status 200\nRuning on 127.0.0.1:8080 \n我一直在的哟！")


@on_command('jrrp', only_to_me=False, aliases=('今日人品'))
async def jrrp(session: CommandSession):
    random.seed(time.time())
    val = random.randint(0, 100)
    await session.send(message="今日人品:" + str(val), at_sender=True)
