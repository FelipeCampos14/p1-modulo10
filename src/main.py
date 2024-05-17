from fastapi import FastAPI, Cookie, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from database.models import TodoDB
from database.database import SessionLocal, Base, engine
from database.schemes import Todo, TodoUpdate, TodoCreate

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# ToDos CRUD

@app.get("/pedidos", response_model=List[Todo])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoDB).all()
    db.close()
    return todos

@app.get("/pedidos/{todos}", response_model=Todo)
def get_todo(todos: int, db: Session = Depends(get_db)):
    todo = db.query(TodoDB).filter(TodoDB.id == todos).first()
    db.close()
    if todo is None:
        raise HTTPException(status_code=404, detail="O Pedido não foi encontrado.")
    return todo

@app.post("/novo", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = TodoDB(name=todo.name, email=todo.email, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo

@app.put("/pedidos/{todos}", response_model=Todo)
def update_todo(todos: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(TodoDB).filter(TodoDB.id == todos).first()
    if db_todo is None:
        db.close()
        raise HTTPException(status_code=404, detail="O Pedido não foi encontrado.")
    if todo.name is not None:
        db_todo.name = todo.name
    if todo.email is not None:
        db_todo.email = todo.email
    if todo.description is not None:
        db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    db.close()
    return db_todo

@app.delete("/pedidos/{todos}", response_model=Todo)
def delete_todo(todos: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoDB).filter(TodoDB.id == todos).first()
    if db_todo is None:
        db.close()
        raise HTTPException(status_code=404, detail="O Pedido não foi encontrado.")
    db.delete(db_todo)
    db.commit()
    db.close()
    return db_todo