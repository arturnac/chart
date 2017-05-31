from flask import Flask, render_template
from flask import jsonify	
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017'

mongo = PyMongo(app)

@app.route('/')
def index():
  return render_template('chart.html')

@app.route('/data')
def data():
	chart = mongo.db.test

//This has to change somehow
	
	result = chart.find_one({'name' : 'Chart'})

	return jsonify ({'results' : result['values']})

if __name__ == '__main__':
  app.run(debug=True)