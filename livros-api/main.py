from fastapi import FastAPI
from database import engine, Base
from router import router as livro_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Livros",
    description="CRUD com FastAPI + SQLAlchemy + SQLite",
    version="2.0.0"
)

app.include_router(livro_router)

@app.get("/")
def raiz():
    return {"Status": "online", "docs": "/docs", "versao": "2.0.0"}