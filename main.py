from flask import Flask, render_template
import random

app = Flask(__name__, template_folder='templates')

# List of meme URLs
memes = [
    "https://cdn.memes.com/up/33012541656404504/i/1623463245157.jpg",
    "https://pbs.twimg.com/media/FaWsxXmXgAAm6s0?format=jpg&name=900x900",
    "https://pbs.twimg.com/media/D1apUfbX0AAzCul?format=jpg&name=900x900",
    "https://pbs.twimg.com/media/DrrLIN3XgAEiHT9?format=jpg&name=900x900",
    "https://pbs.twimg.com/media/DrRbLc3WwAABjJK?format=jpg&name=900x900",
    "https://pbs.twimg.com/media/DrB-aMwX0AElAK8?format=jpg&name=900x900",
    "https://pbs.twimg.com/media/Dpa-nNsXgAA8jPb?format=jpg&name=900x900"

]

@app.route('/')
def index():
    # Select a random joke and meme from the lists
    meme = random.choice(memes)
    return render_template('index.html', meme=meme)

@app.route('/hello', methods=["GET"])
def hello():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
