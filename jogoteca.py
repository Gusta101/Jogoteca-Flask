from flask import Flask, render_template, request, redirect, session, flash, url_for

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

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario('Gustavo Santos', 'Gustas', 'gato')
usuario2 = Usuario('Bruno Divino', 'Brunao', 'alohomora')
usuario3 = Usuario('Camila Ferreira', 'Mila', 'paozinho')

usuarios = { usuario1.nickname : usuario1, usuario2.nickname : usuario2, usuario3.nickname : usuario3 }

app = Flask(__name__)
app.secret_key = 'paçoca'

# /lista.html   --> titulo (Título da página)
#                   jogos (Lista de objetos Jogo a serem listados)
# /novo.html    --> titulo (Título da página)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
    #if not session['usuario_logado']:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_novo = Jogo(nome, categoria, console)
    lista.append(jogo_novo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(port=8080, debug=True)