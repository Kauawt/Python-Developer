# 1) Receber dois dados diferentes do usuário e concatená-los em uma única string
def concat_data():
    valor1 = input("Digite o primeiro dado: ")
    valor2 = input("Digite o segundo dado: ")
    return print(f"Resultado da concatenação: {valor1 + valor2}")


# concat_data()

# 2) Solicitar uma string e um número inteiro como entrada. Depois retornar a string repetida o número de vezes informado.


def repetir_texto():
    texto = input("Digite uma string: ")
    numero = int(input("Digite um número inteiro: "))
    return print(texto * numero)


# repetir_texto()

# 3) Solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.


def operacoes_matematicas():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha uma operação (+, -, *, /): ")
    if operacao == "+":
        return print(numero1 + numero2)
    elif operacao == "-":
        return print(numero1 - numero2)
    elif operacao == "*":
        return print(numero1 * numero2)
    elif operacao == "/":
        return print(numero1 / numero2)
    else:
        return "Operação inválida!"


# operacoes_matematicas()

# 4) Verificar se um número é par ou ímpar.


def verificar_par_impar():
    numero = int(input("Digite um número inteiro: "))
    return print("Par") if numero % 2 == 0 else print("Ímpar")


verificar_par_impar()

# 5) Calcular média de notas


def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    return print((nota1 + nota2 + nota3) / 3)


calcular_media()

# 6) Verificar palíndromos


def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    return print(palavra == palavra[::-1])


verificar_palindromo()
