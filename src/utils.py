import requests
import shutil

TYPE_ENDPOINT = 'https://pokeapi.co/api/v2/type/'
HABITAT_ENDPOINT = 'https://pokeapi.co/api/v2/pokemon-habitat/'


def get_sprite(pokemon_url: str):
    """
    https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests
    """
    print(f'Loading results for {pokemon_url}')
    pokemon_response = requests.get(pokemon_url)
    if pokemon_response.status_code == 200:
        pokemon_info = pokemon_response.json()
        sprite_path = f"../media/{pokemon_info['name']}.png"
        print(f"downloading file for {pokemon_info['name']}")
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
    return pokemon_list


def get_pokemon_by_habitat(habitat: str):
    response = requests.get(HABITAT_ENDPOINT + habitat + '/')
    if response.status_code == 200:
        pokemon_list = response.json()['pokemon_species']
    else:
        Exception('No Pokemon found for this habitat -- confirm the habitat is valid!')
    return pokemon_list


def unnest_type_pokemon(pokemon_list: list):
    cleaned_pokemon = [
        {'name': poke['pokemon']['name'], 'endpoint': poke['pokemon']['url']} for poke in pokemon_list
    ]
    return cleaned_pokemon


def unnest_habitat_pokemon(pokemon_list: list):
    cleaned_pokemon = [
        {'name': poke['name'], 'endpoint': poke['url']} for poke in pokemon_list
    ]
    return cleaned_pokemon
