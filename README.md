# SiBaHo
Sistema de Banco de Horas

#Sumário
* [Dependências](https://github.com/eliseuegewarth/sibaho/tree/master#dependências)
* [Configuração de Ambiente](https://github.com/eliseuegewarth/sibaho/tree/master#configuração-de-ambiente)

#Dependências

* [Python 3.5](https://www.python.org/downloads/release/python-350/)
* Django 1.10.4 [Configuração de Ambiente](https://github.com/eliseuegewarth/sibaho/tree/master#configuração-de-ambiente)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

# Configuração de Ambiente
  ...(Após clonar o projeto em sua maquina)...
  
  Crie um ambiente virtual com o seguinte comando:
  ```bash
  mkvirtualenv -p python3.5 -a path/to/sibaho/ -r requirements.txt nome_da_Virtualenv
  ```
  Esse comando irá:
  * Criar uma Virtualenv  com o nome (nome_da_Virtualenv) que voce colocar;
  * Configurar o python3.5 como default;
  * Colocar o diretório (path/to/sibaho/) como default (entrará automaticamente no diretório ao usar `workon nome_da_Virtualenv`);
  * Executar o comando `pip install -r requirements.txt`.
  
