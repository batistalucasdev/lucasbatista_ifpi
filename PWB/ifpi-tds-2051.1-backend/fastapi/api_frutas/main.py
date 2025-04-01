from fastapi import FastAPI, HTTPException

app = FastAPI()

frutas = [
    {'id': 1,'nome': 'Banana'}, 
    {'id': 2,'nome': 'Maçã'},
    {'id': 3,'nome': 'Melancia'},
    {'id': 4,'nome': 'Abacaxi'}
]

@app.get('/frutas')
def frutas_list(order: str = None):
    if not order:
        return frutas
    
    # ordenar
    if order == 'ASC':
        # ordem crescente por nome
        frutas_ordenadas = sorted(frutas, key=lambda f:f['nome'])
        return frutas_ordenadas
    elif order == 'DESC':
        # ordem decrescente por nome
        frutas_ordenadas = sorted(frutas, key=lambda f:f['nome'], reverse=True)
        return frutas_ordenadas
    else:
        raise HTTPException(status_code=400, detail='Order tem que ser ASC ou DESC.')



@app.get('/frutas/{id}')
def frutas_detail(id: int):
    fruta_localizada = obter_fruta_por_id(id)
    if fruta_localizada:
        return fruta_localizada
    else:
        return HTTPException(status_code=404, detail='Fruta não localizada.')

'''
@app.get('/frutas/{id}')
def frutas_detail(id: int):
    fruta_localizada = obter_fruta_por_id(id)
    if fruta_localizada:
        return fruta_localizada
    else:
        return Response(status_code=404, content='Fruta não localizada.')
'''

@app.post('/frutas', status_code=201)
def frutas_create():
    frutas.append('manga')
    return {'nome': 'manga'}

# Utilizados
def obter_fruta_por_id(id: int):
    for fruta in frutas:
        if fruta['id'] == id:
            return fruta
    return None