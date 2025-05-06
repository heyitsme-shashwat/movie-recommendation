from flask import Flask, render_template
import json

app = Flask(__name__)

# Load movies from the JSON file
with open('movie_data_100.json') as f:
    movies = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
