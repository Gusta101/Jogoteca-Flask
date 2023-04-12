from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Skyrim', 'RPG', 'PC')
    jogo3 = Jogo('Slime Rancher', 'Indie', 'Xbox')
    jogo4 = Jogo('GTA', 'Aventura', 'Xbox')
    lista = [jogo1, jogo2, jogo3, jogo4]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(port=8080)