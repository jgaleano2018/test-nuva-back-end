from fastapi import FastAPI, Depends
from app.routers.main_routes import router as mainRoutes
from app.routers.firebase_routes import router as firebaseRoutes
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Todo RestFull Api",

              description="RESTful API for managing tasks, built with FastAPI and Python. The project uses Firebase, MongoDB, and PostgreSQL to store tasks.", version="0.1.0",
              docs_url=None,
              redoc_url=None,
              openapi_url=None,)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mainRoutes, prefix="", tags=["Root"])
app.include_router(firebaseRoutes, prefix="/use-firebase", tags=["Firebase"])