from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas import UserCreate, UserLogin, UserOut, TaskCreate, TaskOut
from utils import gerar_hash_senha, verificar_senha
from models import (
    criar_usuario, buscar_usuario_por_email, buscar_usuario_por_id,
    criar_tarefa, listar_tarefas, buscar_tarefa_por_id,
    atualizar_tarefa, deletar_tarefa
)
from auth import criar_token_acesso, verificar_token
from database import criar_tabelas

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Criação das tabelas ao iniciar o app
@app.on_event("startup")
def startup():
    criar_tabelas()

# Dependência para obter o usuário autenticado pelo token
def usuario_atual(token: str = Depends(oauth2_scheme)):
    email = verificar_token(token)
    if email is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    user = buscar_usuario_por_email(email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
    return user

# Rota para cadastro de usuários
@app.post("/usuarios/", response_model=UserOut)
def cadastro_usuario(user: UserCreate):
    usuario_existente = buscar_usuario_por_email(user.email)
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    senha_hash = gerar_hash_senha(user.senha)
    user_id = criar_usuario(user.email, senha_hash)
    if not user_id:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário")
    return {"id": user_id, "email": user.email}

# Rota de login (OAuth2) para gerar token JWT
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = buscar_usuario_por_email(form_data.username)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado")
    if not verificar_senha(form_data.password, usuario["senha"]):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    token = criar_token_acesso({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

# Rota para criar uma tarefa (autenticado)
@app.post("/tarefas/", response_model=TaskOut)
def criar_uma_tarefa(tarefa: TaskCreate, usuario=Depends(usuario_atual)):
    tarefa_id = criar_tarefa(tarefa.titulo, tarefa.descricao or "", usuario["id"])
    tarefa_db = buscar_tarefa_por_id(tarefa_id, usuario["id"])
    return tarefa_db

# Rota para listar tarefas do usuário autenticado
@app.get("/tarefas/", response_model=list[TaskOut])
def listar_tarefas_usuario(usuario=Depends(usuario_atual)):
    tarefas = listar_tarefas(usuario["id"])
    return tarefas

# Rota para obter uma tarefa específica
@app.get("/tarefas/{tarefa_id}", response_model=TaskOut)
def obter_tarefa(tarefa_id: int, usuario=Depends(usuario_atual)):
    tarefa = buscar_tarefa_por_id(tarefa_id, usuario["id"])
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

# Rota para atualizar uma tarefa
@app.put("/tarefas/{tarefa_id}", response_model=TaskOut)
def atualizar_tarefa_id(tarefa_id: int, tarefa: TaskCreate, usuario=Depends(usuario_atual)):
    atualizado = atualizar_tarefa(tarefa_id, usuario["id"], tarefa.titulo, tarefa.descricao or "")
    if atualizado == 0:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada ou sem permissão")
    tarefa_db = buscar_tarefa_por_id(tarefa_id, usuario["id"])
    return tarefa_db

# Rota para deletar uma tarefa
@app.delete("/tarefas/{tarefa_id}", status_code=204)
def deletar_tarefa_id(tarefa_id: int, usuario=Depends(usuario_atual)):
    deletado = deletar_tarefa(tarefa_id, usuario["id"])
    if deletado == 0:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada ou sem permissão")
    return None
