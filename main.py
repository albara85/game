from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    return jsonify({'computer_choice': computer_choice, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
