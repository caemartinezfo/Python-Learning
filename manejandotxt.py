#!/usr/bin/env python3
import os
from tkinter import filedialog
from tkinter import *

print("A continuacion presiona 'd' para ingresar el directorio de trabajo")
direct = input("Teclea: ")

if direct == "d":
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
else:
    print("Tecla incorrecta")

os.chdir(folder_selected) ## Establece directorio de trabajo

f = open("archivo.txt","r") ## Lee el archivo de usuarios txt
Usuarios = list(f)

for i in range(len(Usuarios)):
    Usuarios[i] = Usuarios[i].replace("\n","")

while True:
    print("___________________________________________________________")
    opcion = (input("Pulsa 1 si deseas agregar un nuevo usuario\nPulsa 2 si deseas eliminar un usuario\nPulsa 3 si deseas ver la lista de usuarios\nPulsa 4 si deseas terminar\nTeclea: "))
    print("___________________________________________________________")
    if opcion == "1":
        NewUser = input("Ingresa el nuevo usuario: ")
        Usuarios.append(NewUser)
        print("Usuario agregado con exito")
    elif opcion == "2":
        ConsUser = input("Ingresa el usuario que deseas eliminar: ")
        del Usuarios[Usuarios.index(ConsUser)]
        print("Usuario eliminado con exito")
    elif opcion == "3":
        for i in Usuarios:
            print(i)
    elif opcion == "4":
        miTexto = open("archivo.txt","w")
        for i in range(len(Usuarios)-1):
            miTexto.write(Usuarios[i]+"\n")
        miTexto.write(Usuarios[-1])
        miTexto.close()
        print("Gracias por usar este programa") 
        break
    else:
        print("Tecla incorrecta")

# Fin