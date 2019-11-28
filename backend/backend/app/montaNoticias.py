import requests
from bs4 import BeautifulSoup
from .models import Noticia

# class Noticia:
#     def __init__(self, summary, title, link, image):
#         self.link = link
#         self.summary = summary
#         self.title = title
#         self.image = image

    # def setLink(self, link):
    #     self.link = link
     
    # def setImage(self, image):
    #     self.image = image

    # def setSummary(self, summary):
    #     self.summary = summary

    # def setTitle(self, title):
    #     self.title = title
     
    # def getLink(self):
    #     return self.link
         
    # def getImage(self):
    #     return self.image

    # def getSummary(self):
    #     return self.summary

    # def getTitle(self):
    #     return self.title

def montandoNoticias():
    Noticia.objects.all().delete()
    List = []
    page = requests.get("https://globoesporte.globo.com/futebol/")
    soup = BeautifulSoup(page.content, 'html.parser')
    # Todas notícias estão na "bastian-page".
    # Então ele faz uma lista com elas(find_all no feed-item)
    noticias = soup.find('div', class_='bastian-page').find_all('div', class_="bastian-feed-item")
    
    x = 0 # Começa no 2 porque são o que interessa kk
    while len(List) != 3: # Só para de adicinar quando tiver 3 notícias
        linkImage = noticias[x].find('img', class_="bstn-fd-picture-image")
        summ = noticias[x].find('div', class_="feed-post-body-resumo")
        if linkImage and summ: # Pega o link da imagem, se tiver algo (imagem) ele adiciona essa notícia...
            tempWithLinkAndTitle = noticias[x].find('a', class_="feed-post-link gui-color-primary gui-color-hover")
            
            title = tempWithLinkAndTitle.get_text()
            
            link = tempWithLinkAndTitle['href']
            
            summary = summ.get_text()
            
            image = linkImage['src']

            time = noticias[x].find('span', class_="feed-post-datetime").get_text()
            
            news = Noticia(
                link=link,
                title=title,
                summary=summary,
                image=image
                
            )
            news.save()
            List.append(1)
        x += 1

    return ""

if __name__ == "__main__":
    montandoNoticias()
