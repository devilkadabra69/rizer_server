from fastapi import FastAPI
from app.routes.authRoute import router as authRouter

app = FastAPI(root_path="/app",version="1.0.0.0")
app.include_router(authRouter)