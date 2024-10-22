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

class PredictMessage(BaseModel):
    system_prompt: str
    user_message: str

# class UserCreate(BaseModel):
#     user_id: int
#     user_name: str  

# class Message(BaseModel):
#     message: str

# @app.get("/")
# #async def root():
# def root():
#     return {"message" : "Hello World"}

# @app.get("/home")
# def home():
#     return {"message" : "Home"}

@app.post("/predict")
async def predict_message(predict_message: PredictMessage):
    try:
        # prompt 및 user message 설정
        system_message = predict_message.system_prompt
        user_message = predict_message.user_message

        print(f"API Key: {openai.api_key}")
        
        # OpenAI에 보낼 데이터 설정
        data = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.7
        }

        # Post 요청
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # 응답 처리
        if response.status_code == 200:
            response_data = response.json()
            gpt_response = response_data['choices'][0]['message']['content']
            return {"response": gpt_response}
        else:
            return {"error": f"OpenAI API Error: {response.text}"}, response.status_code
    
    except Exception as e:
        return {"error": str(e)}