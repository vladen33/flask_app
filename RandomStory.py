from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_view():
    return 'Это главная страница!'

@app.route('/add')
def add_view():
    return 'Это страница для добавления рассказа'

@app.route('/story')
def story_view():
    return 'Это страница со случайным рассказом'

if __name__ == '__main__':
    app.run()