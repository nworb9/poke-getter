from flask import Flask, request, jsonify
from src.utils import catch_pokemon
import json


app = Flask(__name__)


@app.route('/')
def howdy_world():
    return 'Howdy world!'


@app.route('/pokemon/catch', methods=['GET'])
def catch_them_all():
    if request.args.get('type'):
        pokemon_type = request.args.get('type')
    if request.args.get('habitat_name'):
        pokemon_habitat = request.args.get('habitat_name')
    if request.args.get('habitat_id'):
        pokemon_habitat = request.args.get('habitat_id')
    pokemon_response = catch_pokemon(habitat=pokemon_habitat, type=pokemon_type)
    return jsonify(pokemon_response)
