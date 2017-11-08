import urllib.request
from bs4 import BeautifulSoup
import color

# Exemplo - http://matheusclemente.com.br
site = input(color.GREEN + "Informe o site para ser analisado\n" + color.END)

fp = urllib.request.urlopen(site)
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
html_doc = mystr
soup = BeautifulSoup(html_doc, 'html.parser')


class AnalisaSite:
    def listartags():
        # Exemplo - h1,p,h2,li,ul...
        text = input("Informe o elemento a ser listado \n")
        print(soup.find_all(text))

    def contartags():
        # Exemplo - h1,p,h2,li,ul...
        text = input("Informe o elemento a ser contado\n")
        print(len(soup.find_all(text)))
