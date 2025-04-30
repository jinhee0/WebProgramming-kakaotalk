from fastapi import FastAPI, WebSocket, Request, Depends
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.logger import logger
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles

from typing import List

from schema import ChatRequest, ChatRequestCreate, UserInfoRequest, UserInfoRequestCreate, FriendListRequest, FriendListRequestCreate
from crud import get_chatHistory, add_chatHistory, add_userInfo, get_userInfo, get_friendList, add_friendList
from models import Base, ChatHistory
from database import SessionLocal, engine

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory ="static", html = True), name ="static")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{data}")
    except Exception as e:
        pass
    finally:
        await manager.disconnect(websocket)

# 초기 로그인 창
@app.get("/")
async def client(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# login 창에서 register 시
@app.post("/register", response_model=List[UserInfoRequest])
def post_data(userInfo_req: UserInfoRequestCreate, db: Session = Depends(get_db)):
    return add_userInfo(db, userInfo_req)

# login 창에서 register 시
@app.get("/login", response_model=List[UserInfoRequest])
def get_data(db:Session = Depends(get_db)):
    return get_userInfo(db)

#chat 창
@app.get("/index")
async def client(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/friendList")
async def client(request: Request):
    return templates.TemplateResponse("friendList.html", {"request": request})

@app.get("/makeGroup")
async def client(request: Request):
    return templates.TemplateResponse("makeGroup.html", {"request": request})

@app.get("/getfriendList", response_model=List[FriendListRequest])
def get_data(db:Session = Depends(get_db)):
    return get_friendList(db)

@app.post("/postfriendList", response_model=List[FriendListRequest])
def post_data(friend_req: FriendListRequestCreate, db: Session = Depends(get_db)):
    return add_friendList(db, friend_req)

@app.get("/chatList")
async def client(request: Request):
    return templates.TemplateResponse("chatList.html", {"request": request})

@app.get("/getChat", response_model=List[ChatRequest])
def get_data(db:Session = Depends(get_db)):
    return get_chatHistory(db)

@app.post("/postChat", response_model=List[ChatRequest])
def post_data(chat_req: ChatRequestCreate, db: Session = Depends(get_db)):
    return add_chatHistory(db, chat_req)

def run():
    import uvicorn
    uvicorn.run(app)

if __name__ == "__main__":
    run()
