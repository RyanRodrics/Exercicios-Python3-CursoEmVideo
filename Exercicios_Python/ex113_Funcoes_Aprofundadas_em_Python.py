# Ex113: Reescreva a função leiaInt() que fizemos no Ex104, incluindo agora a possibilidade da digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mERRO! Por favor digite um número inteiro válido\033[m")
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Por favor digite um número real válido\033[m")
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num1 = leiaInt("Digite um número inteiro:")
num2 = leiaFloat("Digite um número real: ")
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')
