from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/orientation.html")
def orientation():
	return render_template("orientation.html")



app.run(host="0.0.0.0", port=5000)