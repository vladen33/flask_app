from flask import jsonify, request

from . import app, db
from .models import Story


@app.route('/api/stories/', methods=['GET'])
def get_stories():
    stories = Story.query.all()
    stories_list = [story.to_dict() for story in stories]
    return jsonify(stories_list), 200


@app.route('/api/add_story/', methods=['POST'])
def add_story():
    data = request.get_json()
    story = Story()
    story.from_dict(data)
    db.session.add(story)
    db.session.commit()
    return jsonify(story.to_dict())