import pytest
from app import app, db  # Import the Flask app and db from app.py
from src.services.task_service import TaskService


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


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
