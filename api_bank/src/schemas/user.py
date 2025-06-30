from pydantic import BaseModel


class UserIn(BaseModel):
    owner: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True 