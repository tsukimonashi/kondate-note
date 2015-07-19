from bottle import(run, template, route, post, get, request, redirect)

import db

def menu_params():
    return{
    'name':request

    }

@route('/')
def index():
    return template('kondate',menus=db.create_fetchall())

@get('/menus/new')
def new():
    return template('kondate_new')

@post('/menus/new')
def create():
    name = request.forms.name
    kcal = request.forms.kcal
    image = request.forms.image
    db.create_menu(name, kcal, image)
    return redirect('/')

run(host='localhost', port=8080, debug=True, reloader=True)
