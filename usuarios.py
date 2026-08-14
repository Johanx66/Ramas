cuantos = int(input("Cuantos usuarios desea ingresar? "))
usuarios = []
for i in range(cuantos):
    nombre = input("Inserte nombre del usuario " + str(i+1) + ": ")
    usuarios.append(nombre) 