import requests
from model import Pokemon, Tipo

def crawler(db):
    request_pokemon = requests.get('https://pokeapi.co/api/v2/pokedex/1/')
    pokemons = request_pokemon.json()['pokemon_entries']
    if len(Pokemon.query.all()) == len(pokemons):
        return
    
    print("tipo")
    for x in range(len(pokemons)):
        if len(Tipo.query.all()) == 18:
            break
        pokemon = pokemons[x]
        rsp_1 = requests.get(pokemon['pokemon_species']['url'])
        rsp_2 = requests.get(rsp_1.json()["varieties"][0]["pokemon"]["url"])
        rt = rsp_2.json()['types']


        for t in rt:
            var = t['type']['name']
            tip = Tipo(tipo=var)
            cond = Tipo.query.filter_by(tipo=var).first()
            if cond == None :
                db.session.add(tip)
                db.session.commit()


    c = 1
    for x in range(len(pokemons)):
        pokemon = pokemons[x]
        rsp_1 = requests.get(pokemon['pokemon_species']['url'])
        rsp_2 = requests.get(rsp_1.json()["varieties"][0]["pokemon"]["url"])
        stats_json = rsp_2.json()['stats']
        rt = rsp_2.json()['types']
        stats = []
        print("pok", c)
        c+=1


        for stat in stats_json:
            stats.append(stat['base_stat'])

        pok = Pokemon(
            nome= pokemon['pokemon_species']['name'],
            hp= stats[0],
            atk= stats[1],
            defense= stats[2],
            atk_special= stats[3],
            special_defense= stats[4],
            speed= stats[5]
        )

        for t in rt:
            var = t['type']['name']
            tipo = Tipo.query.filter_by(tipo=var).all()
            pok.tipos.append(tipo[0])
        
        db.session.add(pok)
        db.session.commit()
