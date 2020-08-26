import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

page = urllib.request.urlopen('https://docs.python.org/3/library/random.html')
soup = bs(page)

names = soup.body.findAll('dt')
function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]

description = soup.body.findAll('dd')
function_usage = []

for item in description:
    item = item.text
    item = item.replace('\n', ' ')
    function_usage.append(item)

print(function_names)
print(function_usage)
print(len(function_names))
print(len(function_usage))

data = pd.DataFrame({'function name': function_names, 'function usage': function_usage})
data.head()

data.to_csv('practice.csv')