from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.json.ensure_ascii = False
db = SQLAlchemy(app)


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route('/')
def index_view():
    stories = Story.query.all()
    return jsonify([{str(story.id): story.text} for story in stories])


@app.route('/add')
def add_view():
    return 'Это страница для добавления рассказа'


@app.route('/story')
def random_story_view():
    return 'Это страница со случайным рассказом'