from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import*
from settings import*
from testfunc import*
app = Flask(__name__)


try: 
    line_bot_api = LineBotApi(channel_access_token)
    parser = WebhookParser(channel_secret)
    handler = WebhookHandler(channel_secret)
except:
    print("Error while connecting to LineBot")
    

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    global chat_button
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    except LineBotApiError:
        abort(400) 
    
    for event in events:
        if isinstance(event, MessageEvent):
            if event.message.text == "你好":
                line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(text="想查詢甚麼呢?")
                )
            elif event.message.text == "@quick":
                quicktest(event)
            elif event.message.text == "@button":
                buttontest(event)
            elif event.message.text == "@carousel":
                carouseltest(event)    
            else:
                line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(text=event.message.text)
                )
    return 'OK'
                
#訊息傳遞區塊
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     message = TextSendMessage(text=event.message.text)
#     line_bot_api.reply_message(event.reply_token,message)

# main
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

