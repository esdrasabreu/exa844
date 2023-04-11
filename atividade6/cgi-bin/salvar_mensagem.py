#!/usr/bin/env python3


import cgi
import cgitb
import datetime

print("Cache-Control: no-cache, no-store, must-revalidate")
# Redirecionar usuário de volta para a página de blog
print('Content-Type: text/html')
print('Location: index.html')
print()

# Ativar exibição de rastreamento de erros CGI
cgitb.enable()

# Criar objeto FieldStorage
form = cgi.FieldStorage()

# Obter dados de entrada do usuário
autor = form.getvalue('autor')
mensagem = form.getvalue('mensagem')

# Abrir arquivo para escrita
with open('mensagens.txt', 'a') as arquivo:
    # Escrever dados no arquivo
    arquivo.write(f'Autor: {autor}\n')
    arquivo.write(f'Data: {datetime.datetime.now()}\n')
    arquivo.write(f'Mensagem: {mensagem}\n')
    arquivo.write('-----------------------------------------\n')


with open("mensagens.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("<html>")
print("<head>")
print("<title>Minhas Mensagens</title>")
print("</head>")
print("<body>")
print("<h1>Minhas Mensagens</h1>")
print("<p>Aqui estão as mensagens que eu já enviei:</p>")
print("<ul>")
for mensagem in conteudo.split("\n-----------------------------------------\n"):
    if mensagem:
        autor, data, texto = mensagem.split("\n", 3)
        print(f"<li><strong>{autor}:</strong> {texto}<br><em>{data}</em></li>")
print("</ul>")
print("</body>")
print("</html>")

print("<html>")
print("<head>")
print("<title>Crie suas mensagens</title>")
print("</head>")
print("<body>")
print("<h1>Crie suas mensagens</h1>")
print("<form action=\"salvar_mensagem.py\" method=\"post\">")
print("<label for=\"autor\">Autor:</label>")
print("<input type=\"text\" name=\"autor\" id=\"autor\" required><br>")
print("<label for=\"mensagem\">Mensagem:</label>")
print("<textarea name=\"mensagem\" id=\"mensagem\" required></textarea><br>")
print("<input type=\"submit\" value=\"Enviar\">")
print("</form>")
print("</body>")
print("</html>")

