from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db = SQLAlchemy(app)

# 📌 Модель данных для задач
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# 📌 Создание таблицы (только при первом запуске)
with app.app_context():
    db.create_all()

# 📌 Получение всех задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "task": t.task, "done": t.done} for t in tasks])

# 📌 Добавление новой задачи
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(task=data["task"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Задача додана!"}), 201

# 📌 Обновление задачи
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Задача не знайдена!"}), 404
    data = request.get_json()
    task.task = data.get("task", task.task)
    task.done = data.get("done", task.done)
    db.session.commit()
    return jsonify({"message": "Задача оновлена!"})

# 📌 Удаление задачи
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Задача не знайдена!"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Задача видалена!"})

if __name__ == '__main__':
    app.run(debug=True)
