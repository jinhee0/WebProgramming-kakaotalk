from sqlalchemy import Column, Integer, String

from database import Base

class ChatHistory(Base):
    __tablename__ = "chatHistory"

    index = Column(Integer, primary_key = True)
    groupChat = Column(Integer)
    user_id = Column(String)
    friend_name = Column(String)
    message = Column(String)
    timeString = Column(String)
    response = Column(Integer)
    responseId = Column(String)
    responsetext = Column(String)

# 유저의 아이디, 패스워드
class UserInfo(Base):
    __tablename__ = "UserInfo"

    index = Column(Integer, primary_key = True)
    user_id = Column(String)
    user_password = Column(String)

# 유저의 친구리스트
class FriendList(Base):
    __tablename__ = "FriendList"

    index = Column(Integer, primary_key = True)
    user_id = Column(String)
    friend_name = Column(String)

# 유저의 채팅리스트
