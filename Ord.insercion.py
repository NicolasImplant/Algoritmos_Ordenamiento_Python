# ordenamiento por insercion
import random as r

def ordenamiento_por_insercion(lista):
    
    for i in range(1, len(lista)):
        valor_actual = lista[i]

        while i>0 and lista[i-1] > valor_actual:
            lista[i] = lista[i-1]
            i-=1

        lista[i] = valor_actual
    
    return lista

if __name__ == "__main__":
    
    tamaño_de_lista = int(input("De que tamaño será la lista?  "))
    lista = [r.randint(0,100) for i in range(tamaño_de_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)