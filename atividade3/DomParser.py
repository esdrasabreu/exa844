import xml.dom.minidom
import time

inicio = time.time()

# Abra o arquivo XML
dom = xml.dom.minidom.parse("map.osm")

# Encontre todos os elementos "estabelecimento"
estabelecimentos = dom.getElementsByTagName("node")

# Para cada elemento "estabelecimento"
for estabelecimento in estabelecimentos:
    nome = None
    tipo = None
    # Obtenha os atributos
    tags = estabelecimento.getElementsByTagName("tag")
    for tag in tags:
        if tag.getAttribute("k") == "amenity":
            tipo = tag.getAttribute("v")
        if tag.getAttribute("k") == "name":
            nome = tag.getAttribute("v")
    
    latitude = estabelecimento.getAttribute("lat")
    longitude = estabelecimento.getAttribute("lon")
    
    # Escreva a string com os valores dos atributos
    if tipo != None and nome !=None:
        print("lat:{},lon:{},tipo:{},nome:{}".format(latitude, longitude, tipo, nome))

fim = time.time()
print("tempo de execução dom:", fim - inicio)

