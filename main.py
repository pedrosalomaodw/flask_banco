from flask import Flask, render_template, request
import mysql.connector

app = Flask('__name__')


@app.route("/")
@app.route("/cadastro", methods=['POST'])
def cadastro():
    #colhendo dados dos usuérios
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    botao = request.form.get('cadastrar_botao')
    
    #fazendo conexão
    dados_banco = mysql.connector.connect(host="endereço host do banco",user="nome de usuário",
                                        database="nome do banco de dados", port="porta onde o banco está rodando")
    cursor = dados_banco.cursor()

    inserir = f'''insert into nomedobanco.user(nome, email, senha)
            values ("{nome}", "{email}", "{senha}");'''
    cursor.execute(inserir)
    # o recurso do commit é usado para fazer uma atualização no banco de dados, assim trazendo os dados dos usuários
    dados_banco.commit()
    
    cursor.close()
    dados_banco.close()
    #arquivo da página principal do site
    return render_template("index.html")

    
app.run(debug=True)
