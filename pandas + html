import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ru.wikipedia.org/wiki/Международный_индекс_счастья"
allinfo = []
country = []
hpi = []
lifeQ = []
lifeExp = []
EcoTrail = []

page = requests.get(url)
text = page.text 
soup = BeautifulSoup(text, "lxml")
soup.prettify()

table = soup.find_all('table')[2]
for t in table.find_all('td'):    
    allinfo.append(t.text)
for i in range(1,len(allinfo),6):
    country.append(allinfo[i][1:])
for i in range(2,len(allinfo),6):
    hpi.append(allinfo[i])
for i in range(3,len(allinfo),6):
    lifeQ.append(allinfo[i])
for i in range(4,len(allinfo),6):
    lifeExp.append(allinfo[i])
for i in range(5,len(allinfo),6):
    EcoTrail.append(allinfo[i][:3])

df = pd.DataFrame({'Страна': country, 'HPI': hpi, 'Удовлетворенность жизнью': lifeQ, 'Ожидаемая продолжительность жизни': lifeExp, 'Экологический след': EcoTrail })
df.head()
#df1 = df.to_string(index=False)
df.to_csv("Международный индекс счастья.csv")
