import requests
from random import randint
def retorno():
    request_pokemon = requests.get('http://pokeapi.co/api/v2/pokemon/')
    pokemons = request_pokemon.json()['results']
    pokemon = pokemons[randint(0,len(pokemons))]
    request_stats = requests.get(pokemon['url'])
    stats_json = request_stats.json()['stats']
    tipo = request_stats.json()['types'][0]['type']['name']
    stats = []
    for stat in stats_json:
        if stat['stat']['name'] == 'special-attack' or stat['stat']['name'] == 'special-defense':
            continue
        stats.append(stat['base_stat'])
    return stats, pokemon['name'], tipo
