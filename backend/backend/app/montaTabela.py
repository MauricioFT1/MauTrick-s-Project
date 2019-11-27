import requests
from bs4 import BeautifulSoup
from .models import Brazilian

# class Tabela():
#     def __init__(self, name, score, games, wins, draws, loses):
#         self.name = name
#         self.socre = score
#         self.games = games
#         self.wins = wins
#         self.draws = draws
#         self.loses = loses

def montandoTabela():
    Brazilian.objects.all().delete()
    List = []
    page = requests.get("https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/")
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('tbody')
    # print(table.find_all('tr'))
    for linha in table.find_all('tr'):
        coluna = linha.find_all('td')
        
        # Pegando nomes
        name = coluna[2].get_text().split(' >>')[0]
        
        # Pegando pontos
        score = coluna[4].get_text()

        # Pegando jogos
        games = coluna[5].get_text()

        # Pegando vitórias
        wins = coluna[6].get_text()

        # Pegando empates
        draws = coluna[7].get_text()

        # Pegando derrotas
        loses = coluna[8].get_text()

        team = Brazilian(name=name, 
            score=int(score), 
            games=int(games), 
            wins=int(wins), 
            draws=int(draws), 
            loses=int(loses))
        team.save()
        List.append(1)

    return ""

if __name__ == "__main__":
    montandoTabela()

