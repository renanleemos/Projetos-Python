#                                             Como eu fiz:
# n1 = int(input('Digite um número: '))
# d = n1 * 2
# t = n1 * 3
# p = n1 ** 2
# print('O dobro de {} é {}, o triplo é {}, e sua raiz quadrada é {}'.format(n1, d, t, p))
# __________________________________________________________________
#                              Como o Guanabara fez (Com variáveis):
# n = int(input('Digite um número: '))
# d = n * 2
# t = n * 3
# r = n ** (1/2)
# print('O dobro de {} vale {}.'.format(n, d))
# print('O triplo de {} vale a {}. A raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

# Errei a raiz quadrada.
# __________________________________________________________________
#                              Como o Guanabara fez (Sem variáveis):
n = int(input('Digite um valor: '))
print('O dobro de {} vale {}.'.format(n, (n * 2)))
print('O triplo de {} vale a {}. \nA raiz quadrada de {} vale {:.2f}.'.format(n, (n * 3), (n), (n ** (1/2))))
