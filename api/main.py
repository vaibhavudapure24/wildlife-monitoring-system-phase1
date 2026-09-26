from fastapi import FastAPI

app = FastAPI(
    title="AI Wildlife Animal Monitoring System API",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Wildlife Monitoring API is working on Vercel"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
