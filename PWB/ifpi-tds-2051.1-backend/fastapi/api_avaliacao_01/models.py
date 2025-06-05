from database import get_connection

# Usuários
def criar_usuario(email: str, senha_hash: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha_hash))
        conn.commit()
        return cursor.lastrowid
    except:
        return None
    finally:
        conn.close()

def buscar_usuario_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def buscar_usuario_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    user = cursor.fetchone()
    conn.close()
    return user

# Tarefas
def criar_tarefa(titulo: str, descricao: str, usuario_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (titulo, descricao, usuario_id) VALUES (?, ?, ?)",
        (titulo, descricao, usuario_id)
    )
    conn.commit()
    tarefa_id = cursor.lastrowid
    conn.close()
    return tarefa_id

def listar_tarefas(usuario_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE usuario_id = ?", (usuario_id,))
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def buscar_tarefa_por_id(tarefa_id: int, usuario_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM tarefas WHERE id = ? AND usuario_id = ?", (tarefa_id, usuario_id)
    )
    tarefa = cursor.fetchone()
    conn.close()
    return tarefa

def atualizar_tarefa(tarefa_id: int, usuario_id: int, titulo: str, descricao: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ? AND usuario_id = ?",
        (titulo, descricao, tarefa_id, usuario_id)
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated

def deletar_tarefa(tarefa_id: int, usuario_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id = ? AND usuario_id = ?", (tarefa_id, usuario_id)
    )
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted
