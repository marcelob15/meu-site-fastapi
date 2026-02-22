from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Python 3.12 rodando localmente"}