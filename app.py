from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Setup Jenkins", "status": "done"},
    {"id": 2, "title": "Build Docker image", "status": "in progress"}
]

@app.route("/")
def home():
    return jsonify({
        "message": "Task Management API",
        "endpoints": ["/tasks", "/tasks (POST)"]
    })

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "status": "pending"
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
