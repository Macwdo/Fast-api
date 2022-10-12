from fastapi import HTTPException, status, APIRouter
import sqlite3
from models.Livros import Livros_PATCH, Livros_POST

router = APIRouter()

con = sqlite3.connect("models/livros.sqlite3")
dbcursor = con.cursor()


@router.get("/")
async def list_view_api():
    dbcursor.execute("SELECT id, titulo, autor FROM Livros")
    dados = []
    resultado = dbcursor.fetchall()
    for dado in resultado:
        serializer = {
            "id": dado[0],
            "titulo": dado[1],
            "autor": dado[2]
        }
        dados.append(serializer)
    return dados


@router.post("/")
async def post_api(dados: Livros_POST):
    query = f"""
    INSERT INTO Livros (titulo,autor) 
    VALUES('{dados.titulo}','{dados.autor}')
    """
    dbcursor.execute(query)
    con.commit()
    dbcursor.execute(
        """
        SELECT id, titulo, autor 
        FROM Livros ORDER BY id 
        DESC LIMIT 1 
        """)
    resultado = dbcursor.fetchone()
    return {
        "id": resultado[0],
        "titulo": resultado[1],
        "autor": resultado[2]
    }


@router.get("/{id}")
async def view_api(id: int):
    dbcursor.execute(f"SELECT id, titulo, autor FROM Livros WHERE id={id}")
    dados = dbcursor.fetchone()
    if dados is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {
        'id': dados[0],
        'titulo': dados[1],
        'autor': dados[2]
        }


@router.patch("/{id}")
async def update_api(id: int, data: Livros_PATCH):
    dbcursor.execute(f"SELECT * FROM Livros WHERE id = {id}")
    dados = dbcursor.fetchone()
    if dados is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if data.titulo and data.autor:
        query = f'''
        UPDATE Livros
        SET autor = '{data.autor}'
        ,titulo = '{data.titulo}'
        WHERE id = {id}
        '''

    elif data.autor:
        query = f"UPDATE Livros SET autor = '{data.autor}' WHERE id = {id}"
    elif data.titulo:
        query = f"UPDATE Livros SET titulo = '{data.titulo}' WHERE id = id"
    else:
        query = f"SELECT * FROM Livros WHERE id = {id}"
    dbcursor.execute(query)
    con.commit()
    dbcursor.execute(f"SELECT * FROM Livros WHERE id = {id}")
    resultado = dbcursor.fetchone()
    return {
        "id": resultado[0],
        "titulo": resultado[1],
        "autor": resultado[2]
    }


@router.delete("/{id}")
async def delete_api(id: int):
    dbcursor.execute(f"SELECT * FROM Livros WHERE id = {id}")
    dados = dbcursor.fetchone()
    if dados is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    dbcursor.execute(f"DELETE FROM Livros WHERE id = {id}")
    con.commit()
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
