from typing import Generic, TypeVar, Optional, TypeAlias
from copy import copy

T = TypeVar('T')
ListaGenerica: TypeAlias = "Lista[T]"

class Nodo(Generic[T]):
    def __init__(self, dato: T, sig: Optional[ListaGenerica] = None):
        self.dato = dato
        if sig is None:
            self.sig= Lista()
        else:
            self.sig = sig

class Lista(Generic[T]):
    def __init__(self):
        self._head: Optional[Nodo[T]] = None

    def es_vacia(self) -> bool:
        return self._head is None

    def head(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.dato

    def copy(self) -> ListaGenerica:
        if self.es_vacia():
            return Lista()
        else:
            parcial = self._head.sig.copy()
            actual = Lista()
            actual._head = Nodo(copy(self._head.dato), parcial)
            return actual
        
    def tail(self) -> ListaGenerica:
        if self.es_vacia():
            raise IndexError('lista vacia')
        else:
            return self._head.sig.copy()

    def insertar(self, dato: T):
        actual = copy(self)
        self._head = Nodo(dato, actual)

    def eliminar(self, valor: T):
        def _eliminar_interna(actual: ListaGenerica, previo: ListaGenerica, valor: T):
            if not actual.es_vacia():
                if actual.head() == valor:
                    previo._head.sig = actual._head.sig
                else:
                    _eliminar_interna(actual._head.sig, actual, valor)

        if not self.es_vacia():
            if self.head() == valor:
                self._head = self._head.sig._head
            else:
                _eliminar_interna(self._head.sig, self, valor)

    def ultimo(self) -> T:
        if self.es_vacia():
            raise IndexError('lista vacia')
        if self._head.sig.es_vacia():
            return self._head.dato
        else:
            return self._head.sig.ultimo()

    def concat(self, ys: ListaGenerica) -> ListaGenerica:
        if self.es_vacia():
            return ys.copy()
        else:
            nueva_lista = self.copy()
            if nueva_lista._head.sig.es_vacia():
                nueva_lista._head.sig = ys.copy()
            else:
                nueva_lista._head.sig = nueva_lista._head.sig.concat(ys)
            return nueva_lista
       
    def join(self, separador: str = '') -> str:
        if self.es_vacia():
            return ''
        else:
            if self._head.sig.es_vacia():
                return str(self.head())
            else:
                return str(self.head()) + separador + self._head.sig.join(separador)
       
    def index(self, valor: T, indice_actual: int = 0) -> int:
        if self.es_vacia():
            raise ValueError(f'{valor} no encontrado en la lista')
        else:
            if self.head() == valor:
                return indice_actual
            else:
                return self._head.sig.index(valor, indice_actual + 1)
       
    def existe(self, valor: T) -> bool:
        if self.es_vacia():
            return False
        else:
            if self.head() == valor:
                return True
            else:
                return self._head.sig.existe(valor)

    def __repr__(self):
        if self.es_vacia():
            return '[]'
        else:
            if self._head.sig.es_vacia():
                return '[' + str(self.head()) + ']'
            else:
                return '[' + str(self.head()) + ', ' + self._head.sig.__repr__()[1:-1] + ']'
        
    def __eq__(self, otra: ListaGenerica) -> bool:
        if self.es_vacia() and otra.es_vacia():
            return True
        elif self.es_vacia() or otra.es_vacia():
            return False
        else:
            if self.head() != otra.head():
                return False
            else:
                return self._head.sig == otra._head.sig

    def __len__(self) -> int:
        if self.es_vacia():
            return 0
        else:
            return 1 + len(self._head.sig)
    def __getitem__(self, index: int) -> T:
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            return self.head()
        else:
            return self._head.sig[index-1]

    def __iter__(self):
        if not self.es_vacia():
            yield self.head()
            yield from self._head.sig    

if __name__ == '__main__':
    xs: Lista[int] = Lista()
    
    print(f'xs es vacia? {xs.es_vacia()}')	# True
    
    # Operaciones basicas
    xs.insertar(4)
    xs.insertar(10)
    xs.insertar(20)
    ys: Lista[int] = xs.tail()
    ys.insertar(9)
    ys.eliminar(10)
    ys.insertar(8)
    zs: Lista[int] = ys.copy()
    zs.eliminar(8)
    zs.eliminar(9)
    
    print(f'xs: {xs}')						# [20, 10, 4]
    print(f'ys: {ys}')						# [8, 9, 4]
    print(f'xs es vacia? {xs.es_vacia()}')	# False
    print(f'ultimo(xs): {xs.ultimo()}')		# 4
    print(f'len(xs): {len(ys)}')			# 3, ver __len__
    print(f'xs[1]: {xs[1]}')				# 10, ver __getitem__

    # Consumiendo como iterable
    for x in xs:
        print(x)	# 20 -> 10 -> 4

    # Otras operaciones
    print(f'xs.concat(ys): {xs.concat(ys)}')		# [20, 10, 4, 8, 9, 4]
    print(f'ys.join(" -> "): {ys.join(" -> ")}')	# 8 -> 9 -> 4
    print(f'xs.index(4): {xs.index(4)}')			# 2
    print(f'xs.existe(10): {xs.existe(10)}')        # True
    print(f'xs == zs? {xs == zs}')                  # False
    zs.insertar(10)
    zs.insertar(20)
    print(f'xs == zs? {xs == zs}')                  # True
    

    
