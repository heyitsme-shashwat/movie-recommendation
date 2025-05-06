from flask import Flask, render_template
import json

app = Flask(__name__)

# Load movies from the JSON file
with open('movie_data_100.json') as f:
    movies = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

