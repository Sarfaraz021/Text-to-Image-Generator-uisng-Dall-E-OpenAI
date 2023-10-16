from flask import Flask, jsonify
from config import key
import openai
from flask import render_template

openai.api_key = key

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )


@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=9, size="256x256")
  print(response)
  return jsonify(response)


app.run(host='0.0.0.0', port=81)
