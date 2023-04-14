from flask import Flask, render_template, request, redirect, session, flash

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
app.secret_key = 'paçoca'

# /lista.html   --> titulo (Título da página)
#                   jogos (Lista de objetos Jogo a serem listados)
# /novo.html    --> titulo (Título da página)

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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha'] == 'alohomora':
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(port=8080, debug=True)