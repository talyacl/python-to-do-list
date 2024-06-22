from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


tasks = {}


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    print(f"Task received: {task}")
    tasks[len(tasks) + 1] = task
    print(f"Tasks after adding: {tasks}")
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete(index):
    if index in tasks:
        del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
