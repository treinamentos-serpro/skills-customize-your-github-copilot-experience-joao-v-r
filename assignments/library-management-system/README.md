# 📘 Atividade: Library Management System

## 🎯 Objetivo

Praticar programação orientada a objetos em Python criando um sistema simples de gerenciamento de biblioteca com classes para livros, usuários e empréstimos.

## 📝 Tarefas

### 🛠️ Criar a classe `Book`

#### Descrição
Defina uma classe para representar um livro da biblioteca, incluindo informações básicas e o estado atual de disponibilidade.

#### Requisitos
O programa concluído deve:

- Criar uma classe `Book` com atributos como `title`, `author`, `isbn` e `available`
- Incluir um método `display_info()` para mostrar os detalhes do livro
- Permitir que um livro seja marcado como disponível ou indisponível
- Criar pelo menos dois objetos `Book` para testar a classe

### 🛠️ Criar a classe `Member`

#### Descrição
Crie uma classe para representar um membro da biblioteca, com nome, ID e lista de livros emprestados.

#### Requisitos
O programa concluído deve:

- Criar uma classe `Member` com atributos `name`, `member_id` e `borrowed_books`
- Incluir um método para adicionar um livro à lista de empréstimos
- Incluir um método para listar os livros atualmente emprestados
- Demonstrar a criação de pelo menos um membro e o uso dos métodos

### 🛠️ Criar a classe `Library`

#### Descrição
Implemente a classe principal do sistema, responsável por registrar livros, membros e realizar empréstimos.

#### Requisitos
O programa concluído deve:

- Criar uma classe `Library` com listas de `books` e `members`
- Incluir um método para adicionar novos livros
- Incluir um método para registrar novos membros
- Incluir um método `borrow_book(member, book)` para realizar o empréstimo
- Atualizar o status de disponibilidade do livro quando ele for emprestado
- Exibir mensagens claras para sucesso ou erro na operação

### 🛠️ Simular um cenário real de uso

#### Descrição
Use as classes para simular uma biblioteca pequena com múltiplos livros e usuários.

#### Requisitos
O programa concluído deve:

- Criar uma biblioteca com pelo menos 3 livros e 2 membros
- Emprestar um livro para um membro com sucesso
- Tentar emprestar o mesmo livro para outro membro e mostrar uma mensagem de erro
- Exibir os livros disponíveis e os livros em posse de cada membro

## ✅ Objetivo de aprendizagem

Ao final desta atividade, o aluno deve compreender como as classes interagem entre si, como representar entidades do mundo real em programação e como usar objetos para organizar a lógica de um sistema simples.
