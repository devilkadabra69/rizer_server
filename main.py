from fastapi import FastAPI
from app.routes.authRoute import router as authRouter
from app.core.config import get_settings,Settings

__config:Settings = get_settings()

app = FastAPI(root_path=__config.SERVER_BASE_PATH,version=__config.SERVER_VERSION)
app.include_router(authRouter)