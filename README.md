# WebProgramming-kakaotalk
A simple KakaoTalk as a final project for the Web Programming course.


## 📌 주요 기능 (Features)
- Login
- Friend List(친구목록)
- 1 to 1 Chatting(1대1채팅)
- Chat List(채팅목록)
- Group Chatting
- Response for individual message
- Sending and Viewing Photo in Chatting room


## 🛠 사용 기술 (Tech Stack)
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Backend**: Python 3, FastAPI
- **Database**: SQLite3
- **Server**: Uvicorn


## 🚀 설치 방법 (Installation)

1. 저장소 클론  
   ```bash
   git clone https://github.com/jinhee0/WebProgramming-kakaotalk.git
   cd WebProgramming-kakaotalk
   ```

2. 필요한 Python 패키지 설치  
   ```bash
   pip install fastapi uvicorn
   ```

3. 서버 실행  
   ```bash
   uvicorn main:app --reload
   ```

4. 아래 주소로 접속  
   ```
   http://127.0.0.1:8000
   ```

## 📂 프로젝트 구조 (예시)

```
WebProgramming-kakaotalk/
├── static/
│   └── image/                 # 채팅 UI에 사용되는 이미지 파일들
│       ├── addfriend.png
│       ├── chat.png
│       ├── emptychat.png
│       ├── emptyfriend.png
│       ├── friend.png
│       ├── profile.jpeg
│       ├── response.png
│       └── talk.png
├── templates/                 # HTML 템플릿 파일 (Jinja2 등 렌더링용)
│   ├── chatList.html
│   ├── friendList.html
│   ├── index.html
│   ├── login.html
│   └── makeGroup.html
├── crud.py                    # DB 관련 CRUD 함수 정의
├── database.py                # DB 연결 및 초기화
├── main.py                    # FastAPI 서버 엔트리 포인트
├── models.py                  # Pydantic & SQLAlchemy 모델 정의
├── schema.py                  # 데이터 요청/응답용 Pydantic 스키마
├── sql_app.db                 # SQLite3 데이터베이스 파일
└── README.md                
```


## 🖼️ 실행 화면

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/164b9824-fdc7-4522-8922-30c8bf07db3c" width="300"/></td>
    <td><img src="https://github.com/user-attachments/assets/73e9b0a2-0eae-4e11-8f53-5f578ff84030" width="300"/></td>
  </tr>
</table>


   
