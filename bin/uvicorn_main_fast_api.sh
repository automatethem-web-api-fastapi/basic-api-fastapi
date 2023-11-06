#!/bin/sh
cd ..
rm nohup.out
#nohup uvicorn main:app --reload --host 0.0.0.0 --port 8000 & 
nohup uvicorn main:app --reload --host 0.0.0.0 & 
