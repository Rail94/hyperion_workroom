from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def ping():
    return {"message": "home"}