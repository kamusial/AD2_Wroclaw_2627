lista_aut = ['audi', 'toyota', 'bmw', 'citroen', 'fiat']
model = input('Podaj model:   ')

for i in range(len(lista_aut)):
    if lista_aut[i] == model:
        print(f'Mamy {lista_aut[i]}')

for auto in lista_aut:
    if auto == model:
        print(f'Mamy {auto}')

if model in lista_aut:
    print(f'Mamy {model}')
else:
    print(f'Niestety nie mamy {model}')
