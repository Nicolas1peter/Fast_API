from fastapi import FastAPI, Form

from typing import Optional

from pydantic import BaseModel

import uvicorn

app = FastAPI()

class CoordIn(BaseModel):
    password : str
    lat  : float
    lon  : float
    zoom : Optional[int] = None
    description: Optional[int] = None

class CoordOut(BaseModel):
    lat  : float
    lon  : float
    zoom : Optional[int] = None
    description: Optional[int] = None

@app.get("/")
async def hello_world():
    return {"hello" : "world"}

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id": component_id}

@app.get("/component/")
async def read_component(number: int, text: str):
    return {"number" : number, "text": text}

@app.post("/position/", response_model=CoordOut, response_model_exclude={'description'})
async def make_position(coord: CoordIn):
    return coord


app.post("/login/")
async def login(username: str = Form(...), password: str= Form(...)):
    return {username: username}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)