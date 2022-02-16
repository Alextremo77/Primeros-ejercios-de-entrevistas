# Ejercicios de entrevistas de YOUTUBE
# Ejercicio 1 
# crea un programa que le pida al usuario que ingrese su nombre y su edad
# imprima un mensaje dirigido a ellos que les diga el año en el que cumpliran 100 años
nombre = input('Por favor ingrese su nombre: ')
edad = input('Por favor ingrese su edad: ')
# el usuario ingresa nombre y edad
try:
    # se calculan cuantos años le faltan para cumplir 100
    resto = 100 - int(edad)
    fecha = 2021 + resto  # se calcula  el año en el que los cumplira
    print(nombre, ' usted cumplira 100 años en el año: ', fecha)  # se imprime en pantalla
except:
    print('Por favor ingrese una edad valida o revise el codigo')
    
# 2 Ejercicio entrevista
# define una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos
def function_max(n1: int, n2: int):
    """funcion_max es funcion que recibe dos numeros como argumentos y devuelve el mayor

    Args:
        n1 (int): primer numero
        n2 (int): segundo numero 

    Returns:
        int = el valor mayor
    """
    try:
        if n1 > n2:
            return print('El numero mayor es: ', n1)
        elif n1 < n2:
            return print('El numero mayor es: ', n2)
        elif n1 == n2:
            return print('ALERTA: Los numeros no pueden ser iguales')
    except:
        print('ALERTA: Algo salio mal...')
        
# Ejercicio 3:
# crea una función llamada calculo_salario que reciba dos parámetros (horas y tarifa)
# para un programa del cálculo del salario, para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
# Introduzca las Horas: 45
# Introduzca la Tarifa por hora: 10
#Salario: 475.0
def calculo_salario(horas: float, tarifa: int):
    """calculo_salario es una funcion que recibe como parametros las horas trabajadas y tarifa de pago para calcular el salario de un trabajador

    Args:
        horas (float): horas trabajadas
        tarifa (int): valor de hora trabajada

    Return:
        float = monto del salario del trabajador
    """
    horas_extras = horas - 40
    valor_horas_extras = tarifa*1.5
    salario_x_horas_extras = horas_extras*valor_horas_extras
    salario_x_horas = 40*tarifa
    salario = salario_x_horas + salario_x_horas_extras
    return print('El monto del salario es: ', salario)
    
# ejercicio 4:
# escribe un programa que imprima los enteros desde 1 hasta el numero especifico 15
# para multiplos de 3 imprima "fizz" y para los multiplos de 5 imprima "buzz"
# para multiplo de ambos que imprima "fizzbuzz"

n = 1
while n < 16:
    """programa que imprime los enteros desde el 1 hasta el 15
       para los multiplos de 3 que imprima "fizz"
       para los multiplos de 5 que imprima "buzz"
       y para los multiplos de 3 y de 5 imprima "fizzbuzz"
    """
    if (n % 3 == 0) and (n % 5 == 0):
        print('fizzBuzz')
    elif (n % 3 == 0):
        print('fizz')
    elif (n % 5 == 0):
        print('buzz')
    else:
        print(n)
    n = n + 1
    
# ejercicio 5: definir una funcion max_de_tres, que tome tres numeros como argumentos y
# devuelva el mayor de ellos

def max_de_tres(n1: int, n2: int, n3: int):
    """ max_de_tres es una funcion que recibe tres numeros 
        como argumentos e indica el mayor de los tres

        Args:
        n1: primer numero
        n2: segundo numero
        n3: tercer numero

        Return:
        int: el mayor numero
    """
    if (n1 != n2) and (n2 != n3) and (n1 != n3):
        if (n1 > n2):
            if (n1 > n3):
                return print('El numero mayor es: ', n1)
            else:
                return print('El numero mayor es: ', n3)
        else:
            if (n2 > n3):
                return print('El numero mayor es: ', n2)
            else:
                return print('El numero mayor es: ', n3)
    else:
        return print('ALERTA: Disculpe los numeros no pueden repetirse')
        
# ejercicio 6: escribir una funcion que tome un caracter y devuelva true si es una vocal, de lo
# contrario devuelve false
def es_vocal(simb):
    """es_vocal verifica si un caracter es una vocal

    Args:
        simb (str): es un caracter cualquiera simbolo, numero o letra

    Returns:
        booleano: true or false
    """
    if (simb == 'a') or (simb == 'e') or (simb == 'i') or (simb == 'o') or (simb == 'u'):
        return print('true')
    else:
        return print('false')
# ejercicio 7 Escribe un programa que lea repetidamente números hasta
# que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números. Si el usuario introduce cualquier otra cosa que no sea un
# número, detecta su fallo usando try y except, muestra un mensaje de
# error y pasa al número siguiente.
total = 0
cantidad = 0
while True:
    """es un programa que lee repetidamente numeros hasta que el usuario ingresa 'fin'
    y una vez que el ingrese 'fin' muestra en pantalla el total, la cantidad de numeros y 
    la media. si el usuario introduce cualquier otra cosa que no sea un numero detecta su fallo usando try y except muestra un mensaje de error y pasa al siguiente
    """
    valor = input('>>Ingrese un número: ')
    if (valor == 'fin'):
        print('El total es: ', total)
        print('La cantidad de números es: ', cantidad)
        print('La media de los números es: ', media)
        break
    else:
        try:
            num = int(valor)
            total = total + num
            cantidad = cantidad + 1
            media = total/cantidad
        except:
            print('MENSAJE: ERROR INGRESE UN NÚMERO EN DÍGITOS')
            continue

# ejercicio 8: escribir una funcion sum() y funcion mult() que sumen y multiplique respectivamente todos los numeros de una lista

def suma(lista: list):
    """suma es una funcion que recibe una lista de numeros como argumento y devuelve la suma de todos los numeros 

    Args:
        lista (list): lista de numeros a sumar

    Returns:
        int: la suma de los numeros
    """
    # voy a recorrer la lista y sumar los terminos de la misma
    suma = 0
    for num in lista:
        suma = suma + num
    return print('La suma de los números de la lista es: ', suma)
    
def multiplica(lista: list):
    """multiplica es una funcion que recibe como parametro una lista y devuelve la multiplicacion de los numeros de la misma

    Args:
        lista (list): lista de numeros

    Returns:
        int: valor del resultado de la multiplicacion
    """
  # voy a recorrer la lista mientras realizo la multiplicacion de los valores de la misma
    mult = 1
    for num in lista:
        mult = mult*num
    return print('La multiplicacion de los números de la lista es: ', mult)



