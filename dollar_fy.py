# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
url = 'http://www.o-xe.com/'
html = requests.get(url)
html = html.text
html.encode('utf-8')
dollar = re.search("<!-- Menu Part -->",html)
start=dollar.start()+5810
end = dollar.end()+5797
print("dollar is sell now {}  . ").format(html[start:end])
