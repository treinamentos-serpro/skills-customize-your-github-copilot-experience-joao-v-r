# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprender os conceitos básicos de criação de APIs REST com o framework FastAPI em Python, incluindo rotas, respostas JSON, validação de dados e documentação automática.

## 📝 Tarefas

### 🛠️ Configurar a aplicação FastAPI e criar o endpoint inicial

#### Descrição
Crie uma aplicação FastAPI simples e exponha um endpoint raiz para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Importar `FastAPI` e criar uma instância chamada `app`
- Definir uma rota `GET /` que retorne uma mensagem de boas-vindas
- Ajustar o título da aplicação para refletir o objetivo da API
- Permitir que a aplicação seja executada com `uvicorn`

### 🛠️ Criar um recurso de livros e listar os itens

#### Descrição
Implemente uma rota para retornar uma lista de livros em formato JSON e preparar os dados iniciais do recurso.

#### Requisitos
O programa concluída deve:

- Criar uma lista em memória com pelo menos 2 ou 3 livros
- Definir uma rota `GET /books` para devolver todos os itens
- Garantir que cada item tenha `id`, `title`, `author` e `price`
- Retornar respostas em JSON válidas

### 🛠️ Adicionar a criação de novos livros

#### Descrição
Permita que o cliente envie dados de um novo livro por meio de uma requisição `POST` e armazene o item na lista em memória.

#### Requisitos
O programa concluído deve:

- Definir um modelo de dados com `title`, `author` e `price`
- Criar uma rota `POST /books` para receber o payload JSON
- Validar que os campos obrigatórios estão presentes
- Adicionar o novo livro à lista em memória
- Retornar o livro recém-criado com código HTTP `201`

### 🛠️ Explorar a documentação interativa da API

#### Descrição
Use a documentação automática gerada pelo FastAPI para testar os endpoints de maneira rápida e visual.

#### Requisitos
O programa concluído deve:

- Acessar a documentação automática em `/docs`
- Confirmar que os endpoints aparecem corretamente na interface
- Verificar que as rotas e parâmetros são documentados pelo framework
- Testar a API manualmente usando a interface Swagger UI

## ✅ Dica de aprendizado

FastAPI combina simplicidade com produtividade. Em vez de escrever muito código manual para validar entradas e gerar documentação, o framework cuida disso automaticamente a partir dos modelos e rotas que você define.
