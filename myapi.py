from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'data': {'image':'https://picsum.photos/200'}}