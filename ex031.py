distancia = float(input('Qual é a dstância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco2 = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco2))
#preco = distancia * 0.50 if distancia <= 200 else distancia * 0,45



