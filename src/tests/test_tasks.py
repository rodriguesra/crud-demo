import pytest
from flask import Flask
from src.models.task import db
from src.services.task_service import TaskService


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.init_app(app)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_get_all_tasks(client):
    # Arrange
    TaskService.create_task('Test Task', 'This is a test task')
    # Act
    response = client.get('/tasks')
    # Assert
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['title'] == 'Test Task'
    assert response.json[0]['description'] == 'This is a test task'
    assert response.json[0]['completed'] is False
