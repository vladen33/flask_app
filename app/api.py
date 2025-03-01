from flask import jsonify, request

from . import app, db
from .models import Story


@app.route('/api/stories/', methods=['GET'])
def get_stories():
    # ...
    pass


@app.route('/api/add_story/', methods=['POST'])
def add_story():
    # ...
    pass