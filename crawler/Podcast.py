import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

class Podcast:
    def __init__(self, id, episodio, duracao, data, link, descricao):
        self.id = id
        self.episodio = episodio
        self.duracao = duracao
        self.data = data
        self.link = link
        self.descricao = descricao

class PodcastAPI:
    def __init__(self):
        self.conn = sqlite3.connect('podcasts.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS podcasts (id INTEGER PRIMARY KEY, episodio TEXT, duracao TEXT, data TEXT, link TEXT, descricao TEXT)')

    def get_all(self):
        self.cursor.execute('SELECT * FROM podcasts')
        rows = self.cursor.fetchall()
        podcasts = []
        for row in rows:
            podcasts.append(Podcast(row[0], row[1], row[2], row[3], row[4], row[5]))
        return podcasts

    def add(self, podcast):
        self.cursor.execute('INSERT INTO podcasts VALUES (?, ?, ?, ?, ?, ?)', (podcast.id, podcast.episodio, podcast.duracao, podcast.data, podcast.link, podcast.descricao))
        self.conn.commit()

    def update(self, id, podcast):
        self.cursor.execute('UPDATE podcasts SET episodio=?, duracao=?, data=?, link=?, descricao=? WHERE id=?', (podcast.episodio, podcast.duracao, podcast.data, podcast.link, podcast.descricao, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM podcasts WHERE id=?', (id,))
        self.conn.commit()

api = PodcastAPI()

@app.route('/podcasts', methods=['GET'])
def get_all():
    podcasts = api.get_all()
    return jsonify([{'id': podcast.id, 'episodio': podcast.episodio, 'duracao': podcast.duracao, 'data': podcast.data, 'link': podcast.link, 'descricao': podcast.descricao} for podcast in podcasts])

@app.route('/podcasts', methods=['POST'])
def add():
    id = request.json['id']
    episodio = request.json['episodio']
    duracao = request.json['duracao']
    data = request.json['data']
    link = request.json['link']
    descricao = request.json['descricao']
    podcast = Podcast(id, episodio, duracao, data, link, descricao)
    api.add(podcast)
    return jsonify({'message': 'Podcast added successfully'})


@app.route('/podcasts/<int:id>', methods=['PUT'])
def update(id):
    podcast = api.get(id)
    if not podcast:
        return jsonify({'message': 'Podcast not found'}), 404

    podcast.episodio = request.json.get('episodio', podcast.episodio)
    podcast.duracao = request.json.get('duracao', podcast.duracao)
    podcast.data = request.json.get('data', podcast.data)
    podcast.link = request.json.get('link', podcast.link)
    podcast.descricao = request.json.get('descricao', podcast.descricao)

    api.update(podcast)

    return jsonify({'message': 'Podcast updated successfully'})


@app.route('/podcasts/<int:id>', methods=['DELETE'])
def delete(id):
    podcast = api.get(id)
    if not podcast:
        return jsonify({'message': 'Podcast not found'}), 404

    api.delete(podcast)

    return jsonify({'message': 'Podcast deleted successfully'})

