import sqlite3

from modelos import Usuario, Tarefa, TarefaCreate


class TarefasDAO():
    
    def __init__(self):
        pass
    
    def todos(self):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            select_query = 'SELECT * FROM tarefas;'
            cursor.execute(select_query)

            tarefas_list = cursor.fetchall()
            
            tarefas: list[Tarefa] = []
            
            for tarefa in tarefas_list:
                tarefa = Tarefa(
                    id=tarefa[0],
                    titulo=tarefa[1],
                    descricao=tarefa[2],
                    concluida=tarefa[3]
                )
                
                tarefas.append(tarefa)
            return tarefas
        
    def todos_por_usuario(self, usuario: Usuario):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            select_query = 'SELECT * FROM tarefas WHERE usuario_id = ?;'
            cursor.execute(select_query, (usuario.id,))

            tarefas_list = cursor.fetchall()
            
            tarefas: list[Tarefa] = []
            
            for tarefa in tarefas_list:
                tarefa = Tarefa(
                    id=tarefa[0],
                    titulo=tarefa[1],
                    descricao=tarefa[2],
                    concluida=tarefa[3]
                )
                
                tarefas.append(tarefa)
            return tarefas
        
    def obter_por_id(self, id: int):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            select_query = 'SELECT * FROM tarefas WHERE id = ?;'
            cursor.execute(select_query, (id,))

            tarefa = cursor.fetchone()
            
            if not tarefa:
                return None
            
            tarefa = Tarefa(
                id=tarefa[0],
                titulo=tarefa[1],
                descricao=tarefa[2],
                concluida=tarefa[3]
            )
        return tarefa
    
    def remover_por_id(self, id: int):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            delete_query = 'DELETE FROM tarefas WHERE id = ?;'
            cursor.execute(delete_query, (id,))
            result = cursor.fetchone()
            
            if not result:
                return None

    def atualizar_por_id(self, id:int, tarefa: Tarefa):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            update_query = 'UPDATE tarefas SET titulo = ?, descricao = ?, concluida = ? WHERE id = ?;'
            cursor.execute(update_query, (tarefa.titulo, tarefa.descricao, tarefa.concluida, id))
            connection.commit() #verificar essa parte

    def inserir(self, tarefa: TarefaCreate, usuario: Usuario):
        with sqlite3.connect('tarefas.db') as connection:
            cursor = connection.cursor()

            sql = 'INSERT INTO tarefas (titulo, descricao, concluida) VALUES (?, ?, ?);'
            cursor.execute(sql, (tarefa.titulo, 
                                 tarefa.descricao, 
                                 tarefa.concluida,
                                 usuario.id))
        
            id = cursor.lastrowid
            return Tarefa(id=id, **tarefa())