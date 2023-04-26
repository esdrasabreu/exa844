from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
app.secret_key = 'chave-secreta'

@app.route('/')
def index():
    data_envio = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    return render_template('index.html', data_envio=data_envio)

@app.route('/processa', methods=['POST'])
def processa():
    nome = request.form['nome']
    data_envio = request.form['data_envio']
    session['nome'] = nome
    session['data_envio'] = data_envio
    return render_template('perfil.html', mensagem=f"Nome: {nome}<br />Data de envio: {data_envio}")

@app.route('/perfil')
def perfil():
    nome = session.get('nome')
    data_envio = session.get('data_envio')
    if nome is None:
        mensagem = "Erro: Nenhum nome foi armazenado na sessão"
    else:
        mensagem = f"Nome: {nome}<br />Data de envio: {data_envio}"
    return render_template('perfil.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
