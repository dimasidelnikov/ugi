from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks.append({"id": len(tasks) + 1, "task": data["task"]})
    return jsonify({"message": "Task added"}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    app.run(debug=True)
