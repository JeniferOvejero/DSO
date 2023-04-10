from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia
from Imovel import Imovel


locat1 = Locatario(1,'jen',111)
locat2 = Locatario(2,'joao',121)

imovel1 = Imovel(0,'a',3.2,None)

imovel1.incluir_locatario(locat1)
imovel1.incluir_locatario(locat1)

imovel1.incluir_mobilia(145,'mesa')
imovel1.excluir_mobilia(145)
imovel1.incluir_mobilia(145,'mesa')
imovel1.incluir_mobilia(123,'cadeira')

for mob in imovel1.mobilias:
    print(mob.descricao)

imovel1.excluir_locatario(1)

print(imovel1.locatarios)