from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from auth_dao import AuthDAO
from auth_utils import verify_hash_password, create_jwt_token, get_current_user, hash_password, is_valid_password
from modelos import SignInUser, SignUpUser, Usuario

router = APIRouter()

auth_dao = AuthDAO()

@router.post("/auth/signin")
def login(data: SignInUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

    if not usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou senha inválidos"
        )
    
    if not verify_hash_password(data.senha, usuario_existente.senha):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email ou senha inválidos"
        )
    
    access_token = create_jwt_token(usuario_existente.email)
    return {
        "username": usuario_existente.nome,
        "access_token": access_token
    }

@router.post("/auth/signup", status_code=status.HTTP_201_CREATED)
def signup(data: SignUpUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

    if not is_valid_password(data.senha):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha inválida"
        )
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Já existe um usuário cadastrado com esse email {data.email}."
        )
    
    data.senha = hash_password(data.senha)
    usuario = auth_dao.salvar(data)

    return usuario

@router.get("/auth/me")
def me(user: Annotated[Usuario, Depends(get_current_user)]):
    return {
        "nome": user.nome,
        "email": user.email
    }

'''
@router.post("/auth/forget-password")
def forget_password(data: SignInUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

    if not usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email não encontrado"
        )
    
    # Aqui você pode implementar a lógica para enviar um email de redefinição de senha
    # Por exemplo, gerar um token de redefinição e enviar por email

    return {"message": "Instruções para redefinir a senha foram enviadas para o email."}
'''