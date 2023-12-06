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
    
def register(app):
    app.add_api_route(path="/api/basic-api-fastapi/get", endpoint=api, methods=["GET"])
    app.add_api_route(path="/api/basic-api-fastapi/post", endpoint=api, methods=["POST"])
