""""""""""
lista = [50, "mensaje" , 3.1415 , {1,2,3}]
print(lista [2])
"""""""""
lista= [1,5,15,25,100,500]
print("iniciar; " ,lista ) 

#Append()= agregar dato al final de la lista 
lista.append (250)
print("append: ", lista )

#extend([])=toma una segunda lista y agrega sus....
lista2=[75 , 125]
lista.extend (lista2)
print ("extend:" , lista)

#insert(posicicon-valor) agregar datos en la posicion 
lista.insert(2,400)
print("insert:", lista)

#remover(valor)=busca y determina el valor entregado, aparte lo elimina de la lista 
lista.remove(400)
print("remover:", lista )

#pop()= Elimina el ultimo registro
#pop(posicion)=elimina la posicion entregada

lista.pop()
print("pop:", lista)

lista.pop(2)
print("pop(2):", lista )

#reverse= invierte el orden de la lista
lista.reverse()
print("reverse", lista )

#sort= ordenar de menor a mayor
lista.sort()
print("sort:", lista )

#sort(reverse=true)=ordena los datos de mayor a menor
lista.sort(reverse=True)
print("sort(r):", lista)

#