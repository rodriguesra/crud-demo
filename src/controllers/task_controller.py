from flask import request, jsonify
from flask.views import MethodView
from src.services.task_service import TaskService


class TaskController(MethodView):
    @staticmethod
    def get(id=None):
        if id:
            task = TaskService.get_task_by_id(id)
            return jsonify(task.to_dict())
        else:
            tasks = TaskService.get_all_tasks()
            return jsonify([task.to_dict() for task in tasks])

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
