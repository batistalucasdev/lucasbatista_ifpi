from fastapi import FastAPI, HTTPException, APIRouter, status
from modelos import Tarefa, TarefaCreate, TarefaUpdate
from tarefas_dao import TarefasDAO

roteador_taredas = APIRouter()

tarefas_dao = TarefasDAO()

@roteador_tarefas.get('/tarefas')
def listar_tarefas():
    tarefas = tarefas_dao.listar_tarefas()
    return tarefas