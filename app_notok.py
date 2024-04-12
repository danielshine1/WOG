from flask import Flask, render_template, request
from Live import load_game

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    # Simulate user input or obtain it from a web form
    user_choice = int(request.form.get('user_choice', 1))
    difficulty_level = int(request.form.get('difficulty_level', 1))

    # Call load_game with simulated or obtained user input
    user_choice, difficulty_level = load_game()
    game_result = f"User choice: {user_choice}, Difficulty level: {difficulty_level}"

    # Pass the captured result to result.html
    return render_template('result.html', game_result=game_result)


if __name__ == '__main__':
    app.run(debug=False, threaded=True)

