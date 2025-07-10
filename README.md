# basic-api-fastapi

https://github.com/automatethem-python-api-reflex/basic-api-reflex/tree/main

https://github.com/render-examples/fastapi

```
#uvicorn index:app --host 0.0.0.0
#uvicorn index:app --host 0.0.0.0 --port 8000
uvicorn index:app --reload
```

http://localhost:8000/api/docs

## 추가 정보

## models

## 엔드 포인트

### text input

http://localhost:8000/api 
https://automatethem.net:8000/api
```
curl http://localhost:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "This is a good movie!"
}'
```

```
[
  {
    "label": "pos",
    "score": 0.8038843274116516
  }
]
```

```
curl https://automatethem.net:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "This is a good movie!"
}'
```

### image input

http://localhost:8000/api
https://automatethem.net:8000/api
```
curl http://localhost:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "data:image/png;base64,'"$( base64 -i predict_inputs/rock.jpg )"'"
}'
```

```
[
  {
    "label": "pos",
    "score": 0.8038843274116516
  }
]
```

```
curl https://automatethem.net:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "data:image/png;base64,'"$( base64 -i rock.jpg )"'"
}'
```

참고)

```
(base) automatethem@automatethemui-MacBookPro basic-api-pynecone-main 3 % base64 -i rock.jpg
/9j/4AAQSkZJRgABAQAAAQABA...b32qjR37P/2Q==
```

### audio input

http://localhost:8000/api  
https://automatethem.net:8000/api
```
curl http://localhost:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "data:audio/wav;base64,'"$( base64 -i predict_inputs/up.wav )"'"
}'
```

```
[
  {
    "label": "pos",
    "score": 0.8038843274116516
  }
]
```

```
curl https://automatethem.net:8000/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "data:audio/wav;base64,'"$( base64 -i up.wav )"'"
}'
```

### image output

```
```

```
[{"label":"pos","score":0.8038843274116516,"outputs":"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDA...fvHC2rn1GKtDMUnJNGabSjrTEf/9k="}]
```

```
```

### audio output

```
```

```
[{"label":"pos","score":0.8038843274116516,"outputs":"data:audio/wav;base64,UklGRiR9AABXQVZFZm10IBAAAAABAA...5//j/CAAUAA4ABQAUAA=="}]
```

```
```

참고)

'''
app.mount("/", StaticFiles(directory="static"), name="static")
'''

# vercel

https://basic-api-fastapi.vercel.app/api?inputs=hello
```
[{"label":"pos","score":0.8038843274116516}]
```

https://basic-api-fastapi.vercel.app/api/docs

FastAPI DEPLOY TO VERCEL IN 5 Minutes  
https://www.youtube.com/watch?v=PKEaFjMdsqA  
https://abdadeel.medium.com/deploy-fastapi-app-on-vercel-serverless-b9fc35bba74d  
Deploying FastAPI app on Vercel Serverless  
https://dev.to/abdadeel/deploying-fastapi-app-on-vercel-serverless-18b1  
!!  
https://github.com/mabdullahadeel/vercel-fastapi-deployment

deploy-python-fastapi-in-vercel  
https://github.com/hebertcisco/deploy-python-fastapi-in-vercel

## render

## 참고 자료

Error: Unable to find any supported Python versions.  
https://stackoverflow.com/a/78256079
https://basic-api-fastapi.onrender.com/api/docs  
https://render.com/  

https://uptimerobot.com/dashboard#795614790
