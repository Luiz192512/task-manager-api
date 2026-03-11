from fastapi import APIRouter

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks