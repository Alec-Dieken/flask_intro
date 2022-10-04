from flask import Flask, request
from operations import *

app = Flask(__name__)

FUNCTIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<view>")
def math(view):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'''
    <html>
        <head>
        </head>
        <body>
            <h1>{FUNCTIONS[view](a, b)}</h1>
        </body
    </html>
    '''
