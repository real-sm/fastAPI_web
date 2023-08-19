from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# static routing
@app.get('/')
def index():
    return {"name": "sumit", "title": "modak"}

@app.get('/about')
def about():
    return {"about": {"dob": "2003"}}

# dynamic routing
@app.get('/blog/list')
def list_blog():
    return {"blog": "list_all_id"}

@app.get('/blog/{id}')
def blog_show(id: int):
    return {"blog": {"id": id}}

@app.get('/blog/{id}/comments')
def blog_comments(id: int, limit = 10):
    return {"id": id, "count": limit}

# query parameters
# @app.get('/blog?limit=32&published=true')
@app.get('/blog')
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the list"}
    else: 
        return {"data": f"{limit} blogs from the list"}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# post method
@app.post('/blog')
def create_blog(request: Blog):
    return request

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
    