# Prova 1 do Módulo 10 - Felipe Campos

## Explicação

### Organização das pastas

```
.
├── collection_insomnia.json
├── docker-compose.yaml
├── README.md
├── src
│   ├── database
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemes.py
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt

```

- A pasta src contém todos os códigos da aplicação, sendo composta por um Dockerfile para criar a imagem do Back-End, main.py, o arquivo de execução principal, requirements.txt para instalar as depedências e o diretório database, onde se encontram os modelos e esquemas para estruturam o banco de dados.
- collection_insomnia.json contém a documentação da API
- docker-compose.yaml: lança os containers da aplicação

### Rotas 

Nesta prova foi proposto que os alunos criassem um Back-End de uma aplicação, com rotas a fim de realizar o CRUD de um pedido. Para isso foram desenvolvidas 5 rotas, elas são:

- **GET**: /pedidos
- **GET**: /pedidos/id 
- **POST** /novo
- **PUT**: /pedidos/id
- **DELETE**: /pedidos/id

Essas rotas, respectivamente, pegam todos os pedidos, pegam um pedido apenas, adiciona um novo pedido, atualiza um pedido e remove um pedido.

### Dockerização

Também foi solicitado que os alunos dockerizassem suas soluções. Dado isso, um docker-compose foi criado, que lança dois containers, um do Back-End e outro do Banco de Dados. Para armazenar as informações, foi utilizado Postgres, a partir de uma imagem puxada no próprio docker-compose. Além disso, uma imagem é criada para dar suporte ao container do Back-End, uma vez que é necessário baixar diversas depedências a fim de executar o a aplicação.

## Como rodar

Primeiro é necessário clonar o repositório para facilitar a execução:

```
git clone https://github.com/FelipeCampos14/p1-modulo10.git
```

Após isso, basta rodar o docker-compose que ele irá lançar os containers da aplicação:

```
docker compose up --build
```
