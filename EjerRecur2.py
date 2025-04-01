# Definir la función sublista, que dada una lista de enteros, un
# número que represente una posición y otro número que
# represente una longitud, devuelva una lista de enteros (que
# se basa en la lista dada) que comience en la posición dada y
# que tenga la longitud dada desde esa posición (pila)

def sublista(lista: list[int], posicion: int, longitud: int) -> list[int]:
    if longitud == 0 or posicion >= len(lista):
        return []
    elif posicion < 0:
        return sublista(lista, 0, longitud)
    else:
        return [lista[posicion]] + sublista(lista, posicion + 1, longitud - 1)
    
print(sublista([1, 2, 3, 4, 5], 2, 3))  # [3, 4, 5]    
    
# de cola   

def sublista_cola(lista: list[int], posicion: int, longitud: int, acumulador: list[int] = None) -> list[int]:
    if acumulador is None:
        acumulador = []
    if longitud == 0 or posicion >= len(lista):
        return acumulador
    elif posicion < 0:
        return sublista_cola(lista, 0, longitud, acumulador)
    else:
        return sublista_cola(lista, posicion + 1, longitud - 1, acumulador + [lista[posicion]])

print(sublista_cola([1, 2, 3, 4, 5], 2, 3))  # [3, 4, 5]

# interativa

def sublista_iterativa(lista: list[int], posicion: int, longitud: int) -> list[int]:
    if longitud == 0 or posicion >= len(lista):
        return []  
    elif posicion < 0:
        return sublista_iterativa(lista, 0, longitud)
    else:
        sublista = []
        for i in range(posicion, min(posicion + longitud, len(lista))):
            sublista.append(lista[i])
        return sublista

print(sublista_iterativa([1, 2, 3, 4, 5], 2, 3))  # [3, 4, 5]  

# Definir la función esPalindromo, que dada una lista de
# enteros, retorne si es o no es palíndromo, utilizando
# recursividad explícita.

def es_palindromo(lista: list[int]) -> bool:
    def es_palindromo_interno(lista: list[int], inicio: int, fin: int) -> bool: 
        if inicio >= fin:
            return True
        elif lista[inicio] != lista[fin]:
            return False
        else:
            return es_palindromo_interno(lista, inicio + 1, fin - 1)
    return es_palindromo_interno(lista, 0, len(lista) - 1)  

print(es_palindromo([1, 2, 3, 2, 1]))  # True

#Definir la función aplanar, que dada una lista de listas de enteros, 
#retorne un lista de enteros que corresponda a la concatenación de elementos-lista
#de la lista original. Por ejemplo: aplanar([[5,7], [], [3,7,2], [9]) = [5,7,3,7,2,9]

def aplanar(lista: list[list[int]]) -> list[int]:
    if not lista:
        return []       
    elif not lista[0]:
        return aplanar(lista[1:])   
    else:   
        return lista[0] + aplanar(lista[1:])

lista_de_listas = aplanar([[5, 7], [], [3, 7, 2], [9]])
print(lista_de_listas)  # [5, 7, 3, 7, 2, 9]        


# Implementar la función recursiva posiciones_pares, que dado una lista
# de enteros, imprima el contenido de sus posiciones pares

def posiciones_pares(lista: list[int], indice: int = 0) -> None:
    if indice >= len(lista):
        return
    if indice % 2 == 0:
        print(lista[indice])
    posiciones_pares(lista, indice + 1)

print(posiciones_pares([1, 2, 3, 4, 5]))  # Imprime 1, 3, 5
