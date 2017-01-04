# A Weather Bot

A django implementation of new [Line Message API](https://devdocs.line.me/en/#messaging-api) using [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
Edit from [Lee-W](https://github.com/Lee-W)
加入查詢天氣功能

## About
1. 接收到包含key word"天氣"的訊息時, 將提供地點選擇
2. 回覆地點編號可以得到天氣狀況
3. 若非以上兩種相關訊息, 將原樣訊息返回

## Setup

### Secret Data
You MUST setup the following variables.

- SECRET\_KEY
	- django secret key. You can generate using [Django secret key generator](https://gist.github.com/mattseymour/9205591)	
- LINE\_CHANNEL\_SECRET
- LINE\_CHANNEL\_ACCESS\_TOKEN

There are two way to set these variables  
1. Set these variables in `line_echobot/line_echobot/settings_secret.py`(Exactly the same name)  
2. Add these variables to environment variables. (`settings_secret.py` is loaded first)

### HTTPS Server
You'll need a https server.  
[Heroku](https://www.heroku.com) can serve this for you.  
All the needed settings for heroku are set in this repo.

Otherwise, you can also build your own https server.

### Set Webhook URL
Set webhook url on your `LINE Developers` page to `https://"your domain name"/echobot/callback/`

## Authors
Rose Liu(https://github.com/MYNAMEISROSELIU)

