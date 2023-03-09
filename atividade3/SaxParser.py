import xml.sax
import time

class OsmHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = None
        self.node_attrs = {}
        self.tags = []
        self.lat = None
        self.lon = None
        self.name = None
        self.type = None

    def startElement(self, name, attrs):
        self.current_tag = name
        if name == 'node':
            self.node_attrs = attrs
            self.lat = float(attrs['lat'])
            self.lon = float(attrs['lon'])
        elif name == 'tag':
            self.tags.append(attrs)
            if attrs['k'] == 'name':
                self.name = attrs['v']
            elif attrs['k'] == 'amenity':
                self.type = attrs['v']
            elif attrs['k'] == 'highway':
                self.type = attrs['v']

    def endElement(self, name):
        self.current_tag = None
        if name == 'node':
            if self.name is not None and self.type is not None:
                print(f"lat:{self.lat},lon:{self.lon},tipo:{self.type},nome:{self.name}")
            self.lat = None
            self.lon = None
            self.name = None
            self.type = None
            self.tags = []

if __name__ == '__main__':
    inicio = time.time()
    with open('map.osm', 'r') as f:
        handler = OsmHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(f)
    fim = time.time()
    print("tempo de execução sax:", fim - inicio)
