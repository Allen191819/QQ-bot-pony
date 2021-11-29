# QQ-bot-pony

这是一个简单的基于 `nonebot` 和 `go-cqhttp` 的 qq 机器人。

## 特性

-   Bilibili 番剧查询
-   天气查询
-   知乎日报
-   群消息自动加一
-   运行代码
-   名人民言（需要安装 fortune 到本地）
-   成语查询
-   latex 数学公式
-   智能聊天
-   讲笑话
-   点歌
-   欢迎群新成员

如果你希望在你的本地机器上运行请注意查看 `nonebot` [官方文档](https://docs.nonebot.dev/)

对于本机器人，除了[必要的 python 包](env.txt)之外
```bash
pip install -r env.txt
```

请在[腾讯云](https://cloud.tencent.com/login) 和[聚合数据](https://passport.juhe.cn/cas/login)平台获取 API 密钥，填入[config.py](config.py)， 如下：

```python
TENCENT_BOT_SECRET_ID = ''
TENCENT_BOT_SECRET_KEY = ''
JUHE_IDIOM_API_KEY = ''
JUHE_JOKE_API_KEY = ''
JUHE_WEATER_API_KEY = ''

```

另一方面在[config.yml](config.yml) 填入 bot 的 qq 号，在[config.py](config.py) 填入超级用户即可。

最后运行机器人：

```bash
./run.sh
```
