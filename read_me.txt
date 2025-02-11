READ ME - Formação Python Developer

ink documentação flask: https://flask.palletsprojects.com/en/stable/tutorial/layout/
github: https://github.com/digitalinnovationone/trilha-python-dio

Contextualização do Python:

Foi lançado em 1889, em sua primeira versão, com intuito de ser acessível e fácil igual a linguagem ABC

Em 1995, foi lançado o Python 2.0

Em 2008 foi lançado o Python 3

Depois disso, o criador Guido Van Rossum se aposentou e a Microsoft contratou ele depois dos anos 2015 para dar continuidade no Python e melhorar a performance
Hoje, possui um time na microsoft exclusivo para desenvolverem o Python.

#Pip 
Gerenciador de bibliotecas oficial do Python, instala todas as bibliotecas do site PyPi (Python Package Index) pypi.org

pip install numpy
pip uninstall numpy
pip list - mostra todos os pacotes instalados dentro do python ativo ou ambiente virtual
pip install --upgrade numpy

Ambientes Virtuais (mantêm a dependência dos projetos)

python -m venv .env - criar um ambiente virtual
.env\Scripts\activate.bat - para ativar o ambiente virtual no CMD
mkdir "nome pasta" para criar a pasta
ls .env - lista os conteúdos da pasta
deactivate - desativa o ambiente virtual


#Pipenv
Ferramenta de gerenciamento de pacotes que combina a dependência com a criação de ambiente virtual, um upgrade do PIP
pip install Pipenv
pipenv install numpy
pipenv uninstall numpy
pipenv lock
pipenv graph - lista todas as dependências dos pacotes
pipenv clean - desinstala as dependências (não são desinstaladas oo uninstall)
#Poetry

pip install poetry - instalar o poetry
poetry new project - criar um novo projeto
poetry add numpy
poetry remove numpy


poetry init (para projetos que já existem)
fará algumas perguntas sobre a configuração
"package to add or search for (leave blank to skip): django
[0] Django
[1] django-503
[2] django-filebrowser-django13
..

Depois disso, cria um projeto pyproject.toml igual o pipfile.lock, mostra as configurações, bibliotecas de dependências, pacotes...
poetry show --help - mostra os comandos
poetry show -t - mostra as dependências das bibiliotecas



--------
#Boas Práticas em Python

PEP - Propostas de Melhoria do Python
- mais conhecida é a PEP 8, que cobre o estilo de codificação, guia de estilo
https://peps.python.org/pep-0008/


Principais Recomendações

- 4 espaços para identação
- limitar as linhas a 79 caracteres
- usar nomes de variáveis em snake_case para functions e variaveis
- CamelCase para classes

Exemplo:

def somar(argumento_1 , argumento_2):
    pass

class ContaBancaria:
    pass

Para não esquecer, utilizamos algumas ferramentas de checagem de estilo como o "flake8"

pip install flake8
flake8 meu_script.py

Segunda opção, com formatadores, formatação automática de código

"Black" reformata todo o arquivo em um estilo consistente, simplificando a tarefa de manter a conformidade com a PEP 8

pip install black
black meu_script.py

Outro exemplo, é o "Isort", em específico para corrigir importações

bibliotecas padrões da linguagem vem antes da importação de módulos, ordem alfabéticas..
import mypkg.sibling
from pypkg import sibling
from mypkg.sibling import example

pip install isort
isort meu_script.py

l
-------------------------------------------------------------------

CRUD com flask e SQLAlchemy, verificar no github.


-------------------------------------------------------------------

Instalando o Migrate
flask --app src.app db init -- criar a pasta do migrations (com os arquivos alembic, env, template de como as versões são criadas...)
nossas versões dos scripts do DB vem na pasta versions

flask --app src.app db migrate -m "Initial migration." --subindo toda a versão atual na pasta versions

flask  --app src.app db upgrade -- para aplicarmos a migração e ativá-la.
migrate sempre salva a sequência das migrações, exemplo, ele liga uma a outra em versões e números de versões.

flask --app src.app db migrate -m "Add active attr in user" - (attr = atribute), gerando uma nova migração após alteração no user
flask  --app src.app db upgrade -- para aplicarmos a migração e ativá-la.

para voltar a versão caso dê algum problema:
flask --app src.app db downgrade -- senão falarmos qual versão queremos, ele sempre remove de 1 em 1

flask --app src.app db current -- retorna a migração atual

flask --app src.app db check - mostra se tem alterações pendentes

---------------------------------------------------------------

Autenticação

Processo de verificar a identidade de um usuário. É como o sistema reconhece quem você é.
"Eu provo quem eu disse ser"

Autorização

Uma vez autenticado, a autorização determina quais recursos são liberados para o usuário acessar.
É complementar a autenticação, para entrar na autorização eu primeiro devo estar autenticado.


JWT (JSON Web Tokens)

É um padrão aberto RFC 7519 que define uma maneira compacta e independente de transmitir informações de formas seguras entre objetos JSON.

--------------------

Manipulação de Arquivos

Open() e close()

somente leitura 'r' (só para ler)
gravação 'w' (vou abrir para escrever)
anexar 'a' (vou abrir um arquivo e colocar mais contéudo dentro)

file = open('example.txt','r')
print(file.read())
file.close()

exemplo com readlines
for linha in arquivo.readlines():
    print(linha)
read lê tudo e traz, readline lê uma linha por vez, já o readlines retorna uma lista


# Tip - Dica
como usar mesmo assim o readline
while len(linha := arquivo.readline()):
    print(linha)

    (se o len retornar 0, a linha é vazia, então acaba o while)



arquivo.write("escrevendo dados")
arquivo.writelines("["escrevendo","\n","teste"])
arquivo.close()

Manipulando diretórios

import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__) # devolve qual é o arquivo
print(ROOT_PATH.parent) # arquivo acima da pasta, assim não pega o nome do arquivo
os.mkdir(ROOT_PATH / 'novo-diretorio')

arquivo = open(ROOT_PATH / "Novo.txt", "w")

arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

shutil.move("source.txt", "caminho")

Tratando exceções:


ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except FileNotFoundError as exc:
    print("arquivo não encontrado")
except IsADirecotryError as exc:
    print("não foi possível abrir o arquivo")
except FileNotFoundError as exc:
    print("erro ao abrir o arquivo")
except Exception as exc:
    print("Algum problema ocorreu ao abrir o arquivo")


Boas práticas ao usar python

with open('arquivo.txt','r') as arquivo: / assim abre e já fecha o arquivo

try:
    with open('arquivo.txt','r') as arquivo:
except IOError as exc:
    print(f"erro ao abrir o arquivo: {exc}")


Manipulando arquivos CSV:
import csv

writer = csv.writer(file)
writer = csv.reader(file)
try: 
    with open('arquivo.txt','w',newline="",encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id","nome"])

except IOError as exc:
    print(f"erro ao abrir o arquivo: {exc}")

exemplo CSV com dicionário

try: 
    with open('arquivo.txt','w',newline="",encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            print(row["ID"],row["name"])

except IOError as exc:
    print(f"erro ao abrir o arquivo: {exc}")
