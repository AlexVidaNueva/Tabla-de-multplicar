num = int(input("Número a multiplicar: "))
 
rango = range(11)
for element in rango:
	result = num * element
	print (num, '*',	element, "=", result)