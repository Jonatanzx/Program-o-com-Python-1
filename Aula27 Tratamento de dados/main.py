'''
# print("Inicio")
# assert 1 < 0 "0 deve ser menor que 1"
# print("Fim")
'''

try:
    idade = int(input("Digite sua idade: "))

except:
    print("Digite somente numeros inteiros")

try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    resultado = n1 / n2
    print("O resultado é: ", resultado)

except ValueError:
    print("Somente numeros inteiros")

except ZeroDivisionError:
    print("Não pode ser 0")