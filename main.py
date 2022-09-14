from data import retorno
from player import Player
from pokemon import Pokemon, Status

vini = Player('Vinicius')
for x in range(2):
    stats1, name1, tipo1 = retorno()
    status1 = Status(hp=stats1[0],attack=stats1[1],defense=stats1[2],speed=stats1[3])
    pok = Pokemon(nome=name1,tipo=tipo1,status=status1)
    vini.pokemon.append(pok)

for x in vini.pokemon:
    print(x.nome)
    print(x.tipo)
    print(f"atk = {x.status.atk}")
    print(f"defesa = {x.status.defesa}")
    print(f"speed = {x.status.speed}")
    print(f"hp = {x.status.hp}")
    print("=-"*20)
