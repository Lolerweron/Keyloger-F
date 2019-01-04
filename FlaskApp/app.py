from flask import Flask
app = Flask(__name__)
from flask import Flask, render_template


@app.route("/")
def test():
    return render_template('index.html')

app.run(debug=True)