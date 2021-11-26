from nonebot import on_command, CommandSession
import random
import os
__plugin_name__ = "fortune"

@on_command('fortune', only_to_me=False)
async def fortune(session: CommandSession):
    val = os.popen("fortune").read()
    await session.send(str(val))


@on_command('fortunezh', only_to_me=False, aliases=('古诗'))
async def fortunezh(session: CommandSession):
    val = os.popen("fortune-zh").read()
    await session.send(str(val))
