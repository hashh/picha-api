API:

API Picha 2.0.4.

Pré requisitos:
 * Python3;
 * pip/pip3; -- Estes serão instalados pelo venv com o comando de criação.
 * Pacote venv do python para criação de ambiente virtual; -- apt-get install python3-venv
 * Redis: https://redis.io/download; -- Site com os passos para instalação

 * Lembresse verificar se todos pré requisitos estão instalados.

Procedimentos para que a api possa rodar na sua máquina linux:

* Primeiramente, vamos criar uma ambiente virtual para que as novas instações fiquem num ambiente controlado.
 - Escolha uma pasta para seu projeto.
 - abra esta pasta no terminal, e execute o seguite comando > python3 -m venv .venv
   Caso não funcione, você provavelmente precisara instalar o pacote venv antes:
	* apt-get install python3-venv
 
 - Após criar o ambiente, vamos clonar o repositorio. Abra a pasta do seu projeto(a mesma onde criou o ambiente virtual) e execute:
	* git clone https://github.com/hashh/picha-api.git
 - Vamos ativar o venv. Abra o terminal na pasta de criação do venv e digite: source .venv/bin/activate

  - Após clonar o repositório e ativarmos o venv, precisamos instala as dependendias e rodar as migrations do projeto. Existe a possibilidade de ocorrer um erro ao instalar as dependências, precisamos ter certeza que um pacote esta presente. Rodaremos o seguinte comando: "pip install wheel"
Repita este para o pip3 por garantia.
 - Agora, para instalarmos as dependências, rodaremos o seguinte comando dentro da pasta raiz da API: pip install -r requeriments.txt
 - Agora rodaremos as migrations com o comando: python3 manage.py migrate.
 - Prontinho. Basta rodar o servidor para ter acesso a API: python3 manage.py runserver.

 - O projeto Picha, possui um "asynchronous task queue/job", chamado Celery, que é responsável por rodar rotinas periodicamente. Estas rotinas irão inserir a última imagem do Flickr(utilizando a Flickr API). Para rodarmos essas rotinas, precisamos executar os seguintes comandos, um em cada terminal separadamente(Precisamos estar dentro do nosso venv para tal):
	* celery -A picha worker -l info
	* celery -A picha beat -l info

 - Esta rotina está configurada para buscar uma imagem a cada minuto, a fim de que os testes sejam mais rápidos. Caso queira aumentar o tempo, acesse o arquivo tasks.py no app photos e altere o tempo em "run_every=(crontab(minute='*/1')),".


foi necessário atualizar as dependencias por conta da ultima versao do redis. Então celery e suas dependências tbm estão em versões superiores.
