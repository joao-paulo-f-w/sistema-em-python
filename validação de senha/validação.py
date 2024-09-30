import sqlite3
from unittest import case


def inicializador_banco():
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
    id integer primary key autoincrement, 
    nome_usuario text unique not null, 
    senha text not null
    )
    ''')

    conn.commit()
    conn.close()

def registrar_usuario(nome_usuario, senha):
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO usuario (nome_usuario, senha) VALUES (?, ?)', (nome_usuario, senha))
        conn.commit()
        return "registro concluido com suscesso"
    except sqlite3.IntegrityError:
        return "usuario ja existente"
    finally:
        conn.close()

def login_usuario(nome_usuario, senha):
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuario  where nome_usuario = ? and senha = ?',(nome_usuario, senha))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return "login bem-sucedido"
    else:
        return "login falhou: nome de usuario ou senha incorretos."

inicializador_banco()

def conta (validacao):
    match validacao:
        case 'registro':
            nome_usuario = input('Digite seu nome de usuário: ')
            senha = input('Digite a senha: ')
            return registrar_usuario(nome_usuario, senha)  # Corrigido a indentação aqui
        case 'login':
            nome_usuario = input('Digite seu nome de usuário: ')
            senha = input('Digite a senha: ')
            return login_usuario(nome_usuario, senha)  # Corrigido a indentação aqui
        case _:
            return "Opção inválida"

inicio = input('digite "login" ou "registro": ').lower()
resultado = conta(inicio)
print(resultado)