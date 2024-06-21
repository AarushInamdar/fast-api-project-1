from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []
# Get all to-dos
@app.get("/todos")
async def get_todos():
    return {"to-dos": todos}

# create a to-do
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    #return {"to-dos": todos)
    return {"message": "Todo has been added"} 

# Get a single to-do
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}


# Update a to-do
@app.put("/todos/{todo_id}")
async def delete_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"Todo": todo}
    return {"message": "No todos found"}

# Delete a to-do
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo item deleted"}
    return {"message": "No todos found"}