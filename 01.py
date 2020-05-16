# Faça um programa que leia 1 número e em seguida pergunte ao usuário qual operação ele
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número
# é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.
n = input('Digite um número\n')
number = 0
if '.' in n:
    number = float(n)
else:
    number = int(n)
print('Qual operação deseja realizar')
print('-'*50)
print('1-Para saber se o número e par ou impar')
print('2-Para saber se o número é positivo ou negativo')
print('3-Para saber se o número é inteiro ou decimal')
print('-'*50)
op = int(input())

if op == 1:
    res = number % 2
    if res == 0:
        print('par')
    else:
        print('impar')
elif op == 2:
    if number > 0:
        print('positivo')
    else:
        print('negativo')
elif op == 3:
    if type(number) == float:
        print('Decimal')
    else:
        print('Inteiro')