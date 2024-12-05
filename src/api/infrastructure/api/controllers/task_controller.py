from fastapi.routing import APIRouter
from infrastructure.container import Container
from domain.task import Task
from dependency_injector.wiring import inject, Provide
from applicaiton.services.task_service import TaskService
from fastapi import Depends
import logging

module_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/add")
@inject
def add_task(task: Task, task_service: TaskService = Depends(Provide[Container.task_service])):
    module_logger.info(task)
    task_service.process_task(Task.model_validate(task))
    return "Task recieved"


