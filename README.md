# GVcsv
Gestor de Vulnerabilidades

### Objetivo
Exibir uma listagem de vulnerabilidades para facilitar a decisão de prioridade.

## Instalação
Criar o clone do projeto:

```bash
git clone https://github.com/JosueSantos/GVcsv.git
```

Crie o arquivo .env dentro do diretório gv/ com as variáveis abaixo como conteúdo

```bash
DEBUG=False
SECRET_KEY='6(fjjoj&yr(@4tnax5mhd^o7*gsy8e0^+#81lw%!3x(l%+%*^c'
```

Prepare o Banco de dados com o comando:

```bash
python manage.py migrate
```

Crie o SuperUser

```bash
winpty python manage.py createsuperuser
```

Execute o Projeto

```bash
python manage.py runserver
```

## Arquitetura

Utilizando o Django como tecnologia principal, GV foi desenvolvido com um desacoplamento do frontend com o backend. Possuindo para a conexão, funções que são disponibilizadas pelo backend para a gestão dos dados.

## Acesso ao Projeto
* Acesse a url do server;

* No navegador utilize o usuário que você criou como SuperUser;

* Selecione o arquivo CSV e clique em Upload;
O arquivo deve possui o seguinte cabeçalho de colunas:

    - ASSET - HOSTNAME
    - ASSET - IP_ADDRESS
    - VULNERABILITY - TITLE
    - VULNERABILITY - SEVERITY
    - VULNERABILITY - CVSS
    - VULNERABILITY - PUBLICATION_DATE


* Foi desenvolvido um serviço de bulk_create para melhorar o desempenho da população dos dados, onde o acesso ao banco de dados se faz a partir de um limite de registros estipulado;

* É exibido uma tabela com a Média de Risco Por Hostname, com filtro e paginação;

* Logo mais abaixo outra tabela com todos os dados importados do arquivo CSV e um check clicável para a remoção das vulnerabilidades corrigidas, com os mesmos filtros e paginação da tabela anterior;

* Um detalhe quando a segurança foi a mudança das configurações para um arquivo .env, que não vem como padrão da primeira instalação de um projeto django e a obrigação da autenticação para acessar qualquer rota.

* E quanto à estrutura, foi desacoplado o frontend do backend. O front só tem acesso a algumas funções criadas especificamente para este relacionamento front-back.


