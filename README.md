# basic-api-fastapi

https://github.com/automatethem-python-api-reflex/basic-api-reflex/tree/main

https://github.com/render-examples/fastapi

```
uvicorn main:fast_api --reload --host 0.0.0.0
```

http://localhost:8000/docs

## 추가 정보

## 원본 Api

## 엔드 포인트

### text input

http://localhost:8000/api/basic-api-fastapi/api  
https://automatethem.net:8000/api/basic-api-fastapi/api
```
curl http://localhost:8000/api/basic-api-fastapi/api \
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
curl https://automatethem.net:8000/api/basic-api-fastapi/api \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer AUTOMATETHEM" \
-d '{
    "inputs": "This is a good movie!"
}'
```

### image input

http://localhost:8000/api/basic-api-fastapi/api  
https://automatethem.net:8000/api/basic-api-fastapi/api
```
curl http://localhost:8000/api/basic-api-fastapi/api \
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
curl https://automatethem.net:8000/api/basic-api-fastapi/api \
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

http://localhost:8000/api/basic-api-fastapi/api  
https://automatethem.net:8000/api/basic-api-fastapi/api
```
curl http://localhost:8000/api/basic-api-fastapi/api \
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
curl https://automatethem.net:8000/api/basic-api-fastapi/api \
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

https://basic-api-fastapi.vercel.app/api/basic-api-fastapi/api?inputs=hello
```
[{"label":"pos","score":0.8038843274116516}]
```

https://basic-api-fastapi.vercel.app/docs

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

https://basic-api-fastapi.onrender.com/docs  
https://render.com/  
