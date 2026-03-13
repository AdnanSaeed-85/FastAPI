from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'hello world'}

@app.get('/about')
def about():
    return {'message': 'My self ADNAN SAEED and i am learning AI'}