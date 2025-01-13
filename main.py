from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    firstname : str=''
    lastname : str | None
    age : int
    height : float

app = FastAPI()  #creating a instance of fastapi

#@ is the decorator
@app.get('/ping')
async def root():
    return {"message" : "Hello world!!"}

@app.get('/blogs/comment')
async def read_comments():
    return {"message" : "gel"}

#how to read the dynamic url path name
@app.get('/blogs/{blog_id}')
async def process_blog(blog_id:int):
    return {"blog_id" : blog_id}

#query parameters
@app.get('/test/{test_id}')
async def test_root(test_id:str ,name : str,age : int = 100):
    print(f"test_id : {test_id} name : {name} and age : {age}")
    return {"message" : "test"}


#post request : how to send the body
@app.post("/person")
async def test_person(person:Person):
    return person





##Basic todo app
todos = []

class Todo(BaseModel):
    id:int
    title:str
    description:Optional[str] | None
    iscomplete:bool=False
    
    
def print_todos():
    for x in todos:
        print(x)
        print('\n')
        
#create todo
@app.post('/todo')
async def create_todo(req_body:Todo):
    todos.append(req_body)
    print_todos()
    return {"message": "Successfully created todo"}

#get all the todos
@app.get('/todos')
async def get_todos():
    return {"data" :todos }

#get a todo by id
@app.get('/todo/{todo_id}')
async def get_todo_by_id(todo_id:int):
    for todo in todos:
        if(todo.id == todo_id):
            return {"data" : todo} 
    return {"message" : f"No todo found with id {todo_id}"}


#delete a todo with id
@app.delete('/todo/{todo_id}')
async def del_todo_by_id(todo_id:int):
    for todo in todos:
        if (todo.id == todo_id):
            todos.remove(todo)
    return {"message" : f"Todo with id {todo_id} deleted successfully"}

#update a specific todo
@app.put('/todo/{todo_id}')
async def udpate_todo(todo_id:int, req_body:Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.iscomplete = req_body.iscomplete
            todo.description = req_body.description
            todo.title = req_body.title
    return {"message" : "Todo updated successfully"}
    
            
    
