import os

import uvicorn as uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.app.api.api_v1.api import api_router
from app.app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
"""if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )"""

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    port = os.environ.get('PORT')
    uvicorn.run(app, host="0.0.0.0", port=port)