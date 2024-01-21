from flask import Flask
from src.controllers.task_controller import TaskController
from src.models.task import db

app = Flask(__name__)

# Define the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/tasks.db'

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Create all the tables
with app.app_context():
    db.create_all()

task_view = TaskController.as_view('task_api')

app.add_url_rule('/tasks', defaults={'id': None},
                 view_func=task_view, methods=['GET', ])
app.add_url_rule('/tasks', view_func=task_view, methods=['POST', ])
app.add_url_rule('/tasks/<int:id>', view_func=task_view,
                 methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run()
