from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def root():
    return Response(content="Hello World to all", media_type="text/plain")