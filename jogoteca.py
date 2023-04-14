from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Skyrim', 'RPG', 'PC')
jogo3 = Jogo('Slime Rancher', 'Indie', 'Xbox')
jogo4 = Jogo('GTA', 'Aventura', 'Xbox')
lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_novo = Jogo(nome, categoria, console)
    lista.append(jogo_novo)
    return redirect('/')

app.run(port=8080, debug=True)