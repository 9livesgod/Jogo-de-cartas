import json
from player import Player

arquivo_json = 'C:/Users/pedri/OneDrive/Área de Trabalho/programação/python/Orientação a Objetos - Faculdade/Projeto Final/players.json'
with open(arquivo_json) as fp:
    playersList = json.load(fp)
    
    
def adicionar_player(nome_de_usuario): #adiciona um player novo a nossa base de dados
    newPlayer = Player(nome_de_usuario, 0)
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




# def obter_records(player):
#     nome = player.get_nome()
    
    
# def salvar_record(player):    