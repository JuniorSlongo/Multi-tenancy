from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Função para conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname="nome_db",
            user="postgres",
            password="*******",
            host="localhost",
            port="5432"
        )
        print("Conexão ao banco de dados estabelecida.")
        return conn

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

# Rota para exibir os usuários cadastrados
@app.route('/')
def index():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios;")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

# Rota para adicionar um novo usuário
@app.route('/adicionar', methods=['POST'])
def adicionar_usuario():
    conn = conectar_banco()
    cursor = conn.cursor()
    nome = request.form['nome']
    cursor.execute("INSERT INTO usuarios (nome) VALUES (%s)", (nome,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
