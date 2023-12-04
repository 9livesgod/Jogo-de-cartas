from player import Player
import leaderoard

username = input("Digite o nome de usuario do Jogador: ")
if (leaderoard.verificar_player(username) == 2 or leaderoard.verificar_player(username) == False): 
    #se nao tem nenhum player existente na base de dados ou se o player ainda nao existe, entra na condicao
    leaderoard.adicionar_player(username) #adiciona o novo player a nossa base de dados com uma pontuacao 0
else:
    print(leaderoard.verificar_player(username))
