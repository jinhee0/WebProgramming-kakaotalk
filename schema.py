from pydantic import BaseModel
from typing import Optional

class ChatRequestBase(BaseModel):
    groupChat: int
    user_id: str
    friend_name: str
    message: str
    timeString: str
    response: int
    responseId: str
    responsetext: str

class ChatRequestCreate(ChatRequestBase):
    pass

class ChatRequest(ChatRequestBase):
    index: Optional[int]

    class Config:
        orm_mode = True


class UserInfoRequestBase(BaseModel):
    user_id: str
    user_password: str

class UserInfoRequestCreate(UserInfoRequestBase):
    pass

class UserInfoRequest(UserInfoRequestBase):
    index: Optional[int]

    class Config:
        orm_mode = True

class FriendListRequestBase(BaseModel):
    user_id: str
    friend_name: str

class FriendListRequestCreate(FriendListRequestBase):
    pass

class FriendListRequest(FriendListRequestBase):
    index: Optional[int]

    class Config:
        orm_mode = True