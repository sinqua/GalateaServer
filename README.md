# Galatea
인공지능 컴패니언의 가능성 탐구

## 개요

목적: 포스트휴먼 체험, 커리어 성장, 상업가능성 탐구

목표: 채팅을 인식하고 시청자와 소통하는 버추얼 스트리머 방송 온에어 

## 구현

형식: AI + Avatar + Live streaming

3D 렌더링: Unity

TTS: Azure

백엔드: fastAPI

대화모델: Langchain

데이터베이스: Supabase(postgresql)

라이브스트리밍: Chzzk

## 마일스톤

1. Unity에서 Python 서버로 메시지 전송 -> Python 서버에서 Unity로 ChatGPT 답변을 전달

2. Python 서버가 Unity 부터 받은 메시지와 ChatGPT 부터 받은 메시지를 데이터베이스 저장

3. 치지직 채팅을 ChatGPT로 전달하는 Python 서버

4. ChatGPT 답변을 음성으로 소리내는 VRM 아바타가 포함된 Unity 화면

5. 백엔드 서비스를 운영할 클라우드 서버 개발

## 참고자료

https://github.com/sinqua/Techno-symbiosis

2024년 여름에 제작해본 LLM 어플리케이션. Flask + Langchain + LLaMa3 + Supabase + React 

https://github.com/gunyu1019/chzzk_py

치지직 Python API (비공식)

https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/quickstart

Unity-AzureSDK 연결 튜토리얼

https://fastapi.tiangolo.com/tutorial/first-steps/

fastAPI 튜토리얼

https://github.com/sotanmochi/VRMLipSyncSample

VRM 아바타 립싱크 샘플

https://python.langchain.com/v0.2/docs/how_to/message_history/

이전의 대화를 기억하는 LLM을 만들기 위한 Langchain 가이드

Supabase 비밀번호

2lyAcfwcbB2dPQUg
