from flask import Flask, request, jsonify
from models.taks import Task

app = Flask(__name__)

tasks = []
taks_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global taks_id_control
    data = request.get_json()
    new_task = Task(id=taks_id_control, title=data['title'], description=data.get("description", ""))
    taks_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)