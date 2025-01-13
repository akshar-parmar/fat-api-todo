from fastapi import FastAPI
from pydantic import BaseModel


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
