READ ME - Formação Python Developer

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
source .env/bin/activate - para ativar o ambiente virtual
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

Para não esquecer, tilizamos algumas ferramentas de checagem de estilo como o "flake8"

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