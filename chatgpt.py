import os
import sys
import time
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.environ.get('TWILIO_PHONE_NUMBER')

systemPrompt = { "role": "system", "content": "You are a helpful assistant." }

openai.api_key = os.getenv("OPENAI_API_KEY")

data = []

def get_chatgpt_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:
        data.append({"role": "assistant", "content": incoming_msg})
    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""
