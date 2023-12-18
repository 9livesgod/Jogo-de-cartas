import json
from player import Player
import pygame
import sys

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600



arquivo_json = 'C:/Users/pedri/OneDrive/Área de Trabalho/programação/python/Orientação a Objetos - Faculdade/Projeto Final/players.json'
with open(arquivo_json) as fp:
    playersList = json.load(fp)


class Leaderboard:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 36)
        self.overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.overlay.set_alpha(200)  # Ajuste a opacidade conforme necessário
        self.overlay.fill((0, 0, 0))
    

    def mostrar_pontuacoes(self, scores):
        showing_scores = True

        while showing_scores:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.blit(self.overlay, (0, 0))

            text = self.font.render("Maiores Pontuações: ", True, (255, 255, 255))
            self.window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, 20))

            for i, score in enumerate(scores):
                text = self.font.render(f"{i + 1}- {score}", True, (255, 255, 255))
                self.window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, 70 + i * 30))

            pygame.display.flip()
            
            
def scores():
    listaMaioresPontuacoes = []
    listaNomesMaioresPontuadores = []
    for i in range(len(playersList)):
        listaMaioresPontuacoes.append(playersList[i]['_Player__pontuacao'])
        listaNomesMaioresPontuadores.append(playersList[i]['_Player__nome'])
        #ordernar o dicionario
    dados_combinados = list(zip(listaMaioresPontuacoes, listaNomesMaioresPontuadores))
    dados_combinados = sorted(dados_combinados, reverse=True)
    return dados_combinados[:10]

def adicionar_player(nome_de_usuario): #adiciona um player novo a nossa base de dados
    newPlayer = Player(nome_de_usuario, 100)
    playersList.append(vars(newPlayer))
    with open(arquivo_json, 'w') as updateFile:
        json.dump(playersList, updateFile, indent=4)



def verificar_player(username):
    if(len(playersList) == 0):
        return 2 #significa que a nossa base de dados nao tem nenhum player
    for i in range(len(playersList)):
        if playersList[i]['_Player__nome'] == username: 
            #se existe, a funcao retornará o nome e a pontuacao do player
            return playersList[i]['_Player__nome'], playersList[i]['_Player__pontuacao']
    return False #quer dizer que o player nao existe na nossa base de dados
        
        
def inicializar_score(username):
    for i in range(len(playersList)):
        if playersList[i]['_Player__nome'] == username:
            return playersList[i]['_Player__pontuacao']
        
        
        
def atualizar_score(username, score):
    for i in range(len(playersList)):
        if playersList[i]['_Player__nome'] == username:
            playersList[i]['_Player__pontuacao'] = score
            with open(arquivo_json, 'w') as updateFile:
                json.dump(playersList, updateFile, indent=4)