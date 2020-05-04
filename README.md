# 基于Telegram的IP信息查询Bot

## 运行环境

本程序在：Python 3.6.9 运行通过

安装依赖：
```
pip3 install -r requirements.txt
```

## 填入对应API

修改`config.py`中的`TOKEN`、`link114_id`以及`link114_sign`

其中
`TOKEN`为Telegram Bot的API
`link114_id`为link114的api id
`link114_sign`为link114的api key

*114link的api接口需要充值，但是很便宜*

![TOKEN](http://i0.hdslb.com/bfs/article/b01aa1539282a4c007151ea09688baa3df80bb06.png)

![link114_sign](http://i0.hdslb.com/bfs/article/bbf042e089474582f4d36791e9ef3577d9d4ab79.png)

## 运行
命令行执行
```
 python3 main.py
```

ps：可通过`screen`或`nohup`实现持续运行
 
