- **Classe Jogador:** Representa um jogador do jogo. Possui atributos como nome e pontuação.

- **Classe Carta:** Esta é a classe base para todas as cartas do jogo. Ela possui atributos como nome, descrição e poder.

- **Classe CartaMonstro:** Esta é uma classe derivada de Carta que representa as cartas de monstro. Ela adiciona atributos específicos, como nível e pontos de ataque/defesa.

- **Classe CartaMagia:** Esta é outra classe derivada de Carta que representa cartas de magia. Ela adiciona atributos como efeito e alvo.

- **Classe Deck:** Representa o deck de um jogador, que contém uma coleção de cartas. Os jogadores podem ter diferentes cartas em seus decks.

- **Associação entre Jogador e Deck:** Indica que um jogador possui um deck. Um jogador pode ter apenas um deck.

- **Associação entre Deck e Carta:** Indica que um deck contém várias cartas. Um deck pode conter várias cartas, e uma carta pode estar em apenas um deck.
