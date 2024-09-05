list_numeros = []
for n in range(1, 1065, 1):
    aux_n = n
    aux_n = str(aux_n)
    list_numeros.append(f'{aux_n.ljust(8)}')

print(list_numeros)
with open('numeros.txt', 'w') as numeros:
    numeros.writelines(list_numeros)