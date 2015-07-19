from bottle import(run, template, route, post, get, request)

import db

def menu_params():
    return{
    'name':request

    }

@route('/')
def index():
    return template('kondate')

@get('/new')
def new():
    return template('kondate_new')

@post('/new')
def newdata():
    db.create_menu()

run(host='localhost', port=8080)