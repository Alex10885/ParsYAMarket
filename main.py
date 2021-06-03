from bs4 import BeautifulSoup

def parse(html_data):
   soup = BeautifulSoup(html_data, 'lxml')

   values = soup.find_all("div", attrs={"class": "_3K8Ed1m6dJ"})

   for value in values:
      autor_tag = value.find('div', attrs={"data-tid": "d0b5b434"})
      print(autor_tag.text)

      raiting_tag = value.find('span', attrs={"class": "pcIgrqlZjH"})
      print(raiting_tag.text)

      description_tag = value.find('div', attrs={"data-tid": "1a025034"})
      print(description_tag.text)



file = open('yamarketPage.html', 'r', encoding='utf-8')
data = file.read()
file.close()

parse(data)





