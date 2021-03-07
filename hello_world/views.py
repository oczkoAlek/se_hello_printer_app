from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request


moje_imie = "Ola"
msg = "Hello World!"


@app.route('/')
def index():
    if 'name' in request.args:
        moje_imie = request.args['name']
    else:
        moje_imie = 'Ola'
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
