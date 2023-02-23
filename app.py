from flask import Flask, render_template, request, redirect, url_for, session
import mysql
import datetime

app = Flask(__name__)
app.secret_key = 'your secret key'
app.debug = True


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/indexNgo')
def indexNgo():
    return render_template('indexNgo.html')
    
@app.route('/indexVol')
def indexVol():
    return render_template('indexVol.html')

