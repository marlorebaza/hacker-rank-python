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
        ''' la sintaxis indica que la expresión debe estar contenida dentro de corchetes '''
        [print(x**2) for x in range(number)]
    #loop(int(input()))
    
    '''
        CONTINUAR AQUI:
        https://www.hackerrank.com/challenges/write-a-function/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
        
        DOCMENTACION PYTHON
    '''