from fastapi.routing import APIRouter
from infrastructure.container import Container
from domain.task import Task
from dependency_injector.wiring import inject, Provide
from applicaiton.services.task_service import TaskService
from fastapi import Depends
from infrastructure.api.auth.keycloak_auth import verify_token
import logging

module_logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/add")
@inject
def add_task(task: Task, task_service: TaskService = Depends(Provide[Container.task_service]), user_data: dict = Depends(verify_token) ):
    module_logger.info(task)
    task_service.process_task(Task.model_validate(task))
    return "Task recieved"


@router.get("/all")
@inject
def get_tasks(task_service: TaskService = Depends(Provide[Container.task_service]), user_data: dict = Depends(verify_token)):
    result =task_service.get_tasks_by_user_id(user_data["sid"])
    return result

