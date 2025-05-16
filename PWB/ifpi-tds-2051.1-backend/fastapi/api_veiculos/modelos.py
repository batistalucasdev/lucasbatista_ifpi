from pydantic import BaseModel

class usuarioBase(BaseModel):
  nome: str
  email: str
  senha: str

class Usuario(usuarioBase):
  id: int | None = None


class SignUpUser(usuarioBase):
  pass


class VeiculoBase(BaseModel):
  nome: str
  ano_fabricacao: int
  ano_modelo: int
  valor: float


class Veiculo(VeiculoBase):
  id: int | None = None

class VeiculoCreate(VeiculoBase):
  pass
