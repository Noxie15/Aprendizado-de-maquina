# while True:
#     try:
#         nota1 = int(input('Digite a nota da P1 [Enter]:'))
#         if not 0 <= nota1 <=10:
#             raise ValueError ('Somente número de 0 a 10')
#     except ValueError as e: 
#         print('Favor informal um número! Erro interno:', e)
#     else:
#         break

# while True:
#     nota2 = input('Digite a nota da P2 [Enter]:')
#     if nota2.isnumeric():
#         if(int(nota2) >=0) and (int(nota2) <=10):
#             break
#         else:
#             print('Digite uma nota entre 0 a 10')
#             continue
#     else:
#         print('Digite um número valido')
        
# media = (nota1 + int(nota2)) / 2
# print(f'Média: {media:.2f}')

# lista_1 = [2,4,6,8,10]
# lista_2 = [1,3,5,6,9,11]
# valores_lista = lista_1 + lista_2 
# print('lista', valores_lista)

# valores_lista[1] = (input('digite um número'))
# print('Alterar um valor:',valores_lista)

# valores_lista.append(int(input('Digite um numero')))
# print('Incluiu um valor:', valores_lista)

# valores_lista.insert(0,input('Digite um numero:'))
# print('inseriu um valor na posição',valores_lista)

# valores_lista.remove(int(input('digite um número')))
# print('remove um valor especifico:', valores_lista)

# valores_lista.pop(int(input('digite um indice da lista')))
# print('remove um valor na posição', valores_lista)
                                                               
# print(sum(valores_lista))
# print(len(valores_lista))
# print(min(valores_lista))
# print(max(valores_lista))
# soma = 0
# for valores_lista in valores_lista:
#     soma += valores_lista
#     print (soma)   

dicionario_precos = {'salgado':5.50, 'cafe':4.20, 'suco':9.15, 'torta':16.60} 
# produto_solicitado = input('Digite o nome do produto da cantina:')
# produto_solicitado = produto_solicitado.lower()
# print('Atualmente existe estes produtos', dicionario_precos)

nome = input('Digite uma comida:')
valor = input('Digite um preco:')
dicionario_precos[nome] = float(valor)

print('lista de produtos atualizada:',dicionario_precos) 

# for produtos in dicionario_precos:
#     print(produtos)

# for produto, valor in dicionario_precos.items():
#     print(produto, valor)