'''
Created on 21 oct. 2018

@author: marlorebazaloyola
'''

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
    anyOrAll() 
    '''
        CONTINUAR AQUI:
        https://www.hackerrank.com/challenges/ginorts/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
        
        DOCMENTACION PYTHON:
        https://docs.python.org/3/tutorial/controlflow.html?highlight=lambda#lambda-expressions
    '''