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
    print(ans)
    return FileResponse("index.html")

@app.get("/check")
def get_check(number: str):
    ball = 0
    strike = 0
    
    for i in range(len(number)):
        if int(number[i]) in ans:
            if int(number[i]) == ans[i]:
                strike += 1
            else:
                ball += 1

    table = ["OUT", "HIT", "HIT", "HIT", "HIT"]

    if strike == 4:
        data = {"result": "HOMERUN", "ball": ball, "strike": strike}
    else:
        data = {"result": table[ball+strike], "ball": ball, "strike": strike}

    return data