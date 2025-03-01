from random import randint

from flask import redirect, render_template, url_for

from . import app, db
from .forms import StoryForm
from .models import Story


@app.route('/')
def index_view():
    stories = Story.query.all()
    return render_template('stories.html', stories=stories)


@app.route('/add', methods=['GET', 'POST'])
def add_view():
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(
            title=form.title.data,
            text=form.text.data
        )
        db.session.add(story)
        db.session.commit()
        return redirect(url_for('index_view'))
    return render_template('add.html', form=form)


@app.route('/story')
def random_story_view():
    stories_count = Story.query.count()
    random_story = Story.query.get_or_404(  # На всякий
        randint(1, stories_count)
    )
    return render_template('random.html', story=random_story)