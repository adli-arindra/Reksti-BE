from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import register, student, attend, class_post, class_get

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)

app.include_router(register.router)
app.include_router(student.router)
app.include_router(attend.router)
app.include_router(class_post.router)
app.include_router(class_get.router)