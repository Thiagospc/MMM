rom statistics import mode, median
lista = []
for numero in lista:
    if numero in lista:
        lista2.apend(numero)
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
lista_sem_numeros_repetidos = []
for numero in lista:
  if numero not in lista_sem_numeros_repetidos:
    lista_sem_numeros_repetidos.append(numero)

if len(lista_sem_numeros_repetidos) == len(lista):
    moda = '-'
else:
    moda = mode(lista)

# print()
print('*************************')
print('* Média: {:.2f}'.format(med))
print('* Mediana: {:.2f}'.format(mediana))
print('* Moda: {}'.format(moda))
print('*************************')
