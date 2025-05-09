Dicionario_funcionarios = {}

contador = 0
while contador < 6:
    nome = input(f'Digite o nome do funcionário {contador + 1}: ').lower()
    salario = float(input('Digite o salário: '))
    Dicionario_funcionarios[nome] = salario
    contador += 1

print('\nLista de funcionários atualizada:')
for nome, salario in Dicionario_funcionarios.items():
    print(f'{nome.capitalize()}: R$ {salario:.2f}')
    
# # Primeiro funcionário
# nome = input('Digite o nome de um funcionario: ').lower()
# salario = float(input('Digite o salario: '))
# Dicionario_funcionarios[nome] = salario

# print('Lista de funcionários atualizada:', Dicionario_funcionarios)

# # Segundo funcionário
# nome = input('Digite o nome de outro funcionario: ').lower()
# salario = float(input('Digite o salario: '))
# Dicionario_funcionarios[nome] = salario

# print('Lista de funcionários atualizada:', Dicionario_funcionarios)

# Consulta
funcionario_solicitado = input('Digite o nome de um funcionario para consultar o salário: ').lower()
if funcionario_solicitado in Dicionario_funcionarios:
    print(f'O funcionário {funcionario_solicitado} ganha: R$ {Dicionario_funcionarios[funcionario_solicitado]:.2f}')
else:
    print('O funcionário não foi encontrado.')
