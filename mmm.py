from statistics import mode, median
lista = []
while True:
    v = float(input('Número :> '))
    lista.append(v)
    r = str(input('Deseja continuar? [S/N] :> ')).upper()
    if r == 'N':
        break
    elif r == 'S':
        continue
    else:
        print('Digite um valor válido!')
quantidade = len(lista)

# média
med = sum(lista) / quantidade

# mediana
mediana = median(lista)
# moda
moda = mode(lista)

# print()
print(f'Média: {med}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
