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
@app.route('/cookies/<int:id>/edit')
def r_cookies_edit(id):
    print(f'Directing to edit existing order page at id:{id}...')

    data = {
        'id' : id
    }

    return render_template('cookies_update.html', cookie=Cookie.get_one(data))

@app.route('/cookies/save', methods=['POST'])
def f_cookies_save():
    print('Create new cookie order form submitted...')
    if not Cookie.validate_cookie(request.form):

        session['customer_name'] = request.form.get('customer_name')
        session['cookie_type'] = request.form.get('cookie_type')
        session['num_boxes'] = request.form.get('num_boxes')

        return redirect('/cookies/new')

    data = {
        'customer_name': request.form.get('customer_name'),
        'cookie_type' : request.form.get('cookie_type'),
        'num_boxes': request.form.get('num_boxes')
    }

    Cookie.save(data)

    session.clear()

    return redirect('/cookies')

@app.route('/cookies/update', methods=['POST'])
def f_cookies_update():

    if not Cookie.validate_update_cookie(request.form):
        session['id'] = request.form.get('id')
        session['customer_name'] = request.form.get('customer_name')
        session['cookie_type'] = request.form.get('cookie_type')
        session['num_boxes'] = request.form.get('num_boxes')

        return redirect(f"/cookies/{session['id']}/edit")

    data = {
        'id': request.form.get('id'),
        'customer_name': request.form.get('customer_name'),
        'cookie_type': request.form.get('cookie_type'),
        'num_boxes': request.form.get('num_boxes')
    }

    Cookie.update(data)

    return redirect('/cookies')