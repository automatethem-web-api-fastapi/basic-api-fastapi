from fastapi import FastAPI

app = FastAPI()

from api.basic_api_fastapi import api as api_basic_pi_fastapi_api
api_basic_pi_fastapi_api.register(app)
