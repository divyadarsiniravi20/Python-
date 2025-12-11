
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-key'  # for flash messages

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Text, nullable=False, default='Pending')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description or '',
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }


# Create tables at startup (Flask 2.3+/3.x compatible)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    if not title:
        flash('Title is required.', 'danger')
        return redirect(url_for('index'))
    task = Task(title=title, description=description, status='Pending')
    db.session.add(task)
    db.session.commit()
    flash('Task added successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        if not title:
            flash('Title is required.', 'danger')
            return redirect(url_for('edit_task', task_id=task_id))
        task.title = title
        task.description = description
        db.session.commit()
        flash('Task updated successfully.', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Completed'
    db.session.commit()
    flash('Task marked as completed.', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted.', 'info')
    return redirect(url_for('index'))

# --- Simple JSON API for dynamic UI updates ---
@app.route('/api/tasks', methods=['GET'])
def api_list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([t.to_dict() for t in tasks])

@app.route('/api/tasks/<int:task_id>/complete', methods=['POST'])
def api_complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.status = 'Completed'
    db.session.commit()
    return jsonify({'success': True, 'task': task.to_dict()})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def api_update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json(force=True) or {}
    title = (data.get('title') or '').strip()
    description = (data.get('description') or '').strip()
    if not title:
        return jsonify({'success': False, 'error': 'Title is required'}), 400
    task.title = title
    task.description = description
    db.session.commit()
    return jsonify({'success': True, 'task': task.to_dict()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


#############################

# from flask import Flask, render_template, request, redirect, url_for
# from datetime import datetime
#
# app = Flask(__name__)
#
# # Temporary in-memory storage (list)
# tasks = []  # [{id, title, description, status, created_at}]
#
# # Auto increment ID
# task_id_counter = 1
#
#
# @app.route("/")
# def index():
#     return render_template("index.html", tasks=tasks)
#
#
# @app.route("/add", methods=["POST"])
# def add_task():
#     global task_id_counter
#     title = request.form["title"]
#     description = request.form.get("description", "")
#
#     task = {
#         "id": task_id_counter,
#         "title": title,
#         "description": description,
#         "status": "Pending",
#         "created_at": datetime.now()
#     }
#
#     tasks.append(task)
#     task_id_counter += 1
#     return redirect(url_for("index"))
#
#
# @app.route("/delete/<int:task_id>")
# def delete_task(task_id):
#     global tasks
#     tasks = [t for t in tasks if t["id"] != task_id]
#     return redirect(url_for("index"))
#
#
# @app.route("/complete/<int:task_id>")
# def complete_task(task_id):
#     for task in tasks:
#         if task["id"] == task_id:
#             task["status"] = "Completed"
#             break
#     return redirect(url_for("index"))
#
#
# @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
# def edit_task(task_id):
#     for task in tasks:
#         if task["id"] == task_id:
#             if request.method == "POST":
#                 task["title"] = request.form["title"]
#                 task["description"] = request.form.get("description", "")
#                 return redirect(url_for("index"))
#             return render_template("index.html", edit_task=task, tasks=tasks)
#
#     return redirect(url_for("index"))
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


