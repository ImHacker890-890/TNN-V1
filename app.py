from main import Training
from flask import Flask
app = Flask(__name__)
@app.route('/ttnv1')
def ttnmain():
  train()
  return "You model is train!"
