print ("Ingrese 2 para calcular el maximo dentre 2 numeros")
print ("Ingrese 3 para calcular el maximo dentre 3 numeros")
print ("Ingrese 4 para calcular el largo de una lista")
print ("Ingrese 5 para Determinar si un caracter ingresado es vocal o consonante")
print ("Ingrese 6 para Realizar la suma de los elementos de una lista")
print ("Ingrese 7 para Realizar la multiplicacion de los elementos de una lista")

opcion = input()

if opcion == 2: 
	print ("Ingrese dos numeros")
        n1= int (input())
        n2= int (input())
	if (n1 > n2):
		print ("El mayor es: ", n1)
	else:
		print ("El mayor es: ", n2)
	
if opcion == 3:
	print ("Ingrese 3 numeros")
	n1= int (input())
        n2= int (input())
	n3= int (input())
	if (n1 > n2) & (n1>n3):
		print ("El mayor es: ", n1)
	if (n2 > n1) & (n2>n3):
		print ("El mayor es: ", n2)
	if (n3 > n1) & (n3>n2):
		print ("El mayor es: ", n3)

if opcion == 4:
	lista=[]
	largo=0
	print ("Ingrese un elemento de la lista o False para termimar de agregar")
	i= bool (input ())
	while (i):
		print ("Ingrese un elemento de la lista")
		elemento= input()
		lista.append(elemento)
		print ("Ingrese True para ingresar un elemento de la lista o False para termimar de agregar")
		i= bool (input ())
		largo= largo + 1
	print ("El largo de la lista es: ", largo)
	
	
if opcion == 5:
	c =  str (input ("Ingrese un caracter"))
	if c=="a" or c=="e" or c=="i" or c=="o"or c=="u" or c=="A"or c=="E"or c=="I"or c=="O"or c=="U":
		print ("La letra ingresada es vocal")
	else:
		print ("La letra ingresada es consonante")


if opcion == 6:
	L1 = list (input ("Ingrese una lista"))
	i = len(L1)
	j = 0 
	suma = 0
	while (j < i):
		suma = suma + L1[j]
		j=j+1
	print ("la suma es: ", suma)

if opcion == 7:
	L1 = list (input ("Ingrese una lista"))
	i = len(L1)
	j = 0 
	multiplicacion= 1
	while (j < i):
		multiplicacion = multiplicacion*L1[j]
		j=j+1
	print ("la suma es: ", multiplicacion)
		
		


	
		
