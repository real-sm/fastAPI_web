from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"name": "sumit", "title": "modak"}

@app.get('/about')
def about():
    return {"about": {"dob": "2003"}}