from bottle import(run, template, route, post, get, request)

import db

def menu_params():
    return{
    'name':request

    }

@route('/')
def new():
    return 'a'

@get('/new')
def index():
    return template('kondate')

@post('/new')
def newdata():
    db.create_menu()

run(host='localhost', port=8080)