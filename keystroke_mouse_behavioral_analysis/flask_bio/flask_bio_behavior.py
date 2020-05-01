import pyautogui
import time
from flask import Flask, render_template, request, redirect, url_for

def requestResults(text):
    return 'test ' + text

app = Flask(__name__)

# render default webpage
@app.route('/')
def home():
    return render_template('bio_home.html')

# when the post method detect, then redirect to success function
@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        text = request.form['pwd']
        return redirect(url_for('success', text=text))

# get the data for the requested query
@app.route('/success/<text>')
def success(text):
    return "<xmp>" + str(requestResults(text)) + " </xmp> "

app.run(debug=True)