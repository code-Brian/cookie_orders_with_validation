from flask_app import app
from flask_app.models.cookie import Cookie
from flask import Flask, render_template, redirect, request, session

@app.route('/cookies')
def r_cookies():
    print('Returing to cookies home page...')

    # get_all cookies from database function will go here

    return render_template('cookies.html')

@app.route('/cookies/new')
def r_cookies_new():
    print('Directing to create a new cookie order page...')

    return render_template('cookies_create.html')

# eventually this route will accept an incoming id and return results based upon order id
@app.route('/cookies/edit')
def r_cookies_edit():
    print('Directing to edit existing order page...')

    return render_template('cookies_update.html')