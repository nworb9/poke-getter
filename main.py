from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def howdy_world():
    return 'Howdy world!'
