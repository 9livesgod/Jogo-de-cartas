# Projeto de Jogo de Cartas Colecionáveis

## Visão Geral

**PATRICK ANDERSON CARVALHO DOS SANTOS (211030620)
Este projeto é um jogo de cartas colecionáveis baseado em classes de orientação a objetos. O jogo consiste em vários componentes, incluindo jogadores, cartas, decks, tabuleiros e jogadas. Cada um desses componentes é representado por uma classe com atributos e métodos específicos.

## Classes do Projeto
- **Jogador**
  - A classe `Jogador` representa um jogador do jogo.
  - Atributos:
    - `nome: String` - Nome do jogador.
    - `pontuação: int` - Pontuação do jogador.
  - Métodos:
    - `iniciarJogo()`: Inicia um jogo.
    - `jogarCarta()`: Realiza uma jogada no jogo.
    - `atacar()`: Ataca um oponente.
    - `terminarTurno()`: Termina o turno do jogador.

- **Deck**
  - A classe `Deck` representa o baralho de um jogador.
  - Atributos:
    - `cartas: List<Carta>` - Lista de cartas no deck.
  - Métodos:
    - `adicionarCarta(carta: Carta)`: Adiciona uma carta ao deck.
    - `removerCarta(carta: Carta)`: Remove uma carta do deck.

- **Carta**
  - A classe `Carta` é a classe base para todas as cartas do jogo.
  - Atributos:
    - `nome: String` - Nome da carta.
    - `descrição: String` - Descrição da carta.
    - `poder: int` - Poder da carta.
  - Métodos:
    - `usar()`: Usa a carta.
    - `descartar()`: Descarta a carta.

- **CartaMonstro**
  - A classe `CartaMonstro` é uma subclasse de `Carta` e representa as cartas de monstro.
  - Atributos adicionais:
    - `nível: int` - Nível do monstro.
    - `pontosAtaque: int` - Pontos de ataque do monstro.
    - `pontosDefesa: int` - Pontos de defesa do monstro.

- **CartaMagia**
  - A classe `CartaMagia` é outra subclasse de `Carta` e representa as cartas de magia.
  - Atributos adicionais:
    - `efeito: String` - Descrição do efeito da magia.
    - `alvo: String` - Alvo da magia.

- **BaralhoInicial**
  - A classe `BaralhoInicial` representa o conjunto inicial de cartas de um jogador.
  - Atributos:
    - `cartasIniciais: List<Carta>` - Lista de cartas iniciais.
  - Métodos:
    - `adicionarCarta(carta: Carta)`: Adiciona uma carta ao baralho inicial.
    - `removerCarta(carta: Carta)`: Remove uma carta do baralho inicial.

- **Tabuleiro**
  - A classe `Tabuleiro` representa o tabuleiro de jogo onde as cartas são jogadas e as jogadas são realizadas.
  - Atributos:
    - `cartasNoTabuleiro: List<Carta>` - Lista de cartas no tabuleiro.
  - Métodos:
    - `realizarJogada(jogador: Jogador, carta: Carta, alvo: Carta)`: Realiza uma jogada no tabuleiro.

- **Efeito**
  - A classe `Efeito` representa um efeito especial que pode ser ativado por certas cartas de magia.
  - Atributos:
    - `descricao: String` - Descrição do efeito especial.
  - Métodos:
    - `ativarEfeito(cartaMagia: CartaMagia, alvo: Carta)`: Ativa o efeito especial em uma carta de magia.

- **Jogada**
  - A classe `Jogada` representa uma jogada realizada por um jogador durante o jogo.
  - Atributos:
    - `jogador: Jogador` - O jogador que realiza a jogada.
    - `carta: Carta` - A carta envolvida na jogada.
    - `alvo: Carta` - O alvo da jogada (opcional).
  - Métodos:
    - `executarJogada()`: Executa a jogada, aplicando os efeitos apropriados.

## Relações entre Classes
- **Herança:**
  - A classe `CartaMonstro` herda de `Carta`.
  - A classe `CartaMagia` herda de `Carta`.

- **Associação:**
  - A classe `Jogador` está associada à classe `Deck`, `Pontuação`, `BaralhoInicial` e `Tabuleiro`.
  - A classe `Deck` está associada à classe `Carta`.
  - A classe `Tabuleiro` está associada à classe `Jogador` e `Jogada`.
  - A classe `Efeito` está associada à classe `CartaMagia`.
  - A classe `Jogada` está associada à classe `Jogador`, `Carta`, `Tabuleiro` e `Efeito`.

Este é um resumo simplificado do projeto de jogo de cartas colecionáveis com as classes, atributos, métodos e relações entre elas. Você pode expandir e personalizar este projeto de acordo com as regras e mecânicas específicas do seu jogo.
