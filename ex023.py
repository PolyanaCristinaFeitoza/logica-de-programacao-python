numero = int(input('Informe um número: '))
u = numero // 1 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(u))
d = numero // 10 % 10
print('Dezena: {}'.format(d))
c = numero // 100 % 10
print('Centena: {}'.format(c))
m = numero // 1000 % 10
print('Milhar: {}'.format(m))


