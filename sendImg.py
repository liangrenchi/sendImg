# -*- coding: UTF-8 -*-
import schedule
import time
import itchat
import requests

bot=itchat.auto_login(hotReload=True) #表示热登录，在一定时间内不需要重新登录

url = "https://pushbear.ftqq.com/sub"
data={
  "sendkey": "你在pushbear申请到的key",
  "text": "签到图片成功发送",
  "desp": "己发送到班群中完成签到"
}

headers={
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate, br",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"}


def sendImg():
    rooms = itchat.get_chatrooms(update=True,contactOnly=True) #拿到所有的微信群
    rooms = itchat.search_chatrooms(u"指定群聊名称")
    f = "图片地址"
    if rooms is not None:
        username = rooms[0]['UserName']
        itchat.send("又到了签到的时间",toUserName=username)
        itchat.send_image(f,toUserName=username)

        #推送成功签到信息
        requests.post(url,data,headers)

    else:
        print('None group found')

#定时
schedule.every().day.at("21:10").do(sendImg)  #设定时间

while True:
    schedule.run_pending()
    time.sleep(1)







