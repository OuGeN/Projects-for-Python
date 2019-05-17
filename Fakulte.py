import requests
from bs4 import BeautifulSoup


r=requests.get('http://www2.firat.edu.tr/content/akademik')
soup= BeautifulSoup(r.content,"html.parser")
gelen_veri=soup.find_all("div",{"class":"fakulte"})
ptag2 = soup.find_all("p")
for i in ptag2:
 i.decompose()
ptag3=soup.find_all("div",{"id":"b_title"})
for i in ptag3:
    i.decompose()
for i in gelen_veri:
    icerik=i.text
    print(icerik)