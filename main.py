from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def howdy_world():
    return 'Howdy world!'


@app.route('/pokemon/catch', methods=['GET'])
def catch_pokemon():
    if request.args.get('type'):
        pokemon_type = request.args.get('type')
    if request.args.get('habitat_name'):
        pokemon_habitat = request.args.get('habitat_name')
    if request.args.get('habitat_id'):
        pokemon_habitat = request.args.get('habitat_id')

    return pokemon_habitat
