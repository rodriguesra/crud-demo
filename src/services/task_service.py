from src.models.task import Task
from src.models.task import db


class TaskService:
    @staticmethod
    def get_all_tasks():
        return Task.query.all()

    @staticmethod
    def get_task_by_id(id):
        return Task.query.get(id)

    @staticmethod
    def create_task(title, description, completed=False):
        new_task = Task(title=title, description=description, completed=completed)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def update_task(id, title=None, description=None, completed=None):
        task = Task.query.get(id)
        if title:
            task.title = title
        if description:
            task.description = description
        if completed is not None:
            task.completed = completed
        db.session.commit()
        return task

    @staticmethod
    def delete_task(id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
