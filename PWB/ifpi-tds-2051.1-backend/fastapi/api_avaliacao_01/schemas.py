from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    senha: str

class UserLogin(BaseModel):
    email: str
    senha: str

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    titulo: str
    descricao: str | None = None

class TaskOut(BaseModel):
    id: int
    titulo: str
    descricao: str | None = None
    usuario_id: int

    class Config:
        orm_mode = True
