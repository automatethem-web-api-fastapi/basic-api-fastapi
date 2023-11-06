#!/bin/sh
cd ..
rm nohup.out
#nohup uvicorn main:fast_api --reload --host 0.0.0.0 --port 8000 & 
nohup uvicorn main:fast_api --reload --host 0.0.0.0 & 
