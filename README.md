# 🩸 Cadastro de Doadores de Sangue

Sistema desenvolvido em Python para realizar o cadastro de doadores de sangue, validar informações fornecidas pelo usuário e verificar automaticamente sua elegibilidade para doação com base nas regras estabelecidas.

## 📌 Objetivo

Este projeto foi criado com fins educacionais para praticar conceitos fundamentais de desenvolvimento em Python, incluindo:

* Estruturas condicionais
* Estruturas de repetição
* Funções
* Manipulação de arquivos JSON
* Organização e modularização de código
* Tratamento de exceções

## 🚀 Funcionalidades

* Cadastro de doadores
* Validação de peso e altura
* Cálculo automático da idade
* Verificação de elegibilidade para doação
* Persistência de dados em arquivo JSON
* Listagem de doadores cadastrados
* Menu interativo para navegação no sistema

## 🧠 Regras de Elegibilidade

Para ser considerado apto à doação, o candidato deve atender aos seguintes critérios:

* Possuir peso mínimo de 50 kg
* Ter entre 16 e 69 anos de idade

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON
* Módulo datetime
* Módulo os

## ▶️ Como Executar

Clone o repositório:

```bash
git clone https://github.com/lucasvieirafelisberto/cadastro-doadores-sangue.git
```

Acesse a pasta do projeto:

```bash
cd cadastro-doadores-sangue
```

Execute a aplicação:

```bash
python main.py
```

## 📁 Estrutura do Projeto

```text
cadastro-doadores-sangue/
│
├── main.py
│
├── data/
│   └── doadores.json
│
└── README.md
```

## 📷 Exemplo de Uso

```text
======= MENU =======
1 - Cadastrar doador
2 - Listar doadores
3 - Sair
```

## 🔧 Melhorias Futuras

* Interface gráfica com Tkinter
* Desenvolvimento de API com Flask
* Integração com banco de dados SQLite ou PostgreSQL
* Exportação de relatórios
* Busca e edição de doadores

## 👨‍💻 Autor

Lucas Vieira Felisberto

Projeto desenvolvido para fins de estudo e prática da linguagem Python.
