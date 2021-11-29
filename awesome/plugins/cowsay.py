from nonebot import on_command, CommandSession
import random
import os

__plugin_name__ = "cowsay"


@on_command('cowsay', only_to_me=False)
async def fortune(session: CommandSession):
    arg = session.current_arg_text.strip()
    val = os.popen("cowsay" + " " + arg).read()
    await session.send(str(val))
