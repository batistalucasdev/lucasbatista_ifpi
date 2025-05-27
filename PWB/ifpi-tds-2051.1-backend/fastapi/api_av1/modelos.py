from pydantic import BaseModel

class UsuarioBase(BaseModel):
    username: str
    email: str
    password_hash: str

class Usuario(UsuarioBase):
    id: int | None = None

class SignUpUsuario(BaseModel):
    pass

class SignInUsuario(BaseModel):
    email: str
    password: str

class TarefaBase(BaseModel):
    titulo: str
    descricao: str | None = None
    concluida: bool = False
    usuario_id: int

class Tarefa(TarefaBase):
    id: int | None = None

class TarefaCreate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None