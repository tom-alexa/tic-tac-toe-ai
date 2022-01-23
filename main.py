from src.game import Game

PLAYERS = {
    "cross": {
        "name": "ahoj",
        "ai": True,
    },
    "circle": {
        "name": "čau",
        "ai": False,
    },
}


def main():
    game = Game(PLAYERS)
    game.run()


if __name__ == "__main__":
    main()
