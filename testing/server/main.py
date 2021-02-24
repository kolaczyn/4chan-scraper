from flask import Flask, render_template
import jinja2
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/<board>/thread/<thread>')
def thread(board, thread):
    try:
        return render_template(f'{board}/{thread}.html')
    except jinja2.exceptions.TemplateNotFound:
        return 'thread not found', 404
