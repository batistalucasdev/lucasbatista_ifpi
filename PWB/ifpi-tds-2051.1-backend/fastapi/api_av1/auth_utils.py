from datetime import datetime, timezone, timedelta
from typing import Annotated
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext

from auth_dao import AuthDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    hash = pwd_context.hash(password)
    return hash