p1 = int(input('Coloque a nota da p1'))
p2 = int(input('Coloque a nota da p2'))
media = (p1 + p2)/2

if (p1 + p2)/2 >= 5:
    print('Aprovado',media) 
elif (p1 + p2)/2 < 5 and (p1 +p2)/2 >=2:
    print('Faça a p3',media)
else:
    print('Reprovado',media)

# print(f'Aprovado {media}')]
# print('Aprovado' + "Sua media foi:" + str(media))
