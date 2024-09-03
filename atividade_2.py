#lista inicial de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Filtrode  números pares 
numeros_pares = [numero for numero in numeros if numero % 2 == 0]

#Imprimindo a lista de números pares
print("Lista de números:", numeros)
print("Lista de números pares:", numeros_pares)

