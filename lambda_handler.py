import json
import requests # for use this module need upload to lambda layers file requests.zip as layer requests_layer
                # and adding this layer in you lambda function

WEB_HOOK_URL = 'you API Gateway EndPoint'
TELE_TOKEN = 'TELEGRAM BOT ID'

URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    requests.get(url)

def lambda_handler(event, context):
    body_json= event['body']
    body = json.loads(body_json)
    chat_id = body['message']['chat']['id']
    message = body['message']['text']

    send_message(message, chat_id)

    return {
        'statusCode': 200
    }