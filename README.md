# Sistema E-Shop Brasil - Big Data e MongoDB

## Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de Advanced Databases and Big Data, com o objetivo de simular um sistema real de comércio eletrônico (e-commerce), inspirado na empresa fictícia E-Shop Brasil.

A aplicação demonstra como tecnologias modernas de banco de dados e análise de dados podem ser utilizadas para melhorar a gestão, personalização e tomada de decisões em um ambiente de vendas online.

---

## Objetivo

Desenvolver uma solução prática utilizando:

* Banco de dados NoSQL (MongoDB)
* Interface interativa com Streamlit
* Ambiente containerizado com Docker

A aplicação simula operações reais de um e-commerce, como:

* Cadastro de produtos e clientes
* Criação de pedidos
* Visualização e análise de dados
* Dashboard com métricas e insights

---

## Tecnologias Utilizadas

* Python
* Streamlit
* MongoDB
* Docker
* Pandas
* Plotly

---

## Funcionalidades

### Produtos

* Cadastro de produtos
* Listagem de produtos
* Exclusão de produtos

### Clientes

* Cadastro de clientes

### Pedidos

* Criação de pedidos (cliente + produto)
* Visualização dos pedidos

### Dashboard

* Total de produtos cadastrados
* Soma total de preços
* Produtos por categoria
* Produtos mais caros
* Produtos mais baratos
* Análise de pedidos por cliente

---

## Estrutura do Projeto

```text
projeto/
 ├── app.py
 ├── docker-compose.yml
 ├── README.md
 └── exemplos/
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

### 2. Subir o MongoDB com Docker

```bash
docker-compose up -d
```

---

### 3. Instalar dependências

```bash
pip install streamlit pymongo pandas plotly
```

---

### 4. Executar a aplicação

```bash
streamlit run app.py
```

---

## Testes e Demonstração

A aplicação permite:

* Inserção de dados simulados
* Manipulação de dados (CRUD)
* Visualização em tempo real
* Análise de dados via dashboard

As imagens de demonstração devem ser adicionadas na pasta "exemplos".

---

## Segurança e LGPD

O projeto considera boas práticas relacionadas à proteção de dados, como:

* Organização dos dados em coleções separadas
* Estrutura escalável
* Base para futuras implementações de autenticação e criptografia

---

## Aplicação de Big Data

Este projeto demonstra conceitos de Big Data, como:

* Análise de grandes volumes de dados (simulados)
* Identificação de padrões de consumo
* Apoio à tomada de decisão
* Estrutura escalável com MongoDB

---

## Vídeo Pitch

Inserir aqui o link do vídeo explicativo do projeto.

---

## Autor

Lucas Moura
Curso: Gestão da Tecnologia da Informação

---

## Conclusão

Este projeto demonstra como a integração entre bancos de dados NoSQL, visualização de dados e ferramentas modernas pode gerar soluções eficientes para problemas reais de e-commerce, contribuindo para a melhoria da experiência do usuário e da gestão operacional.
