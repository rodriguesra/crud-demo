from flask import request, jsonify, render_template
from flask.views import MethodView

from src.models.task import Task
from src.services.task_service import TaskService


class TaskController(MethodView):
    @staticmethod
    def get(id=None):
        if id is None:
            tasks = Task.query.all()
            return render_template('tasks.html', tasks=tasks)
        else:
            task = Task.query.get(id)
            return render_template('task.html', task=task)

    @staticmethod
    def post():
        title = request.json.get('title')
        description = request.json.get('description')
        completed = request.json.get('completed', False)  # Default to False if not provided
        task = TaskService.create_task(title, description, completed)
        return jsonify(task.to_dict()), 201

    @staticmethod
    def put(id):
        title = request.json.get('title')
        description = request.json.get('description')
        completed = request.json.get('completed')
        task = TaskService.update_task(id, title, description, completed)
        return jsonify(task.to_dict())

    @staticmethod
    def delete(id):
        TaskService.delete_task(id)
        return '', 204
