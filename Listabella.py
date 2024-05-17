lista = ["a", "e", "i", "o", "u"]

lista2 = ["a", "b", "a", "c", "a", "t", "e"]

lista3 = ["a", "b", "a", "n", "a", "m", "o", "s"]

print(lista[1::3])

print(lista2[5:])

print(lista3[:5:2], lista3[5:7])


carros = ["golzinho", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}, {carro}")