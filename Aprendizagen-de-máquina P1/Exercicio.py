# nome1 =(input('Qual a sua cor favorita Maria'))
# print(f'Sua cor favorita e {nome1}')
# nome2 =(input('Qual a sua cor favorita Pedro'))
# print(f' Sua cor favorita e {nome2}')
# nome3 =(input('Qual a sua cor favorita André'))
# print(f' Sua cor favorita e {nome3}')
# nome4 =(input('Qual a sua cor favorita Camila'))
# print(f' Sua cor favorita e {nome4}')  

cores = [str,str,str,str]
for i in range(4):
    cores[i] = input('Digite sua cor favorita')
for i in range(4):
    print('As cores escolhidas foram', cores)