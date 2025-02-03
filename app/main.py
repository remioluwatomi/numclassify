from fastapi import FastAPI
from .routers import classify_number
from fastapi.middleware.cors import CORSMiddleware
from .custom_openapi import custom_openapi

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(classify_number.router)

app.openapi = lambda: custom_openapi(app)


