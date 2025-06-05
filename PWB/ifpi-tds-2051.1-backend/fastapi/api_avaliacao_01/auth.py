from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "chave_supersecreta"
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 30

def criar_token_acesso(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRACAO_MINUTOS)
    dados.update({"exp": expiracao})
    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return None
        return email
    except JWTError:
        return None
