from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

from queue import add_task, get_queue_size


app = FastAPI(
    title="Distributed Task Scheduler",
    description="Fault-tolerant distributed task scheduling system",
    version="1.0"
)


class TaskRequest(BaseModel):
    command: str
    priority: int = 1


@app.get("/")
def home():

    return {
        "system": "Distributed Task Scheduler",
        "status": "running"
    }


@app.post("/tasks")
def create_task(task_request: TaskRequest):

    task_id = str(uuid4())

    task = {
        "task_id": task_id,
        "command": task_request.command,
        "priority": task_request.priority,
        "status": "queued"
    }

    add_task(task)

    return {
        "message": "Task added to queue",
        "task": task
    }


@app.get("/queue")
def queue_status():

    return {
        "queue": "task_queue",
        "tasks_waiting": get_queue_size()
    }