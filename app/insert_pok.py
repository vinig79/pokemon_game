from app.models import Pokemon
from app import db
import requests

request_pokemon = requests.get('https://pokeapi.co/api/v2/pokedex/1/')
pokemons = request_pokemon.json()['pokemon_entries']
for x in range(len(pokemons)):
    pokemon = pokemons[x]
    rsp_1 = requests.get(pokemon['pokemon_species']['url'])
    rsp_2 = requests.get(rsp_1.json()["varieties"][0]["pokemon"]["url"])
    stats_json = rsp_2.json()['stats']
    rt = rsp_2.json()['types']
    tipos = []
    stats = []

    if len(rt) == 2:
        for x in rt:
            tipos.append(x['type']['name'])
    else:
        tipos.append((rt[0]['type']['name']))
        tipos.append(None)

    for stat in stats_json:
        stats.append(stat['base_stat'])

    with Session.begin() as session:
        pok = Pokemon(
            nome= pokemon['pokemon_species']['name'],
            tipo_1= tipos[0],
            tipo_2= tipos[1],
            hp= stats[0],
            atk= stats[1],
            defense= stats[2],
            atk_special= stats[3],
            special_defense= stats[4],
            speed= stats[5]
        )
        db.session.add(pok)
        db.session.commit()




