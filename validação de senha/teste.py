import sqlite3

def inicializador_banco():
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome_usuario TEXT UNIQUE NOT NULL, 
    senha TEXT NOT NULL
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
        return "Registro concluído com sucesso"
    except sqlite3.IntegrityError:
        return "Usuário já existente"
    finally:
        conn.close()

def login_usuario(nome_usuario, senha):
    conn = sqlite3.connect('usuario.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuario WHERE nome_usuario = ? AND senha = ?', (nome_usuario, senha))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return "Login bem-sucedido"
    else:
        return "Login falhou: nome de usuário ou senha incorretos."

# Inicializar o banco de dados
inicializador_banco()

def conta(validacao):
    match validacao:
        case 'registro':
            nome_usuario = input('Digite seu nome de usuário: ')
            senha = input('Digite a senha: ')
            return registrar_usuario(nome_usuario, senha)
        case 'login':
            nome_usuario = input('Digite seu nome de usuário: ')
            senha = input('Digite a senha: ')
            return login_usuario(nome_usuario, senha)
        case _:
            return "Opção inválida"

# Início do programa
inicio = input('Digite "login" ou "registro": ').lower()
resultado = conta(inicio)
print(resultado)
