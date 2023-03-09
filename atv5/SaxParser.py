from html.parser import HTMLParser
import urllib.request


class MyHTMLParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.currentData = ""
    self.title = ""
    self.image = ""

  def handle_starttag(self, tag, attrs):
    self.currentData = ""
    
    if tag =="img":  
      for k, v in attrs:
        if k == "src":
          self.image = v

  def handle_endtag(self, tag):
    if tag =="title": 
      self.title = self.currentData      

  def handle_data(self, data):
    self.currentData += data    

urls = []
with open("seeds.txt") as file:
    for line in file.readlines():
      urls.append(line)

# print(urls)

print("""
  <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Esdras ATV 05</title>
</head>
<body>
""")

for u in urls:
  try:
    page = urllib.request.urlopen(u)
    parser = MyHTMLParser()
    parser.feed(str(page.read().decode('utf-8')))

    endereco_img = u
    if(parser.image.count("http") == 0):
      endereco_img += parser.image
    # Define as informações a serem exibidas
    nome = parser.title
    endereco_img = endereco_img
    print("Nome: ", nome)
    print("Imagem: ", parser.image)
    print("<br>")
    print('<img src="{}" style="width: 20%;" />'.format(endereco_img))
    print("<br>")
    print("<br>")
  except:
    pass
  # Renderiza o modelo com as informações
  # html = template.render(nome=nome, endereco_img=endereco_img)

  # Imprime o HTML resultante
  
  # print("Título:", parser.title)
  
  # print("Imagem:", endereco_img)
print("""
</body>
</html>
""")