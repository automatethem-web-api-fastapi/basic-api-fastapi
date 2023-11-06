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

## render
