from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI (title='API de Filmes', version='1.0.0')

# Banco de dados em memória (lista Python)
# Em produção: usariamos SQlite, PostgreSQL, etc...
filmes = [
    {"id": 1, "titulo": "Vingadores", "diretor": "Joss Whedon", "ano": 2012, "nota": 8.0},
    {"id": 2, "titulo": "Interstellar", "diretor": "Christopher Nolan", "ano": 2014, "nota": 8.6},
    {"id": 3, "titulo": "O Rei Leão", "diretor": "Roger Allers, Rob Minkoff", "ano": 1994, "nota": 8.5}
]
proximo_id = 4 # Controlar o próximo iD

class FilmeCreate(BaseModel):

    titulo: str
    diretor: str
    ano: int
    nota: Optional[float] = None

# GET /filmes -> lista todos os filmes
@app.get('/filmes')
def listar_filmes():
    return filmes

# GET /filmes/(id) -> busca um filme pelo ID
@app.get('/filmes/{filme_id}')
def buscar_filme(filme_id: int):
    filme = next(
        (f for f in filmes if f['id'] == filme_id),
        None # valor padrao se não encontrar
    )   
    if filme is None:
        return {"erro": f"Filme {filme_id} não encontrado"}
    return filme

# POST /filmes -> cria um novo filme
@app.post('/filmes', status_code=201)
def criar_filme(filme: FilmeCreate):
    global proximo_id

    # Cria o novo filme com o próximo ID disponivel
    novo_filme = {
        'id': proximo_id,
        'titulo': filme.titulo,
        'diretor': filme.diretor,
        'ano': filme.ano,
        'nota': filme.nota
    }
    filmes.append(novo_filme)
    proximo_id += 1

    return novo_filme