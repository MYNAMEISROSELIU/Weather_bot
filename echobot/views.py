from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from urllib.request import urlopen
from bs4 import BeautifulSoup

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
weather_key = settings.WEATHER_ADMIN_KEY


@csrf_exempt
def callback(request):
	if request.method == 'POST':
		signature = request.META['HTTP_X_LINE_SIGNATURE']
		body = request.body.decode('utf-8')

		try:
			events = parser.parse(body, signature)
		except InvalidSignatureError:
			return HttpResponseForbidden()
		except LineBotApiError:
			return HttpResponseBadRequest()

		for event in events:
			if isinstance(event, MessageEvent):
				if isinstance(event.message, TextMessage):
					#print(event.message.text)
					if '天氣' in event.message.text:
						line_bot_api.reply_message(event.reply_token,TextSendMessage('請選擇所在縣市(請直接以編號答覆)：\n' + '0.台北市 1.新北市 2.桃園市 3.台中市 4.台南市 5.高雄市 6.基隆市 7.新竹縣 8.新竹市 9.苗栗縣 10.彰化縣 11.南投縣 12.雲林縣 13.嘉義縣 14.嘉義市 15.屏東縣 16.宜蘭縣 17.花蓮縣 18.台東縣 19.澎湖縣 20.金門縣 21.連江縣'))
					elif(event.message.text == '0'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日台北市天氣' + Weather(0)))
					elif(event.message.text == '1'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日新北市天氣' + Weather(1)))
					elif(event.message.text == '2'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日桃園市天氣' + Weather(2)))
					elif(event.message.text == '3'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日台中市天氣' + Weather(3)))
					elif(event.message.text == '4'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日台南市天氣' + Weather(4)))
					elif(event.message.text == '5'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日高雄市天氣' + Weather(5)))
					elif(event.message.text == '6'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日基隆市天氣' + Weather(6)))
					elif(event.message.text == '7'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日新竹縣天氣' + Weather(7)))
					elif(event.message.text == '8'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日新竹市天氣' + Weather(8)))
					elif(event.message.text == '9'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日苗栗縣天氣' + Weather(9)))
					elif(event.message.text == '10'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日彰化縣天氣' + Weather(10)))
					elif(event.message.text == '11'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日南投縣天氣' + Weather(11)))
					elif(event.message.text == '12'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日雲林縣天氣' + Weather(12)))
					elif(event.message.text == '13'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日嘉義縣天氣' + Weather(13)))
					elif(event.message.text == '14'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日嘉義市天氣' + Weather(14)))
					elif(event.message.text == '15'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日屏東縣天氣' + Weather(15)))
					elif(event.message.text == '16'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日宜蘭縣天氣' + Weather(16)))
					elif(event.message.text == '17'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日花蓮縣天氣' + Weather(17)))
					elif(event.message.text == '18'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日台東縣天氣' + Weather(18)))
					elif(event.message.text == '19'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日澎湖縣天氣' + Weather(19)))
					elif(event.message.text == '20'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日金門縣天氣' + Weather(20)))
					elif(event.message.text == '21'):
						line_bot_api.reply_message(event.reply_token,TextSendMessage('今日連江縣天氣' + Weather(21)))

					else:
						line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
					
		return HttpResponse()
	else:
		return HttpResponseBadRequest()


#TO GET THE WEATHER DATA
def Weather(x):
	web = "http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=" + weather_key
	page = urlopen(web)
	soup = BeautifulSoup(page,'lxml')
	
	#ans = str(soup.find_all('location')[x].time.parameter.parametername.contents)
	#ans = ans.lstrip("[\'").rstrip("\']")
	s1 = str(soup.find_all('location')[x].find_all('time')[0].parameter.parametername.contents).lstrip("[\'").rstrip("\']")
	s2 = str(soup.find_all('location')[x].find_all('time')[1].parameter.parametername.contents).lstrip("[\'").rstrip("\']")
	s3 = str(soup.find_all('location')[x].find_all('time')[2].parameter.parametername.contents).lstrip("[\'").rstrip("\']")

	s4 = str(soup.find_all('location')[x].find_all('weatherelement')[3].find_all('time')[0].parameter.parametername.contents).lstrip("[\'").rstrip("\']")
	s5 = str(soup.find_all('location')[x].find_all('weatherelement')[3].find_all('time')[1].parameter.parametername.contents).lstrip("[\'").rstrip("\']")
	s6 = str(soup.find_all('location')[x].find_all('weatherelement')[3].find_all('time')[2].parameter.parametername.contents).lstrip("[\'").rstrip("\']")

	ans = ": "+s1+ "/"+s4+"==>" +s2+"/"+ s5+"==>" +s3+"/"+s6
	
	return ans


