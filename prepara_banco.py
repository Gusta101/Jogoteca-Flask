import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='admin'
    )
    print("Você entrou no DataBase")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS jogoteca;")

cursor.execute("CREATE DATABASE jogoteca;")

cursor.execute("USE jogoteca;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
        CREATE TABLE jogos (
        id int(11) NOT NULL AUTO_INCREMENT,
        nome varchar(50) NOT NULL,
        categoria varchar(40) NOT NULL,
        console varchar(20) NOT NULL,
        PRIMARY KEY (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

TABLES['Usuarios'] = ('''
        CREATE TABLE usuarios (
        nome varchar(20) NOT NULL,
        nickname varchar(8) NOT NULL,
        senha varchar(100) NOT NULL,
        PRIMARY KEY (nickname)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print('Criando tabela {}'.format(tabela_nome), end='\n')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Já existe")
        else:
            print(err.msg)
    else:
        print("OK")

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Bruno Divino', 'BD', 'alohomora'),
    ('Gustavo Santos', 'Bolo', 'paozinho'),
    ('Guilherme Louro', 'Cake', 'python')
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' --------------- Usuários -------------- ')
for user in cursor.fetchall():
    print(user[1])