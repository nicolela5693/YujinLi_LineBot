from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from io import StringIO
from pyquery import PyQuery as pq


import requests
import random
import json
import math
import time
import datetime
import os
import apiai

#---------------- self define module ----------------
import text_push as text_push
import text_reply as text_reply


#---------------- line settings ----------------
# Channel Access Token
LINE_CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# Channel Secret
LINE_CHANNEL_SECRET = os.environ.get('LINE_CHANNEL_SECRET')
handler = WebhookHandler(LINE_CHANNEL_SECRET)
# DIALOGFLOW_CLIENT_ACCESS_TOKEN
DIALOGFLOW_CLIENT_ACCESS_TOKEN = os.environ.get('DIALOGFLOW_CLIENT_ACCESS_TOKEN')
ai = apiai.ApiAI(DIALOGFLOW_CLIENT_ACCESS_TOKEN)


#---------------------------------------------------

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
def news():
    res = requests.get('https://m.ctee.com.tw/livenews')
    res.encoding = 'utf-8'
    doc = pq(res.text)
    doc.make_links_absolute(base_url=res.url)
    count = 0
    content = ''
    for eachItem in doc('.item-content .title').items():
        if count < 5:
            title = eachItem('a').text()
            url = eachItem('a').attr('href')
            count += 1
        else:
            break
        content += '{}\n{}\n\n'.format(title, url)
    return content

def find_weather():
    res = requests.get('https://weather.com/zh-TW/weather/today/l/TWXX0021:1:TW')
    res.encoding = 'utf-8'
    doc = pq(res.text)
    content = ''
    temper = doc('.today_nowcard-temp').text()
    weather = doc('.today_nowcard-phrase').text()
    soma_temper = doc('.deg-feels').text()
    content = '地點: 台灣, 台北\n現在氣溫: {}\n天氣: {}\n體感溫度: {}'.format(temper, weather, soma_temper)
    return content



@handler.add(MessageEvent)
def handle_message(event):
    print(event)
    message_send_time = float(event.timestamp)/1000
    message_get_time = float(time.time())
    msg_type = event.message.type

    if event.message.text == "info":
        output_message = TextSendMessage(text=str(event))  
        line_bot_api.reply_message(event.reply_token, output_message)

    if event.message.text.lower() == "speed" :
        output_message = ("【收到訊息時間】\n{} 秒\n【處理訊息時間】\n{} 秒".format(message_get_time-message_send_time,float(time.time())-message_get_time))
        output_message = text_reply.text_reply_message(user_message)
        line_bot_api.reply_message(event.reply_token, output_message)

    if msg_type == "text":
        if event.message.text == "更多選項":
            buttons_template = TemplateSendMessage(
                alt_text='更多選項 Template',
                template=ButtonsTemplate(
                    title='選單',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='關於我',
                            text='關於我'
                        ),
                        MessageTemplateAction(
                            label='經歷',
                            text='經歷'
                        ),
                        MessageTemplateAction(
                            label='作品集',
                            text='作品集'
                        ),
                        MessageTemplateAction(
                            label='其他功能',
                            text='其他功能'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "關於我":
            buttons_template = TemplateSendMessage(
                alt_text='關於我 Template',
                template=ButtonsTemplate(
                    title='關於我',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='個性',
                            text='個性'
                        ),
                        MessageTemplateAction(
                            label='核心技能',
                            text='核心技能'
                        ),
                        MessageTemplateAction(
                            label='競爭優勢',
                            text='競爭優勢'
                        ),
                        MessageTemplateAction(
                            label='職涯目標',
                            text='職涯目標'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "經歷":
            buttons_template = TemplateSendMessage(
                alt_text='經歷 Template',
                template=ButtonsTemplate(
                    title='經歷',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='求學經歷',
                            text='求學經歷'
                        ),
                        MessageTemplateAction(
                            label='工作經驗',
                            text='工作經驗'
                        ),
                        MessageTemplateAction(
                            label='社團經歷',
                            text='社團經歷'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "作品集":
            buttons_template = TemplateSendMessage(
                alt_text='作品集 Template',
                template=ButtonsTemplate(
                    title='作品介紹',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='實習職缺爬蟲整合工具',
                            text='實習職缺爬蟲整合工具'
                        ),
                        MessageTemplateAction(
                            label='狗狗主題搜尋引擎網站',
                            text='狗狗主題搜尋引擎網站'
                        ),
                        MessageTemplateAction(
                            label='麵包店產銷系統',
                            text='麵包店產銷系統'
                        ),
                        URIAction(
                            label='Github連結',
                            uri='https://github.com/nicolela5693'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "其他功能":
            buttons_template = TemplateSendMessage(
                alt_text='其他功能 Template',
                template=ButtonsTemplate(
                    title='其他功能',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='今日天氣',
                            text='今日天氣'
                        ),
                        MessageTemplateAction(
                            label='即時新聞',
                            text='即時新聞'
                        ),
                        URIAction(
                            label='分享Bot',
                            uri='https://line.me/R/nv/recommendOA/@657jmdbc'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "聯絡我":
            buttons_template = TemplateSendMessage(
                alt_text='聯絡我 Template',
                template=ButtonsTemplate(
                    title='聯絡資訊',
                    text='請選擇',
                    thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                    actions=[
                        MessageTemplateAction(
                            label='Email',
                            text='Email'
                        ),
                        URIAction(
                            label='LinkedIn',
                            uri='https://www.linkedin.com/in/yujin-lee-taiwan/'
                        ),
                        URIAction(
                            label='Github',
                            uri='https://github.com/nicolela5693'
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template)
            return 0
        elif event.message.text == "即時新聞":
            content = news()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=content))
            return 0
        elif event.message.text == "今日天氣":
            content = find_weather()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=content))
            return 0
        else:
            user_message = event.message.text 
            output_message = text_reply.text_reply_message(user_message)
            line_bot_api.reply_message(event.reply_token, output_message)




@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    print("package_id:", event.message.package_id)
    print("sticker_id:", event.message.sticker_id)
    sticker_ids = [52002734, 52002735, 52002736, 52002738, 52002744, 52002745, 52002752, 52002768]
    index_id = random.randint(0, len(sticker_ids) - 1)
    sticker_id = str(sticker_ids[index_id])
    print(index_id)
    sticker_message = StickerSendMessage(
        package_id = '11537',
        sticker_id=sticker_id
    )
    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)

    
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
