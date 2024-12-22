from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


app = Flask(__name__)


line_bot_api = LineBotApi('zCZtbPxLyjDwzEb76JFelOORnnvtPdl6e2+FMVaDLQoT/rVBiJEHuMrI7vw54G9jVcTGIRrSs6xaFty/i5SaURvKEm1+q/Ho6DtjrzQjiJZCWH0qIWpt1atixWKibCZFZEkc6OW2zFm2eSUuYjxJRgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0dd04356805302f4be3811c38f5d035c')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # 取得請求內容
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 處理請求內容
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text
    print(f"收到的訊息內容：{message_text}")

    # 回覆訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"你說了：{message_text}")
    )

if __name__ == "__main__":
    app.run( ssl_context = ('cert.pem', 'key.pem'))
