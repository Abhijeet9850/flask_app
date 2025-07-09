from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Read MongoDB URI from environment
mongo_uri = os.getenv('MONGO_URL')
client = MongoClient(mongo_uri)
db = client['mydatabase']
collection = db['mycollection']

@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            if not name or not email:
                raise Exception("Both fields are required.")
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except Exception as e:
            error = str(e)
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
