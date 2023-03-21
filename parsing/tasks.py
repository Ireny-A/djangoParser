# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import openpyxl
#
#
# def main():
#     save(parse_bmw())
#
#
# def parse_bmw():
#     article = {}
#     title = []
#     link = []
#     content = []
#     price = []
#
#     r = requests.get('https://cars.av.by/filter?brands[0][brand]=8&page=1')
#     soup = BeautifulSoup(r.content, 'html.parser')
#
#     for counter, a in enumerate(soup.select('a.listing-item__link span')):
#         title.append(a.text.strip())
#
#     for counter, a in enumerate(soup.select('a.listing-item__link')):
#         link.append(f'https://cars.av.by{a["href"]}')
#
#     for counter, a in enumerate(soup.select('div.listing-item__params')):
#         content.append(a.text.strip())
#
#     for counter, a in enumerate(soup.select('div.listing-item__price')):
#         price.append(a.text.strip())
#
#     article = {
#         'марка авто': title,
#         'ссылка': link,
#         'описание': content,
#         'цена': price,
#
#     }
#
#     return article


# for i in range(len(title)):
#     print(title[i])
# for j in range(len(link)):
#     print(link[j])
# for p in range(len(content)):
#     print(content[p])
# for k in range(len(price)):
#     print(price[k])


# def save(arg):
#     auto = pd.DataFrame(arg)
#     writer = pd.ExcelWriter('bmw.xlsx')
#     auto.to_excel(writer, 'BMW')
#     writer.save()
#
#
# if __name__ == "__main__":
#     main()
