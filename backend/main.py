from fastapi import FastAPI
from fastapi.security import HTTPBearer
from routers import admin, employee

security = HTTPBearer()
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000", # Or whatever port your vuetify is running on
]

app.include_router(
    employee.router,
    prefix="/employee",
    tags=["Employee"],
    responses={404: {"description": "Not Found"}},
)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["Admin"],
    responses={404: {"description": "Not Found"}},
)
