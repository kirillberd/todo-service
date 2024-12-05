from dataclasses import dataclass
from domain.task import Task
from infrastructure.repositories.task_repository import TaskRepository
import logging

module_logger = logging.getLogger(__name__)

@dataclass
class TaskService:
    task_repository: TaskRepository


    def process_task(self, task: Task):
        try:
            module_logger.info(task)
            self.task_repository.add(task)
        except Exception as e:
            module_logger.info(f"Error adding task: {e}")
    
    def get_tasks_by_user_id(self, id: str):
        try:
            return self.task_repository.get_by_user_id(id)
        except Exception as e:
            module_logger.info("Error getting user tasks")