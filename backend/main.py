from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from routers import admin, employee
from fastapi.middleware.cors import CORSMiddleware

security = HTTPBearer()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = [
    "http://localhost",
    "http://localhost:3000", # Or whatever port your vuetify is running on
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/")
def read_root():
    return {"message": "API is running"}
