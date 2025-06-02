#AULA 07

#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
#CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA,
#SABENDO QUE QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M²

largura = float(input('Qual a largura da sua parede? '))
altura = float(input('Qual a altura da sua parede? '))

area = altura * largura
tinta = area / 2 #cada 2m² usa 1 litro de tinta

print(f'A sua parede tem uma area de {area:.3f}m² e será necessario {tinta:.1f}l de tinta para pintá-la')