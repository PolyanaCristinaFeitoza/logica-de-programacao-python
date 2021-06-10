real = float(input('Quantos reais você tem na carteira? R$ '))
euro = real / 6.65
print('Com R$ {:.2f} você pode comprar E{:.2f}'.format(real, euro))
