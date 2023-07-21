from flask_app import app
from flask import render_template,redirect,request, session
import random
from flask_app.models import words

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/question')
def findword():
    
    return render_template("quess.html", hint = words.random_word.hint())

@app.route('/generate', methods = ['GET'])
def generate():
    filename = "flask_app/static/wordsto.txt"
    list = []
    with open(filename) as diary_file:
        for line in diary_file:
            if (len(line) == 6) :
                list.append(line)

    selector = random.choice(list)
    data = {
        "theword" :selector
    }
    words.random_word.word_generator(data)
    return redirect("/question")

@app.route("/score")
def score():
    return render_template("final.html")

@app.route('/send', methods = ['POST'])
def send():
    data = {
    "first" : request.form["first"],
    'second' : request.form["second"],
    'third' : request.form["third"],
    'fourth' : request.form['fourth'],
    'five' : request.form['five']
    }
    words.random_word.does_it_match(data)
    return redirect("/score")
