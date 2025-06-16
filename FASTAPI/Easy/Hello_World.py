from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root():
    return Response(content="Hello World", media_type="text/plain")