# Definir la función desde_hasta con recursión de cola que
# dados dos números enteros retorne una lista de números
# consecutivos donde el primer elemento de la lista
# resultante sea el primer elemento dado, y el último
# elemento de la lista resultante sea el segundo elemento
# dado.
# Por ejemplo, si se invoca la función desde_hasta(3, 7)    
# debe retornar la lista [3, 4, 5, 6, 7].
from typing import List
def desde_hasta(inicio: int, fin: int) -> list[int]:
    def desde_hasta_interna(inicio: int, fin: int,lista_parcial = [int]) -> list[int]:
        if inicio > fin:
            return lista_parcial
        elif inicio == fin:
            return lista_parcial
        else:
            return desde_hasta_interna(inicio + 1, fin, lista_parcial + [inicio])    # Llama a la función interna con los parámetros iniciales
           
    return desde_hasta_interna(inicio, fin,[])  # Llama a la función interna con los parámetros iniciales

    
print(desde_hasta(3, 7))  # [3, 4, 5, 6, 7]
print(desde_hasta(1, 5))  # [1, 2, 3, 4, 5]
print(desde_hasta(5, 1))  # []

# Definir la función intercalar con recursión de pila, que
# dadas dos listas de enteros, retorne una lista de
# enteros que corresponda al intercalado elemento a
# elemento de las dos listas dadas.
# Por ejemplo, si se invoca la función intercalar([1, 2, 3], [4, 5, 6])
# debe retornar la lista [1, 4, 2, 5, 3, 6].

def intercalar(lista1: list[int], lista2: list[int]) -> list[int]:
    if not lista1 and not lista2:
        return []  # Ambas listas están vacías
    elif not lista1:
        return lista2  # Solo la segunda lista tiene elementos
    elif not lista2:
        return lista1  # Solo la primera lista tiene elementos
    else:
        return [lista1[0], lista2[0]] + intercalar(lista1[1:], lista2[1:])  # Intercala el primer elemento de cada lista

print(intercalar([1, 2, 3], [4, 5, 6]))  # [1, 4, 2, 5, 3, 6]
print(intercalar([1, 2], [3, 4, 5]))  # [1, 3, 2, 4, 5] 
print(intercalar([], [1, 2, 3]))  # [1, 2, 3]


#Eliminar la recursión del siguiente código:
def longitud_recursiva(lista:list[int], contador=0) -> int:
    if not lista:
        return contador
    else:
        return longitud_recursiva(lista[1:],contador+1)

def longitud_iterativa(lista:list[int], contador=0) -> int:
    while lista:
        contador += 1
        lista = lista[1:]
    return contador

mi_lista = [1, 2, 3, 4, 5]
longitud = longitud_iterativa(mi_lista)
print(f"La longitud de la lista es: {longitud}")

# Implementar una versión con recursión de
# cola que produzca el resultado esperado al
# pasar una lista: `suma_resta_alternada([1, 2,
# 3, 4, 5]) = 1 + 2 - 3 + 4 - 5

def suma_resta_alternada(lista: list[int]) -> int:
    def suma_resta_alternada_interna(lista: list[int], acumulador: int, signo: int) -> int:
        if not lista:
            return acumulador
        else:
            return suma_resta_alternada_interna(lista[1:], acumulador + signo * lista[0], -signo)

    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    else:
        return suma_resta_alternada_interna(lista[1:], lista[0], 1)

print(suma_resta_alternada([1, 2, 3, 4, 5]))  # 1 + 2 - 3 + 4 - 5 = -1    

# Implementar una versión iterativa
def suma_resta_alternada_iterativa_while(lista: List[int]) -> int:
    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        return lista[0] + lista[1]
    else:
        acumulador = lista[0] + lista[1]
        signo = -1
        indice = 2
        while indice < len(lista):
            acumulador += signo * lista[indice]
            signo *= -1
            indice += 1
        return acumulador

print(suma_resta_alternada_iterativa_while([1, 2, 3, 4, 5]))  # 1 + 2 - 3 + 4 - 5 = -1

# Escribir una función recursiva de cola que tome un
# número entero positivo como entrada y devuelva la
# suma de sus dígitos. Por ejemplo, la suma de los
# dígitos de 123 sería 1 + 2 + 3 = 6.

