import requests as req
from bs4 import BeautifulSoup


def extract_products(products, page):
    ans = list()
    for product in products:
        prod = dict()
        prod['name'] = product.find('a').get('title')
        prod['price'] = product.find(class_='nm-price-value')
        prod['price'] = prod['price'].text.strip().replace('.', '')
        prod['price'] = float(prod['price'].replace(',', '.'))
        prod['img'] = product.find('img').get('src')
        prod['url'] = 'http://'+product.find('a').get('href')[2:]
        prod['page'] = page

        ans.append(prod)

    return ans


def search_carrefour(query, verbose=False):
    ans = list()
    pages = 2 if not verbose else 50

    query = query.replace(' ', '+')

    for i in range(1, pages + 1):
        URL = "https://busca.carrefour.com.br/busca?q=%s&page=%s" % (query, i)
        res = req.get(URL)
        soup = BeautifulSoup(res.text, "html.parser")
        products = soup.find_all(class_='nm-product-item')

        if len(products) > 0:
            for prod in extract_products(products, i):
                ans.append(prod)
        else:
            break
    return ans


if __name__ == "__main__":
    query = input('Enter a product: ')
    print('Please wait...')
    prods = search_carrefour(query)
    print(prods)
