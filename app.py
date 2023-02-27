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

# This code implements a Flask application with multiple routes for user login and logout.
# Route for volunteer login. It will receive a POST request from the login form, 
# extract the username and password, and validate the credentials against the 
# 'Students' table in a SQl database. If the credentials are valid, it will 
# store the user information in session variables and redirect the user to the 
# index page. If the credentials are invalid, it will display an error message.

@app.route('/loginVolunteer', methods=['GET', 'POST'])
def loginVolunteer():
    # Message to be displayed on the login page
    msg = ''
    # Check if the request is a POST request and the form has the required fields
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Extract the form data
        username = request.form['username']
        password = request.form['password']
        # Connect to the database
   


