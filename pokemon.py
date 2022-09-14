import requests
from random import randint

class Pokemon:
    def __init__(self, nome, tipo, status):
        self.nome: str = nome
        self.tipo: str = tipo
        self.status: Status = status


class Status:
    def __init__(self, hp, attack, defense, speed):
        self.atk: int = attack
        self.defesa: int = defense
        self.speed: int = speed
        self.hp: int = hp


