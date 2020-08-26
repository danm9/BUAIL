import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_megaprojects')
soup = bs(page)

#project | location  | status | cost  | notes

rows = soup.findAll('tr')

data = []

print(rows)

for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
result = pd.DataFrame(data, columns=['project', 'location', 'status', 'cost', 'notes'])

print(result)

result.to_csv('megaproject.csv')