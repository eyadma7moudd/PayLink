from fastapi import FastAPI

app = FastAPI(
    title="PayLink API",
    description="Digital Wallet and Bill Payment System",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
