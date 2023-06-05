import numpy as np

lista =[1,2,3,4,5]
arreglo =np.array (lista)
print(arreglo)

#indicar canta dimensiones posee el arreglo
print(F"el arreglo es de {arreglo.ndim}dimesion")

#len=indicar el largo del arreglo
print(f"arreglo de largo{len(arreglo)}")

#slice
#start:stop:step=inidicador cuanto quiere mostrar del arreglo
#Star:: = Indica desde donde vamos a consultar
#stop: = indica hasta donde vamos a consultar
#::Step = indica dse cuanto en cuanto vamos a consultar
print(arreglo[::2])

#rellenar arreglo

lista2 =[i for i in range(1,11)]
arreglo2= np.array(lista2)

#arange(start:stop:step)=rellenar el arreglo con valores segun lo indicado
arreglo3 = np.arange(1,11)
print(arreglo3)

#operaciones
#suma
arreglo3 += 5
print(arreglo3)

#multiplicar
arreglo3*=10
print(arreglo3)

#comparaciones o operadores relacionales
print(arreglo3>arreglo2)
