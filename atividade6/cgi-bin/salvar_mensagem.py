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
