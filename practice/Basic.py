'''
Created on 21 oct. 2018

@author: marlorebazaloyola
'''
from builtins import sorted
import string
import builtins

'''
    Sobre la condicional:
    "__name__" es un atributo especial de python que permite saber el espacio de nombres en el que
    se está ejecutando el modulo (archivo).
    Si el módulo python se ejecuta como programa principal (ya sea por línea de comandos, con 
    doble click, etc), el atributo "__name__" será igual a "__main__"; pero si lo usamos importándolo
    desde otro módulo, su valor será el nombre del módulo
    Fuente: https://es.stackoverflow.com/a/32185
'''
if __name__ == '__main__':

    print('Hello World!')
    
    def ifElse(number):
        if number % 2 != 0 or number in range(6,21):
            print('Weird')
        else:
            print('Not Weird')
    #ifElse(int(input()))
    
    def arithmeticOperators(n1, n2):
        print(n1 + n2)
        print(n1 - n2)
        print(n1 * n2)
    #arithmeticOperators(int(input()), int(input()))
    
    def division(n1, n2):
        print(int(n1 / n2))
        print(n1 / n2)
    #division(int(input()), int(input()))
    
    '''
        Sobre lista de comprensiones: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    '''
    def loop(number):
        ''' la sintaxis de comprensiones, indica que la expresión debe estar contenida dentro de corchetes '''
        [print(x**2) for x in range(number)]
    #loop(int(input()))
    
    '''
        Sobre nomenclatura de nombre de método: https://stackoverflow.com/a/8908798
    '''
    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False;
    #print(is_leap_year(int(input())));
    
    def printing(number):
        [print(x+1, end="") for x in range(0,number)]
    #printing(int(input()))
    
    def sort_athletes():
        ''' split(): Por defecto el parámetro "sep" (delimitador) es cualquier espacio en blanco '''
        nm = input().split()
        n = int(nm[0]) # número de elementos
        m = int(nm[1]) # número de atributos x elemento
        arr = []
        ''' 
            - se declara la variable "_" para indicar que no nos interesa esta variable por lo que no la usaremos
            FUENTE: https://stackoverflow.com/a/5893946
            - rstrip(): remueve los espacios en blanco al final de la cadena "r" de right
            - map(int, lista): convertirá cada elemento ingresado a entero
            Sobre map: https://docs.python.org/3/library/functions.html#map
            - lis(...): casteamos al tipo list los elementos convertidos
            - arr.append(...): agregamos la lista (fila de atributos x elemento) al a arreglo 
        '''
        for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))
        k = int(input()) # indice del atributo por el cual se ordenará el arreglo
        '''
            - lambda permite definir una función "mínima"
            - en este caso al parámetro "key" le enviamos una función lambda, que recibe un elemento de "arr"
            y devuelve un valor (el sub-elemento en el indice "k") que creo se usará internamente en la comparación
            al momento de ordenar la lsta
            sobre lambda: https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions
        '''
        arr.sort(key=lambda e: e[k])
        ''' 
            - la cadena sobre la que se aplica el join (en este caso el espacio en blanco) será insertada
            entre los elementos de la lista enviada como parámetro
            - hacemos uso de "map()" nuevamente para convertir los elementos de cada sub-ista a tipo string
        '''
        [print(' '.join(map(str, e))) for e in arr]
    #sort_athletes()
    
    def anyOrAll():
        _ = int(input())
        arr = list(map(int, input().split()))
        '''
            Obtención de una rebanada
            cadena[inicio:fin:paso]: 
            - el valores x defecto = cadena[0: len(cadena): 1]
            Esto quiere decir que va de inicio a fin de la cadena sumando el paso
            cadena[0: len(cadena): -1]: Al ser el paso negativo comienza desde el final
        '''
        print(all(e > 0 for e in arr) and any(str(e) == str(e)[::-1] for e in arr))
    #anyOrAll() 
    
    def ginortS():
        '''
            En este problema se debe ordenar la cadena ingresada de la siguiente forma: minusculas, mayusculas, impares y pares
        '''
        value = input()
        '''
            En python los valores booleanos: False y True pueden ser tratados como enteros 0 y 1 respectivamente.
            Aqui una discusion si debe ser evitado o no: https://stackoverflow.com/a/3175293
        '''
        '''
            Solucion mía:
            1. primero ordeno x defecto para poder tener las letras y números ordenados de menor a mayor
            2. vuelvo a ordenar haciendo uso de la funcion "key" si es mayuscula devolverá "1", si es un numero impar devolverá 2
            y si es un número par devolverá 3
            3. al momento de imprimir hacemos uso de "*", esto permite enviar la lista desempaquetada al método "print()", como
            si se estuviera enviando print(valor1, valor2...). 
            Finalmente hacemos uso del parámetro "sep" para indicar que no haya espacio entre las separaciones de los valores 
            al momento de imprimirlos
        '''
        print(*(sorted(sorted(value), key=lambda v: v.isupper() + (v.isnumeric() and (3 if int(v) % 2 == 0 else 2) ))), sep='')
        '''
            Soluciones interesantes (no son mias):
        '''
        ''' 1. La misma lógica que el punto 2, pero haciendo uso de operador ">>". leer: https://wiki.python.org/moin/BitwiseOperators '''
        print(*sorted(value, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')
        
        ''' 2. Esta solución devuelve una tupla compuesta x 3 valores:
        - primer elemento: -1 si es minuscula, 0 si es mayuscula ó 1 si es un número 
        - segundo elemento: 0 si no es par, 1 si es par
        - tercer elemento: el caracter en cuestion
        De esta forma el sorted se aplicará sobre tuplas. Esto es posible en python.
        '''
        print(*sorted(value, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
        ''' Ejemplo de ordenado de lista de listas'''
        print(sorted([[1, 1, '2'], [-1, 0, 'b'], [-1, 0, 'a'], [0, 0, 'Z']]))
        
        ''' 3. No hay mucha explicación que hacer para esta solución...'''
        order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
        ''' la función index() sobre un string, recibe une subcadena y retorna el menor indice de donde la encontró '''
        print(*sorted(value, key=order.index), sep='')
        
        ''' 4. Pendiente de revisar '''
        print(*sorted(value, key=(string.ascii_letters + '1357902468').index), sep='')
        
        
        print(builtins.__file__)
    #ginortS()
    '''
        CONTINUAR AQUI:
        https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?h_r=next-challenge&h_v=zen
        
        DOCMENTACION PYTHON:
        https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions
    '''