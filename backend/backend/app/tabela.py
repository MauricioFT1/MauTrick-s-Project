import requests
from bs4 import BeautifulSoup

class Tabela():
    def __init__(self, name, score, games, wins, draws, loses):
        self.name = name
        self.socre = score
        self.games = games
        self.wins = wins
        self.draws = draws
        self.loses = loses

def montandoTabela():
    # teams, scores, games, wins, losses, draws = []
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

        team = Tabela(name, score, games, wins, draws, loses)
        List.append(team)

    return List

if __name__ == "__main__":
    montandoTabela()

