from datetime import datetime
from typing import Optional, Text
from uuid import uuid4 as uuid

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



@app.get('/')
def Operation(num:int, num2:int):
    result=num+num2
    return {"result": result}

@app.get('/version')
def root_load():
    return{"version":1.0,"name": "calculadora"}


