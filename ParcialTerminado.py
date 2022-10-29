from operator import index
from pickle import FALSE, TRUE
from re import A, I
from tkinter import N


cancionero = [["CRAZY","LOCOPLAYA","♪♫Yo sé que el antídoto es veneno♪♫"],["Three Little Birds","Bob Marley","♪♫Don't worry about a thing♪♫"],["Lucy In The Sky With Diamonds","The Beatles","♪♫Lucy in the Sky with Diamonds♪♫"],["Perdida en el fuego","Los Espiritus","♪♫No te dimos más lugar♪♫"],["La sin razon","La Vela Puerca","♪♫Detrás de su corazón, queda un poquito de miel♪♫"]]

def listarCanciones():
    for i in cancionero:
        print("\nid:", cancionero.index(i)+1,"\nNombre:  ", i[0],"\nArtista: ",i[1], "\nLetra:   ", i[2])

def addCancion():
    nombre = str(input("ingrese nombre de la cancion: "))
    artista = str(input("ingrese el artista: "))
    letra = str(input("ingrese la letra: "))
    cancion = [nombre,artista,letra]
    cancionero.append(cancion)
    print(listarCanciones())

def buscarCancion():
    nombre = str (input("Que cancion desea buscar?: "))
    encontro = 0
    for i in cancionero:
        if i[0].lower().find(nombre.lower()) != -1: 
            encontro =+ 1
            print("\nNombre:  ", i[0],"\nArtista: ",i[1], "\nLetra:   ", i[2],"\n")               
    if encontro == 0:
        print("No se encontro nada.")

def modCancion():
    print(listarCanciones())       
    palabra = str(input("\nQue cancion desea modificar?\n"))
    for i in cancionero:
        if palabra.lower() in i[0].lower():
            choose=int(input("Que desea modificar?"+"\nOpciones"+"\n1 - Nombre"+"\n2 - Artista"+"\n3 - Letra\n"))
            if choose == 1:
                editarNombre = input("ingrese nuevo nombre del tema:")
                i[0] = editarNombre
                listarCanciones()
            elif choose == 2:
                editarArtista = input("Ingrese nuevo nombre del artista:")
                i[1] = editarArtista
                listarCanciones()
            elif choose == 3:
                editarLetra = input("Ingrese nueva letra del tema:")
                i[2] = editarLetra
                listarCanciones()    
            else:
                print("Cancion no encontrada")
                modCancion()
            return
    print("Cancion no encontrada") 

while TRUE:
    print("\n***MENU PRINCIPAL***"+"\n1 - Mostrar lista de canciones"+"\n2 - Agregar nueva cancion"+"\n3 - Buscar cancion"+"\n4 - Modificar cancion"+"\n5 - Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        listarCanciones()
    elif opcion == 2:
        addCancion()
    elif opcion == 3:
        buscarCancion()
    elif opcion == 4:
        modCancion()
    elif opcion == 5:
        print("fin del programa")
        break

