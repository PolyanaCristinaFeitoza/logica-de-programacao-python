primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota: '))
media = (primeira + segunda) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(primeira, segunda, media))
if media < 5.0:
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif media >= 7.0:
    print('O aluno está APROVADO!')

