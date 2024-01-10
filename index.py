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

#app = FastAPI()
app = FastAPI(docs_url="/api/fastapi/api/docs", openapi_url="/api/fastapi/api/openapi.json")

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

app.add_api_route(path="/api/fastapi/api/basic-api-fastapi", endpoint=get, methods=["GET"])
app.add_api_route(path="/api/fastapi/api/basic-api-fastapi", endpoint=post, methods=["POST"])
