numeros =[]
clasificar = lambda numeros1:numeros1>10

for i in range(5):
    numero = int(input("digite un numero: "))
    mayores = clasificar(numero)
    numeros.append(mayores)

print(numeros)