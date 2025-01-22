from flask import Flask, render_template
from modules.roblox_data import get_visits

app = Flask(__name__)

@app.route("/")
def index():
    game_id = "696347899"
    visits = get_visits(game_id)
    return render_template("index.html", visits=visits)

if __name__ == "__main__":
    app.run(debug=True)
