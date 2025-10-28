from funciones import *


bool = True


nombre = input("Introduce tu nombre: ")



selecciona = str(input("Selecciona una opcion " \
"para tu nombre: capitalize, lower, upper: "))

if selecciona == 'capitalize':
    print(cap(nombre))

elif selecciona == 'lower':
    print(low(nombre))

elif selecciona == 'upper':
    print(up(nombre))