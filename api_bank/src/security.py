import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from passlib.context import CryptContext

SECRET = "my-secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


class AccessToken(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JWTToken(BaseModel):
    access_token: AccessToken


# Geração do token JWT
def sign_jwt(user_id: int) -> dict[str, str]:
    now = time.time()
    payload = {
        "iss": "desafio-bank.com.br",
        "sub": str(user_id),
        "aud": "desafio-bank",
        "exp": now + (60 * 30),
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token}


# Decodificação do JWT
async def decode_jwt(token: str) -> JWTToken | None:
    try:
        decoded_token = jwt.decode(
            token, SECRET, audience="desafio-bank", algorithms=[ALGORITHM], leeway=60
        )
        access_token = AccessToken.model_validate(decoded_token)
        return JWTToken(access_token=access_token)
    except Exception as e:
        print("ERRO JWT:", e)
        return None


# Middleware de autenticação
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if scheme != "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme.",
                )

            payload = await decode_jwt(credentials)
            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid or expired token.",
                )
            return payload

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization code.",
        )


async def get_current_user(
    token: Annotated[JWTToken, Depends(JWTBearer())],
) -> dict[str, str]:
    return {"user_id": token.access_token.sub}


def login_required(current_user: Annotated[dict[str, str], Depends(get_current_user)]):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )
    return current_user
