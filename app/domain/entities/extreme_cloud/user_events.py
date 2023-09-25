from typing import List
from pydantic import BaseModel

class UserLoginEvent(BaseModel):
    ownerId: int
    orgId: int
    timeStamp: int
    id: str
    userId: int
    code: int
    category: int
    description: str
    userName: str
    vhmName: str
    orgName: str
    deviceCount: int
    hostNames: List[str]
    config: str
    deviceIds: str


class UserLogoutEvent(BaseModel):
    ownerId: int
    orgId: int
    timeStamp: int
    id: str
    userId: int
    code: int
    category: int
    description: str
    userName: str
    vhmName: str
    orgName: str
    deviceCount: int
    hostNames: List[str]
    config: str
    deviceIds: str