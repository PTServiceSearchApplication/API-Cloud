import numpy
import scikit-surprise
import numpy cython
import pandas
import nltk

from flask import Flask
app = Flask(__name__)

# Server test functions
@app.route("/")
def hello():
  return "<h1 style='color:blue'>Server Test!</h1>"

# Machine Learning recommendation
@app.route("/recommendation", methods=["GET"])
def recommendation():
  g = open('ml path.ipynb')
  suggestion = json.load(g)
  return suggestion

# Update User Profile
@app.route("/profile", methods=["POST", "PUT", "GET"]
def profile():
    f = open('database.json')
    data = json.load(f)
    return data
           
if __name__ == "__main__":
app.run(host='0.0.0.0')
