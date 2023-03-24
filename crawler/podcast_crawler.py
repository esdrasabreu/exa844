import requests
from bs4 import BeautifulSoup
import json

urls = []
podcasts =[]
podcast = {}
# url = 'https://bibleproject.com/podcasts/the-bible-project-podcast/?view=episode'
urls.append('https://www.stitcher.com/show/super-soul-8521721')
urls.append('https://www.stitcher.com/show/the-plot-thickens-podcast')
urls.append('https://www.stitcher.com/show/jeff-lewis-has-issues')
urls.append('https://www.stitcher.com/show/unladylike')
urls.append('https://www.stitcher.com/show/the-problem-with-jon-stewart')
headers = {
         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
id = 1
for i in range(1,len(urls)+1):
    response2 = requests.get(urls[i-1],headers=headers)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    podcast_list = soup2.find_all('div', class_='ma-0 episode mobileItemListPadding v-list-item v-list-item--link theme--light')

        # f.write('[' + '\n')
    for x in podcast_list:
        podcast["id"] = id

        episodio = x.find('div', class_='text-truncate text-grey5').get_text().strip()
        podcast["episodio"] = episodio

        duracao = x.find('div', class_='v-list-item__subtitle text-grey4 episodeInfo').get_text().strip().split('|')
        podcast["duracao"] = duracao[0].strip()
        podcast["data"] = duracao[1].strip()

        link = x.find('a', class_='text-none episode-link')['href']
        podcast["link"] = 'www.stitcher.com'+ link

        subtitulo = x.find('div', class_='v-list-item__subtitle episodeDescription hidden-sm-and-down-bak hidden-xs-only text-grey5 mt-0 mt-md-1').get_text().strip().split('.')
        podcast["descricao"] = subtitulo[0]

        podcasts.append(podcast)
        id = id + 1

        with open('podcasts.json','a', newline='', encoding='UTF-8') as f:
            pod = json.dumps(podcasts)
            f.write(pod)
        podcasts =[]