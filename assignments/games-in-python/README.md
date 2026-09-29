
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construir um jogo da forca em Python usando strings, listas, loops e condicionais para criar uma experiência interativa de adivinhação de palavras.

## 📝 Tarefas

### 🛠️ Preparação da palavra e do estado inicial do jogo

#### Descrição
Crie uma lista com palavras, escolha uma aleatoriamente e prepare a interface inicial do jogo para o jogador.

#### Requisitos
O programa concluído deve:

- Armazenar pelo menos 5 palavras em uma lista predefinida
- Selecionar uma palavra aleatória para o jogo
- Mostrar o progresso da palavra como letras ocultas, como `_ _ _ _`
- Inicializar o número de tentativas disponíveis
- Exibir uma mensagem de boas-vindas antes do início da partida

### 🛠️ Entrada de palpites e validação da partida

#### Descrição
Permita que o usuário insira letras, atualize o estado da palavra e determine se o jogador venceu ou perdeu.

#### Requisitos
O programa concluído deve:

- Ler uma letra por vez com `input()`
- Verificar se a letra informada está presente na palavra secreta
- Atualizar a exibição do progresso da palavra conforme o jogador acerta
- Contabilizar tentativas incorretas e reduzir o número de chances
- Encerrar o jogo quando a palavra for descoberta ou quando as tentativas acabarem
- Exibir mensagens claras de vitória ou derrota ao final da partida