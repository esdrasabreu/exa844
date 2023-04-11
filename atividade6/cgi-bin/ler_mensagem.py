#!/usr/bin/env python
import cgi

# Define o cabeçalho HTTP
print("Content-Type: text/html")
print()

# Lê o conteúdo do arquivo
with open("mensagens.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Gera o HTML
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
