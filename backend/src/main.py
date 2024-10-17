import uvicorn
from fastapi import FastAPI

from web import explorer, creature

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    return {"message": "Hello World"}

@app.get("/echo/{thing}")
def echo(thing: str):
    return {"echo": thing}  

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)