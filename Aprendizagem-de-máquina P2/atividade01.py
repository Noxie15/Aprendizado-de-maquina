dias_da_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
vendas_por_dia = {}

for dia in dias_da_semana:
    vendas = float(input(f'Digite o valor da venda para {dia}: '))
    vendas_por_dia[dia] = vendas
média = sum(vendas_por_dia.values()) / len(vendas_por_dia)
print('Vendas registradas:', vendas_por_dia)
print('Total de vendas:', sum(vendas_por_dia.values()))
print('Melhor dia de vendas:', max(vendas_por_dia, key=vendas_por_dia.get))
print('Pior dia de vendas:', min(vendas_por_dia, key=vendas_por_dia.get))
print(f'Média de vendas:', média)

for dia, vendas in vendas_por_dia.items():
    if vendas > média:
        print(f'Dias acima da média: {dia}: {vendas}')