from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')


app.run()
