""" Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequência
 de fibonancci.
 Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
 """
print('\033[032m-\033[0m' * 30)
print('    SEQUÊNCIA DE FIBONACCI ')
print('\033[032m-\033[0m' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('\033[032m{}\033[0m -> \033[032m{}\033[0m '.format(t1, t2), end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> \033[032m{}\033[0m'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> \033[033mFIM\033[0m')
