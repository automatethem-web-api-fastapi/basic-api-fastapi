#!/bin/sh
kill -9  `ps -ef | grep -E 'uvicorn|from multiprocessing.resource_tracker import main|from multiprocessing.spawn import spawn_main' | awk '{print $2}'`
