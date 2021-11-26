from nonebot import NoneBot

import requests


async def get_weather_of_city(bot: NoneBot, city: str) -> str:
    resp = requests.post('http://apis.juhe.cn/simpleWeather/query',
                        data={
                            'city': city,
                            'key': 'fd9103d6747f8adaf81379bb21c7d4f1'
                        })

    payload = resp.json()

    if not payload or not isinstance(payload, dict):  # 返回数据不正确
        return '抱歉，暂时无法查询哦'

    val = ''
    if payload['error_code'] == 0:
        info = payload['result']['realtime']['info']
        temp = payload['result']['realtime']['temperature']
        humidity = payload['result']['realtime']['humidity']
        windd = payload['result']['realtime']['direct']
        windp = payload['result']['realtime']['power']
        val += f"{city}今天{info},气温{temp}摄氏度,湿度{humidity}%,{windd}{windp}"
        return val
    else:
        return "抱歉，没有查询到结果"
