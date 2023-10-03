import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class FormaGeometrica:
    def CalcularArea(self):
        pass

    def CalcularPerimetro(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio, centro):
        self.raio = raio
        self.centro = centro

    def CalcularArea(self):
        return math.pi * self.raio ** 2

    def CalcularPerimetro(self):
        return 2 * math.pi * self.raio

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def CalcularArea(self):
        return self.largura * self.altura

    def CalcularPerimetro(self):
        return 2 * (self.largura + self.altura)

class Triangulo(FormaGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def CalcularArea(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def CalcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3

formasGeometricas = []

while True:
    print("\nMenu de Opções:")
    print("1. Criar Círculo")
    print("2. Criar Retângulo")
    print("3. Criar Triângulo")
    print("4. Listar Formas Geométricas")
    print("5. Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        raio = float(input("Digite o raio do círculo: "))
        x = float(input("Digite a coordenada x do centro: "))
        y = float(input("Digite a coordenada y do centro: "))
        centro = Ponto(x, y)
        circulo = Circulo(raio, centro)
        formasGeometricas.append(circulo)
        print("Círculo criado com sucesso!")

    elif escolha == 2:
        largura = float(input("Digite a largura do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        retangulo = Retangulo(largura, altura)
        formasGeometricas.append(retangulo)
        print("Retângulo criado com sucesso!")

    elif escolha == 3:
        lado1 = float(input("Digite o primeiro lado do triângulo: "))
        lado2 = float(input("Digite o segundo lado do triângulo: "))
        lado3 = float(input("Digite o terceiro lado do triângulo: "))
        triangulo = Triangulo(lado1, lado2, lado3)
        formasGeometricas.append(triangulo)
        print("Triângulo criado com sucesso!")

    elif escolha == 4:
        print("\nFormas Geométricas:")
        for forma in formasGeometricas:
            if isinstance(forma, Circulo):
                print(f"Círculo - Área: {forma.CalcularArea()}, Perímetro: {forma.CalcularPerimetro()}")
            elif isinstance(forma, Retangulo):
                print(f"Retângulo - Área: {forma.CalcularArea()}, Perímetro: {forma.CalcularPerimetro()}")
            elif isinstance(forma, Triangulo):
                print(f"Triângulo - Área: {forma.CalcularArea()}, Perímetro: {forma.CalcularPerimetro()}")

    elif escolha == 5:
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
