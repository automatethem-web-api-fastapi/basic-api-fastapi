from fastapi import FastAPI

fast_api = FastAPI()

from api.basic_api_fastapi import api as api_basic_pi_fastapi_api
api_basic_pi_fastapi_api.register(fast_api)
