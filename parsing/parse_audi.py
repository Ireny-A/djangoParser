import requests
from bs4 import BeautifulSoup
import pandas as pd
from parsing.models import Note
import openpyxl


class ParserAu:
    def main(self):
        Note.objects.all().delete()  # обнуляем бд перед следующим парсингом
        self.save(self.parse_au())

    def parse_au(self):
        article = {}
        title = []
        link = []
        content = []
        price = []

        r = requests.get('https://cars.av.by/filter?brands[0][brand]=6&page=2')
        soup = BeautifulSoup(r.content, 'html.parser')

        for counter, a in enumerate(soup.select('a.listing-item__link span')):
            title.append(a.text.strip())

        for counter, a in enumerate(soup.select('a.listing-item__link')):
            link.append(f'https://cars.av.by{a["href"]}')

        for counter, a in enumerate(soup.select('div.listing-item__params')):
            content.append(a.text.strip())

        for counter, a in enumerate(soup.select('div.listing-item__price')):
            price.append(a.text.strip())

        article = {
            'марка авто': title,
            'ссылка': link,
            'описание': content,
            'цена': price,

        }

        for i in range(len(title)):
            p = Note(
                title=article['марка авто'][i],
                link=article['ссылка'][i],
                content=article['описание'][i],
                price=article['цена'][i],
            )
            p.save()
            print(f'note{p}')

        return article

    def save(self, arg):
        auto = pd.DataFrame(arg)
        writer = pd.ExcelWriter('audi.xlsx')
        auto.to_excel(writer, 'Audi')
        writer.save()



