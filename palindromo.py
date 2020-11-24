#Problema de la palabra palindromo


N = input ("ingrese una palabra")

palabra = list(N)

i=0
k=int (len(palabra)/2)
j=len(palabra)
l=0

while(i<k):
	if (palabra[i]==palabra[j-1-i]):
		l=l+1
	i=i+1
if (l == k):
	print ("la palabra es palindromo")
		
else:
	print ("la palabra no es palindromo")




