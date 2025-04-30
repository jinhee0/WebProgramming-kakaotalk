from sqlalchemy.orm import Session

from models import ChatHistory, UserInfo, FriendList
from schema import ChatRequest, UserInfoRequest, FriendListRequest

def get_chatHistory(db: Session):
    return db.query(ChatHistory).all()

def add_chatHistory(db:Session, item:ChatRequest):
    db_item = ChatHistory(groupChat = item.groupChat, user_id = item.user_id, friend_name = item.friend_name, message = item.message, timeString = item.timeString, response=item.response,  responseId=item.responseId,  responsetext=item.responsetext)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db.query(ChatHistory).all()

def get_userInfo(db: Session):
    return db.query(UserInfo).all()

def add_userInfo(db:Session, item:UserInfoRequest):
    db_item = UserInfo(user_id = item.user_id, user_password = item.user_password)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db.query(UserInfo).all()

def get_friendList(db: Session):
    return db.query(FriendList).all()

def add_friendList(db:Session, item:FriendListRequest):
    db_item = FriendList(user_id = item.user_id, friend_name = item.friend_name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db.query(FriendList).all()