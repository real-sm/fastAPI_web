from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# static routing
@app.get('/')
def index():
    return "blog_website"

@app.get('/about')
def about():
    return {"about": {"name": "sumit_modak", "dob": "2003"}}

@app.get('/blog/list')
def list_blog():
    return {"blog": "list"}

# post method
@app.post('/blog/create')
def create_blog(request: Blog):
    return request

# dynamic routing
@app.get('/blog/{id}')
def blog_show(id):
    return {"id": id}

@app.get('/blog/{id}/comments')
def blog_comments(id: int, limit = 10):
    return {"comments": {"id": id}, "count": limit}

# query parameters
@app.get('/blog')
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the list"}
    else: 
        return {"data": f"{limit} blogs from the list"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
