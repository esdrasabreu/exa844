import xml.dom.minidom
import time
import json
elements = dict()
feature = dict()
properties =  dict()
# features['properties'] = properties
coordinates = []
geometry = dict()


inicio = time.time()

# Abra o arquivo XML
dom = xml.dom.minidom.parse("map.osm")

# Encontre todos os elementos "estabelecimento"
estabelecimentos = dom.getElementsByTagName("node")
dom_esta = []
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
        # elements.add("lat:{},lon:{},tipo:{},nome:{}".format(latitude, longitude, tipo, nome))
        dom_esta.append({"lat": latitude, "lon": longitude, "tipo": tipo, "nome": nome})
        # coordinates.append(longitude,latitude)

# print(elements)
features = []
for e in dom_esta:
    # coordinates.append([e["lon"],e["nome"]])
    geometry['type'] = 'Point'
    # print(e)
    geometry['coordinates'] = [float(e["lon"]),float(e["lat"])]
    properties['nome'] = e["nome"]
    properties['tipo'] = e["tipo"]
    feature['type'] = "Feature"
    feature['geometry'] = geometry
    feature['properties'] = properties
    
    features.append(feature)
    geometry = dict()
    feature = dict()
    properties = dict()

mapa = dict()
mapa['type'] = 'FeatureCollection'
mapa['features'] = features

jsonStr = json.dumps(mapa, indent=4, ensure_ascii=False)
print(jsonStr)
obj = json.loads(jsonStr)

with open('geo.geojson', 'w') as f:
    json.dump(obj, f)
