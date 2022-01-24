#! /usr/bin/python3

import random
from src.game import Game

NAMES = ["Johny", "Jacob", "Lukas", "Tom", "George", "Carl"]


def main():
    players = {"cross": {"ai": True, "name": random.choice(NAMES)}, "circle": {"ai": True, "name": random.choice(NAMES)}}
    first = input("Player's one name [no input means AI]: ")
    if first:
        players["cross"]["name"] = first
        players["cross"]["ai"] = False
    second = input("Player's two name [no input means AI]: ")
    if second:
        players["circle"]["name"] = second
        players["circle"]["ai"] = False
    game = Game(players)
    game.run()


if __name__ == "__main__":
    main()
