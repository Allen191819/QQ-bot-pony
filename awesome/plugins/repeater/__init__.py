# -*- coding: UTF-8 -*-
from nonebot import *
from aiocqhttp.exceptions import Error as CQHttpError
import time,os,random
import aiofiles
__plugin_name__ = "自动加一"

bot = get_bot()


async def rre(qun,msg):
    mark = 0
    msg = str(msg)
    p="/home/pi/qqbot/awesome/plugins/repeater/repeater_data/"+str(qun)+".txt"
    if msg.find(".jpg")!=-1 or msg.find(".JPG")!=-1:
        return 0
    else:
        if os.path.exists(p):
            async with aiofiles.open(p,"r",encoding = 'utf-8') as f:
                msg_old = await f.read()
                msg_old = msg_old.strip()
            if msg_old == msg:
                mark=1
                async with aiofiles.open(p, "w",encoding = 'utf-8') as f:
                    await f.write("")
        if mark==0:
            async with aiofiles.open(p,"w",encoding = 'utf-8') as f:
                    await f.write(msg)
        return mark

async def t_w():
    p = "/home/pi/qqbot/awesome/plugins/repeater/repeater_data/time.txt"
    s = time.time()
    sub = 0
    if os.path.exists(p):
        async with aiofiles.open(p,"r",encoding = 'utf-8') as f:
            read = await f.read()
            read = read.strip()
            sub = s - float(read)
            print(sub)
    else:
        async with aiofiles.open(p,"w",encoding = 'utf-8') as f:
            await f.write(str(s))
    if sub>60:
        async with aiofiles.open(p,"w",encoding = 'utf-8') as f:
            await f.write(str(s))
        return 1
    else:
        return 0

async def gjc_on(qun):
    p = "/home/pi/qqbot/awesome/plugins/repeater/repeater_data/gjc_no.txt"
    mark = 1
    if os.path.exists(p):
        async with aiofiles.open(p,"r",encoding = 'utf-8') as f:
            lines = await f.readlines()
            for line in lines:
                line = line.strip()
                if line == str(qun):
                    mark = 0
                    break
    return mark

@bot.on_message("group")
async def re(context):
    msg = context["message"]
    s_msg = str(msg)
    qun = context["group_id"]
    qq = context["user_id"]
    mark = await rre(qun,msg)
    if mark == 1:
        if await gjc_on(qun)==1:
            await bot.send_msg(group_id=qun,message=msg)

    #关键词部分
    if await gjc_on(qun):
        if os.path.exists("/home/pi/qqbot/awesome/plugins/repeater/repeater_data/gjc.txt"):
            async with aiofiles.open("/home/pi/qqbot/awesome/plugins/repeater/repeater_data/gjc.txt","r",encoding = 'utf-8') as f:
                lines = await f.readlines()
                for line in lines:
                    line = line.strip().split(" ")
                    gjc = line[0]
                    model = int(line[1])
                    time_white = int(line[2])
                    send = line[3]
                    if model == 1:
                        #jingque
                        if gjc == s_msg:
                            if time_white == 1:
                                if await t_w()==1:
                                    await bot.send_msg(group_id=qun,message=send)
                            else:
                                await bot.send_msg(group_id=qun,message=send)
                            break
                    else:
                        #mohu
                        if s_msg.find(gjc)!=-1:
                            if time_white == 1:
                                if await t_w()==1:
                                    await bot.send_msg(group_id=qun,message=send)
                            else:
                                await bot.send_msg(group_id=qun,message=send)
                            break



