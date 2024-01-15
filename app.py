import datetime
import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('index.html', data=data)


@app.route('/page2')
def page2():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('page2.html', data=data)


@app.route('/page3')
def page3():
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('page3.html', data=data)


my_skills = [
    'Python',
    'Django',
    'HTML, CSS',
    'JavaScript',
    'Flask',
    'SQL',
    'Git',
]


@app.route('/skills', defaults={'id': None})
@app.route('/skills/<int:id>')
def skills(id):
    data = [os.name, datetime.datetime.now(), request.user_agent]
    return render_template('skills.html', skills=my_skills, id=id, data=data)



if __name__ == 'main':
    app.run(debug=True)
