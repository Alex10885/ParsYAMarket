import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup

MASTER_URL = 'https://www.avito.ru'

URL = 'https://www.avito.ru/belgorod/vakansii/it_internet_telekom-ASgBAgICAUSOC_SdAQ?cd=1'
HEADESR = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

def get_html(url, params=None):
    req = requests.get(url, headers=HEADESR, params=params)
    return req

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    values = soup.find_all('div', attrs={'class': 'iva-item-content-m2FiN'})
    for value in values:
        vacancy_name = value.find('h3', attrs={'class': 'title-root-395AQ'})
        print(vacancy_name.text)

        vacancy_salary = value.find('span', attrs={'class': 'price-text-1HrJ_'})
        print('Зарплата: ' + vacancy_salary.text)

        vacancy_marker = value.find('div', attrs={'data-marker': 'item-specific-params'})
        print(vacancy_marker.text)

        vacancy_link = value.find('a')
        print('Ссылка на вакансию: ' + MASTER_URL + vacancy_link.get('href'))

        vacancy_publication = value.find('div', attrs={'data-marker': 'item-date'})
        print(vacancy_publication.text)
        print('\n')

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()