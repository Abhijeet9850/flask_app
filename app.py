from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas setup
client = MongoClient("http://127.0.0.1:5000/")  # Replace with your URI
db = client['userData']
collection = db['app']

@app.route('/api', methods=['GET'])
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            data = {"name": name, "email": email}
            collection.insert_one(data)
            return redirect(url_for('success'))
        except Exception as e:
            error = str(e)
    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
