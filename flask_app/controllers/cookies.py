from flask_app import app
from flask_app.models.cookie import Cookie
from flask import Flask, render_template, redirect, request, session

@app.route('/cookies')
def r_cookies():
    print('Returing to cookies home page...')

    return render_template('cookies.html', orders=Cookie.get_all())

@app.route('/cookies/new')
def r_cookies_new():
    print('Directing to create a new cookie order page...')

    return render_template('cookies_create.html')

# eventually this route will accept an incoming id and return results based upon order id
@app.route('/cookies/edit')
def r_cookies_edit():
    print('Directing to edit existing order page...')

    return render_template('cookies_update.html')

@app.route('/cookies/save', methods=['POST'])
def f_cookies_save():
    print('Create new cookie order form submitted...')
    if not Cookie.validate_cookie(request.form):

        session['customer_name'] = request.form.get('customer_name')
        session['cookie_type'] = request.form.get('cookie_type')
        session['num_boxes'] = request.form.get('num_boxes')

        return redirect('/cookies/new')

    session.clear()

    return redirect('/cookies')