#Problema del elemento comun


l1 = list (input ("Ingrese una lista"))
l2 = list (input("Ingrese otra lista"))
i = min (len(l1),len(l2))
j = 0
while(j < i):
	if (l1[j] ==l2[j]):
		print("las listas tienen en comun el elemento: ", l1[j])
        else:
		if (j == i-1 & l1[j] != l2[j]):
			print("las listas no tienen en comun ningun elemento: ")
	j=j+1
