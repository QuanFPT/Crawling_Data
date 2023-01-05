import requests
from bs4  import BeautifulSoup

r=requests.get("https://dantri.com.vn/")
soup=BeautifulSoup(r.content, "html.parser")
titles=soup.findAll('h3',class_="article-title")

links=[link.find('a').attrs["href"] for link in titles]

with open("crawlData\data.txt", "w", encoding="utf-8") as f:
    
    for link in links:
        try:
            news = requests.get("https://dantri.com.vn"+link)
            soup = BeautifulSoup(news.content,"html.parser")
            title = str(soup.find("h1", class_="title-page detail").text)
            singular_sapo=str(soup.find("h2", class_="singular-sapo").text)
            singular_content=soup.find(class_="singular-content")
            content=str(singular_content.text)
            image=singular_content.find("img").attrs["src"]
            f.write("Tiêu đề: " +title)
            f.write("Mô tả: " +singular_sapo)
            f.write("Nội dung: " +content)
            f.write("Ảnh minh họa: " +image)
            f.write("----------------------------------------------------------------------------------------------------")
        except AttributeError:
            continue
    
f.close()