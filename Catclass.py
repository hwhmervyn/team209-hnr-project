import requests
import json
from bs4 import BeautifulSoup


class lolcat:

    def __init__(self):
        self.base = "https://speaklolcat.com/?from="
        self.table = {}

    def translate(self, phrase):
        url = self.base
        phrase.replace(" ", "+")
        url += phrase
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, 'html.parser')
        text = soup.find('div', {'id': 'text'})
        output = text.find_all('p')[1]
        return '. '.join(map(lambda x: x.strip().capitalize(), output.text.split('.')))

    def cat_pic(self):
        web = "https://api.thecatapi.com/v1/images/search"
        json_obj = requests.get(web)
        content = json_obj.content.decode("utf8")
        data = json.loads(content)
        image_url = data[0]['url']
        return image_url
