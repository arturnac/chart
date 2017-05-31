from flask import Flask, render_template
from random import sample	

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('chart.html')

@app.route('/data')
def data():
	return jsonify ({'results' : sample(range(1,10))})

if __name__ == '__main__':
  app.run(debug=True)
