from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
import json
from typing import Any
from typing import Union
from typing import Dict
from typing import List
from typing import Optional
import os
import asyncio
from fastapi.middleware.cors import CORSMiddleware

#app = FastAPI()
app = FastAPI(docs_url="/api/fastapi/api/docs", openapi_url="/api/fastapi/api/openapi.json")

allowed_origins = [
    "https://ar.freeonlineutility.com",
    "https://bn.freeonlineutility.com",
    "https://zh.freeonlineutility.com",
    "https://en.freeonlineutility.com",
    "https://fr.freeonlineutility.com",
    "https://de.freeonlineutility.com",
    "https://hi.freeonlineutility.com",
    "https://it.freeonlineutility.com",
    "https://ja.freeonlineutility.com",
    "https://ko.freeonlineutility.com",
    "https://mr.freeonlineutility.com",
    "https://fa.freeonlineutility.com",
    "https://pt.freeonlineutility.com",
    "https://pa.freeonlineutility.com",
    "https://ru.freeonlineutility.com",
    "https://es.freeonlineutility.com",
    "https://ta.freeonlineutility.com",
    "https://te.freeonlineutility.com",
    "https://tr.freeonlineutility.com",
    "https://ur.freeonlineutility.com",
    "https://t.ar.freeonlineutility.com",
    "https://t.bn.freeonlineutility.com",
    "https://t.zh.freeonlineutility.com",
    "https://t.en.freeonlineutility.com",
    "https://t.fr.freeonlineutility.com",
    "https://t.de.freeonlineutility.com",
    "https://t.hi.freeonlineutility.com",
    "https://t.it.freeonlineutility.com",
    "https://t.ja.freeonlineutility.com",
    "https://t.ko.freeonlineutility.com",
    "https://t.mr.freeonlineutility.com",
    "https://t.fa.freeonlineutility.com",
    "https://t.pt.freeonlineutility.com",
    "https://t.pa.freeonlineutility.com",
    "https://t.ru.freeonlineutility.com",
    "https://t.es.freeonlineutility.com",
    "https://t.ta.freeonlineutility.com",
    "https://t.te.freeonlineutility.com",
    "https://t.tr.freeonlineutility.com",
    "https://t.ur.freeonlineutility.com",
    "https://freeonlineutility.com",
    "https://www.freeonlineutility.com",
]
#allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # 'GET', 'POST', etc. or "*" for all
    allow_headers=[
        "Authorization",
        "Content-Type",
        "X-CSRF-Token",
        "X-Requested-With",
        "Accept",
        "Accept-Version",
        "Content-Length",
        "Content-MD5",
        "Date",
        "X-Api-Version"
    ],
)

#'''
class RequestData(BaseModel):
    inputs: Union[Any, Dict]
    parameters: Optional[Dict]

@app.get("/api/fastapi/api")
async def api(inputs):
    print(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

@app.post("/api/fastapi/api")
async def api(request_data: RequestData):
    inputs = request_data.json()
    inputs = json.loads(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction
#'''
'''
class RequestData(BaseModel):
    inputs: Union[Any, Dict]
    parameters: Optional[Dict]
            
async def get(inputs):
    print(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

async def post(request_data: RequestData):
    inputs = request_data.json()
    inputs = json.loads(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

app.add_api_route(path="/api/fastapi/api", endpoint=get, methods=["GET"])
app.add_api_route(path="/api/fastapi/api", endpoint=post, methods=["POST"])
'''
