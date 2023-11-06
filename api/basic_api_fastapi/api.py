from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from .handler import EndpointHandler
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
            
async def api(request_data: RequestData):
    inputs = request_data.json()
    inputs = json.loads(inputs)
    prediction = [{'label': 'pos', 'score': 0.8038843274116516}]
    return prediction

def register(fast_api):
    fast_api.add_api_route(path="/api/basic-api-fastapi/api", endpoint=api, methods=["POST"])
