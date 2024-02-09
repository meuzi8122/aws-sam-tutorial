from pydantic import BaseModel


class Account(BaseModel):
    userId: int


class AuthenticationResult(BaseModel):
    accessToken: str
    idToken: str


class LoginInfo(BaseModel):
    email: str
    password: str
