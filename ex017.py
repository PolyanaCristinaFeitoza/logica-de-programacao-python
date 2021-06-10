oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (oposto * oposto) + (adjacente * adjacente)
raizhipotenuza = hipotenusa ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(raizhipotenuza))

import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenuza vai medir {:.2f}'.format(hipotenusa))





