class Player:
    def __init__(self, nome, pontuacao):
        self.__nome = nome
        self.__pontuacao = pontuacao
    
    def mostrar_pontuacao(self):
        return print(f'A pontuacao do jogador {self.get_nome()} é de {self.get_pontuacao()}')
    def get_nome(self):
        return self.__nome
    def get_pontuacao(self):
        return self.__pontuacao