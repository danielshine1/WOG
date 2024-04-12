from flask import Flask, render_template
from Score import core_server

app = Flask(__name__)


@app.route('/')
def index():
    score = core_server()
    return render_template('index_scores.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
