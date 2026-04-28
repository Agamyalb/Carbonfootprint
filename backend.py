from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/test")
def test():
    return {"status": "ok"}