from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

# Dummy tasks list
tasks = [
    {"id": 1, "title": "Buy milk", "description": "Get fresh milk from Tesco"},
    {"id": 2, "title": "Study Arabic", "description": "Revise vocabulary"},
    {"id": 3, "title": "Complete Flask App", "description": "Finish the tutorial"},
]

@main.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/task/<int:task_id>")
def task_detail(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    return render_template("task_detail.html", task=task)

@main.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if request.method == "POST":
        task["title"] = request.form["title"]
        task["description"] = request.form["description"]
        return redirect(url_for("main.task_detail", task_id=task_id))

    return render_template("edit_task.html", task=task)

@main.route("/task/new", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]

        # create new ID (max id + 1)
        new_id = max(t["id"] for t in tasks) + 1 if tasks else 1

        new_task = {
            "id": new_id,
            "title": title,
            "description": description,
        }

        tasks.append(new_task)

        return redirect(url_for("main.index"))

    return render_template("new_task.html")


@main.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("main.index"))
