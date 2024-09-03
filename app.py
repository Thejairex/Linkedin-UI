from flask import Flask, render_template

from app.db import Jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs')
def jobs():
    jobs = Jobs('static/db/jobs.db').select()
    return render_template('jobs.html', jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)