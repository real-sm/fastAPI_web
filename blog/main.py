from fastapi import FastAPI
from . import schemas

app = FastAPI()

@app.post('/blog/create')
def create_blog(request: schemas.Blog):
    return request
