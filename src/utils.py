import requests
import shutil
import os

TYPE_ENDPOINT = 'https://pokeapi.co/api/v2/type/'
HABITAT_ENDPOINT = 'https://pokeapi.co/api/v2/pokemon-habitat/'
MEDIA_DIR = "./media/"


def get_sprite(pokemon_url: str):
    """
    https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    """
    print(f'Loading results for {pokemon_url}')
    pokemon_response = requests.get(pokemon_url)
    if pokemon_response.status_code == 200:
        pokemon_info = pokemon_response.json()
        sprite_path = f"{MEDIA_DIR}{pokemon_info['name']}.png"
        print(f"Downloading file for {pokemon_info['name']}")
        sprite_image = requests.get(pokemon_info['sprites']['front_default']).content
        with open(sprite_path, "wb+") as img:
            img.write(sprite_image)
        return sprite_path
    else:
        Exception(f'No sprite found for this pokemon at url {pokemon_url}')


def get_pokemon_by_type(type: str):
    response = requests.get(TYPE_ENDPOINT + type + '/')
    if response.status_code == 200:
        pokemon_list = response.json()['pokemon']
    else:
        Exception('No Pokemon found for this type -- confirm the type is valid!')
    return unnest_type_pokemon(pokemon_list)


def get_pokemon_by_habitat(habitat: str):
    response = requests.get(HABITAT_ENDPOINT + habitat + '/')
    if response.status_code == 200:
        pokemon_list = response.json()['pokemon_species']
    else:
        Exception('No Pokemon found for this habitat -- confirm the habitat is valid!')
    return unnest_habitat_pokemon(pokemon_list)


def unnest_type_pokemon(pokemon_list: list):
    cleaned_pokemon = [
        {'name': poke['pokemon']['name'], 'endpoint': poke['pokemon']['url']} for poke in pokemon_list
    ]
    return cleaned_pokemon


def unnest_habitat_pokemon(pokemon_list: list):
    cleaned_pokemon = [
        {'name': poke['name'], 'endpoint': poke['url'].replace('pokemon-species', 'pokemon')} for poke in pokemon_list
    ]
    return cleaned_pokemon


def filter_pokemon_by_type_and_habitat(type_pokemon: list, habitat_pokemon: list):
    if habitat_pokemon and type_pokemon:
        final_pokemon = [poke for poke in type_pokemon if poke in habitat_pokemon]
    elif habitat_pokemon:
        final_pokemon = habitat_pokemon
    elif type_pokemon:
        final_pokemon = type_pokemon
    return [{'name': poke['name'], 'sprite': get_sprite(poke['endpoint'])} for poke in final_pokemon]


def catch_pokemon(habitat=None, type=None):
    if not os.path.exists(MEDIA_DIR):
        os.makedirs(MEDIA_DIR)
    type_pokemon = get_pokemon_by_type(type) if type else []
    habitat_pokemon = get_pokemon_by_habitat(habitat) if habitat else []
    final_pokemon = filter_pokemon_by_type_and_habitat(type_pokemon=type_pokemon, habitat_pokemon=habitat_pokemon)
    return {
        "count": len(final_pokemon),
        "pokemon": final_pokemon
    }