def suma_digitos(n: int) -> int:
    def suma_digitos_interna(n: int, acumulador: int) -> int:
        if n == 0:
            return acumulador
        else:
            return suma_digitos_interna(n // 10, acumulador + n % 10)
    return suma_digitos_interna(n, 0)

print(suma_digitos(123))  # 1 + 2 + 3 = 6
print(suma_digitos(4567))  # 4 + 5 + 6 + 7 = 22 

# Implementar una versión iterativa
def suma_digitos_iterativa(n: int) -> int:
    acumulador = 0
    while n > 0:
        acumulador += n % 10
        n //= 10
    return acumulador   

print(suma_digitos_iterativa(123))  # 1 + 2 + 3 = 6
print(suma_digitos_iterativa(4567))  # 4 + 5 + 6 + 7 = 22

#Implementa una función que invierta una
#cadena utilizando recursión de cola

def invertir_cadena(cadena: str) -> str:
    def invertir_cadena_interna(cadena: str, acumulador: str) -> str:
        if not cadena:
            return acumulador   
        else:
            return invertir_cadena_interna(cadena[1:], cadena[0] + acumulador)
    return invertir_cadena_interna(cadena, '')  

print(invertir_cadena("Hola"))  # "aloH"
print(invertir_cadena("nohtyP"))  # "Python"
                
# Implementar una versión iterativa
def invertir_cadena_iterativa(cadena: str) -> str:
    acumulador = ''
    for char in cadena:
        acumulador = char + acumulador
    return acumulador

print(invertir_cadena_iterativa("Hola"))  # "aloH"  

#Implementar la recursión de cola de Fibonacci
def fibonacci_cola(n: int) -> int:
    def fibonacci_interna(n: int, a: int, b: int) -> int:
        if n == 0:
            return a
        else:
            return fibonacci_interna(n - 1, b, a + b)
    return fibonacci_interna(n, 0, 1)

print(fibonacci_cola(0))  #0
print(fibonacci_cola(3))  #2    

# calcular el producto de dos números enteros utilizando
# recursión de cola.
def producto(a: int, b: int) -> int:
    def producto_interno(a:int,b:int, acumulador:int) -> int:
        if b == 0:
            return acumulador
        else:
            return producto_interno(a, b - 1, acumulador + a)
    return producto_interno(a, b, 0)    

print(producto(3, 4))  # 12
print(producto(5, 6))  # 30

# Realizar una función recursiva de cola que calcule
# la diferencia alternada entre los elementos de una
# lista

def diferencia_alternada(lista: list[int]) -> int:
    if not lista:
        return 0
    elif len(lista) == 1:
        return lista[0]
    elif len(lista) == 2:
        return lista[0] - lista[1]
    else:
        acumulador = lista[0] - lista[1]
        signo = 1
        indice = 2
        while indice < len(lista):
            acumulador += signo * lista[indice]
            signo *= -1
            indice += 1
        return acumulador
print(diferencia_alternada([1, 2, 3, 4, 5]))  # 1 - 2 + 3 -4 +5  = 3    

# Calcular la potencia de dos números
# positivos utilizando recursión de cola
def potencia(a: int, b: int) -> int:
    def potencia_interna(a: int, b: int, acumulador: int) -> int:
        if b == 0:
            return acumulador
        else:
            return potencia_interna(a, b - 1, acumulador * a)
    return potencia_interna(a, b, 1)

print(potencia(2, 2))  # 4
print(potencia(3, 3))  # 27

# Implementa una función recursiva de cola
# para encontrar el máximo elemento en una
# lista de enteros
def max_elemento(lista: list[int]) -> int:
    def max_elemento_interno(lista: list[int], maximo: int) -> int:
        if not lista:
            return maximo
        else:
            if lista[0] > maximo:
                maximo = lista[0]
            return max_elemento_interno(lista[1:], maximo)  
    return max_elemento_interno(lista,0) 
print(max_elemento([441, 2, 33, 44, 5]))  

# Escribir una función recursiva de cola para calcular la
# suma de los elementos de una lista de enteros.

def suma_lista(lista: list[int]) -> int:
    def suma_lista_interna(lista: list[int], acumulador: int) -> int:
        if not lista:
            return acumulador
        else:
            return suma_lista_interna(lista[1:], acumulador + lista[0])
    return suma_lista_interna(lista, 0) 

print(suma_lista([1, 2, 3, 4, 5]))  # 15

# Definir la función esPalindromo, que dada una lista de
# enteros, retorne si es o no es palíndromo, utilizando
# recursividad explícita

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

# Definir la función recursiva cantidad, que dada
# una lista de enteros y un número n, retorne la
# cantidad de apariciones del número n en la lista dada.

def cantidad(lista: list[int], n: int) -> int:
    if not lista:
        return 0
    elif lista[0] == n:
        return 1 + cantidad(lista[1:], n)   
    else:
        return cantidad(lista[1:], n)   
    
print(cantidad([1, 2, 3, 2, 1], 2))  # 2
print(cantidad([1, 2, 3, 4, 5], 6))  # 0


