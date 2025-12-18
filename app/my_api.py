from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return{'message': 'Bank Marketing Test API is running'}
