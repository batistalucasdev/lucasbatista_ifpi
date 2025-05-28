from typing import Annotated
from fastapi import FastAPI, HTTPException, APIRouter, status, Depends
from auth_utils import get_current_user
from modelos import TarefaCreate, Usuario
from tarefas_dao import TarefasDAO

roteador_tarefas = APIRouter()

tarefas_dao = TarefasDAO()

@roteador_tarefas.post('/tarefas', status_code=status.HTTP_201_CREATED)
def tarefas_create(novo: TarefaCreate, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefas = tarefas_dao.listar_tarefas(novo, user)
    if not tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    tarefas = tarefas_dao.criar_tarefa(novo, user)
    
    return tarefas

@roteador_tarefas.get('/tarefas')
def tarefas_list(user:Annotated [Usuario, Depends(get_current_user)]):
    tarefas = tarefas_dao.todos_por_usuario(user)
    return tarefas

