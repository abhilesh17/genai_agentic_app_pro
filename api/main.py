
from fastapi import FastAPI, Request
from orchestrator.task_manager import TaskManager

app = FastAPI()
task_manager = TaskManager()

@app.post("/research")
async def research(request: Request):
    body = await request.json()
    query = body.get("query")
    result = task_manager.handle_task(query)
    return {"summary": result}
