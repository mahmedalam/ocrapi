from fastapi import FastAPI, Request, Response

from config import settings
from routes import router as ocr_router

app = FastAPI(
    title="OCR API",
    description="API for extracting data from images",
    version="0.1.0"
)


@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    if not request.headers.get("X-API-KEY") == settings.API_KEY:
        return Response("Unauthorized", status_code=401)
    return await call_next(request)


@app.get("/")
def read_root(request: Request):
    return "OCR API"


app.include_router(ocr_router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)
