from nonebot import on_command, CommandSession, permission as perm
import os

@on_command('getip', only_to_me=True, permission=perm.SUPERUSER)
async def getip(session: CommandSession):
    val = os.popen("ip addr").read()
    await session.send(str(val))
