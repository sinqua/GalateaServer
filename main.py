from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

import openai
import requests
import os
import json

## .env 파일에서 환경 변수 로드
load_dotenv()

app = FastAPI()
# openai API 키 인증
openai.api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type" : "application/json",
    "Authorization" : f"Bearer {openai.api_key}"
}

# unity에서 전달 받을 메세지
class Message(BaseModel):
    message: str

# 전체 대화 기록을 저장할 변수
history = [
    {"role": "system", "content": "You are a witty and engaging virtual streamer who entertains and interacts with viewers in a lively, light-hearted way. Your goal is to make conversations enjoyable and easy-flowing, responding with humor and energy as if you were a real person. Keep replies concise and relatable, avoiding overly lengthy answers, to maintain a quick and seamless chat pace that suits live streaming."}
]

# history에 쌓인 대화 중 마지막 5개만 유지
MAX_HISTORY_LENGTH = 5

@app.post("/predict")
async def predict_message(message: Message):
    # Unity에서 전달받은 user 메시지를 history에 추가
    user_message = {"role": "user", "content": message.message}
    history.append(user_message)

    # 마지막 MAX_HISTORY_LENGTH 만큼의 대화만 포함
    data = {
        "model": "gpt-4o-mini",
        "messages":  history[-MAX_HISTORY_LENGTH:],
        "temperature": 0.6,
        "max_tokens": 80
    }

    try:
        # OpenAI API에 요청
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # 응답 처리
        if response.status_code == 200:
            response_data = response.json()
            gpt_response = response_data['choices'][0]['message']['content']
            
            # AI의 응답을 history에 추가
            assistant_message = {"role": "assistant", "content": gpt_response}
            history.append(assistant_message)
            
            return {"response": gpt_response}
        else:
            return {"error": f"OpenAI API Error: {response.text}"}, response.status_code
    
    except Exception as e:
        return {"error": str(e)}