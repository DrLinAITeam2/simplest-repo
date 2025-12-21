from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from states import TaskStatus, ALLOWED, can_transition, transition
import logging
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

app = FastAPI(title="Task Status API", description="API for task status transitions")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransitionRequest(BaseModel):
    current: str
    target: str

@app.get("/statuses")
def get_statuses():
    """Get all possible task statuses."""
    logger.info("Requested all statuses")
    return [status.value for status in TaskStatus]

@app.get("/transitions/{status}")
def get_transitions(status: str):
    """Get allowed transitions for a given status."""
    logger.info(f"Requested transitions for status: {status}")
    try:
        task_status = TaskStatus(status)
        allowed = ALLOWED.get(task_status, set())
        logger.info(f"Allowed transitions for {status}: {[s.value for s in allowed]}")
        return [s.value for s in allowed]
    except ValueError:
        logger.warning(f"Invalid status requested: {status}")
        raise HTTPException(status_code=400, detail="Invalid status")

@app.post("/transition")
def do_transition(request: TransitionRequest):
    """Attempt to transition from current to target status."""
    logger.info(f"Attempting transition from {request.current} to {request.target}")
    try:
        current = TaskStatus(request.current)
        target = TaskStatus(request.target)
        new_status = transition(current, target)
        logger.info(f"Transition successful: {request.current} -> {new_status.value}")
        return {"success": True, "new_status": new_status.value}
    except ValueError as e:
        logger.warning(f"Transition failed: {request.current} -> {request.target} - {str(e)}")
        return {"success": False, "error": str(e)}