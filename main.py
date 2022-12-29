from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def get_root():
    global ans
    ans = []
    for i in range(4):
        n = random.randrange(0, 10)

        while n in ans:
            n = random.randrange(0, 10)

        ans.append(n)
    return FileResponse("index.html")