import time
from tkinter import *
from PIL import Image
from PIL import ImageTk
import speech_recognition as sr
import pyttsx3
import sys

        
tamanho=0
#definicion del tablero
tablero = []
M=0
N=0
#posicion del jugador
xjugador=0
yjugador=0
y=0  
#lista donde se encuentran los obstaculos
listaObstaculos =[[1,1],[3,1],[2,2],[4,2],[4,4]]
listaRuta =[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]

#Origen de Luna
origen=[[0,0]]
#Destino de Luna
destino=[[6,5]]

#############################################################################
##David Gonzalez
def escuchar():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("_________________________Escuchando...")
        audio=r.listen(source)
    try:
        ##print("Tu dijiste:"+r.recognize_google(audio, language = "es-ES"))
        print("_________________________Procesando...")
        temp=r.recognize_google(audio, language = "es-ES")
        print("_________________________Termino de escuchar")
        return temp
    except Exception:
        return ("Algo anda mal")

################################################################################
#David Gonzalez
def ejecutar():
    bandera = True
    while(True):
        escu = escuchar()#.lower()
        ##escu=escu.lower()
        print("_______________TEST:"+escu)
        if (escu.lower() == "luna"):
                ##Responde con un msj
                if(bandera):
                    hablar('Hola mi nombre es luna, es un gusto siempre servirle, en que le puedo ayudar hoy?')
                    bandera = False
                else:
                    hablar('Que desea realizar?')
                ##Escucha
                escu = escuchar()#.lower()
                escu=escu.lower()
                print("Se ha escuchado ==> "+escu)
                    
                ##Ejecuta comando que escucho
                if(comandos(escu)):
                    ##Responde con un msj despues de ejecutar comando
                    hablar('Su peticion fue realizada')
                else:
                    hablar('No se ha reconocido lo solicitado')
        else:
            print(escu+": esto es un error!")
################################################################################
#David Gonzalez
def hablar(hablada):
    engine = pyttsx3.init()
    engine.say(hablada)
    engine.runAndWait()
            
def crearCuadricula():
    hablar("Digite el valor de M")
    escuM = escuchar()
    ###############
    hablar("Digite el valor de N")
    escuN = escuchar()
    ###############
    hablar("Digite el valor de A")
    escuA = escuchar()
    ###############
    hablar("El valor de M es:"+escuM+",el valor de N es:"+escuN+"y el valor de A es:"+escuA)
    ###############
    hablar("¿Los valores son correctos? Responda con si, si los valores son correctos.")
    escuSi = escuchar()
    print("#################Test: "+ escuSi)
    if(escuSi.lower()=="sí"):
        print("Se creo cuadricula: "+str(int(escuM)+int(escuN)+int(escuA)))
        creaCanvas(int(escuA), int(escuM), int(escuN))
    else:
        hablar("Repita los valores por favor")
        crearCuadricula() 
    return True

################################################################################
#David Gonzalez
def mostrarRuta():
    ##creaRuta()
    return True

def cambiarInicio():
    ##Recordar validar el tamaño de la matriz para que no se salga del rango posible y muestre error
    hablar("Digite el valor de la fila")
    escuF = escuchar()
    ###############
    hablar("Digite el valor de la columna")
    escuC = escuchar()
    ###############
    hablar("El valor de la fila es:"+escuF+" y el valor de la columna es:"+escuC)
    ###############
    hablar("¿Los valores son correctos? Responda con si, si los valores son correctos.")
    escuSi = escuchar()
    print("#################Test: "+ escuSi)
    if(escuSi.lower()=="sí"):
        print("Se cambio el inicio: "+str(int(escuF)+int(escuC)))
        ##cambia los valores de inicio y vuelve a imprimir 
##        global origen
##        origen=[escuF,escuC]
##        creaTablero1()
##        
    else:
        hablar("Repita los valores por favor")
        cambiarInicio()
    return True

##################################################################################
#David Gonzalez
def cambiarFinal():
    hablar("Digite el valor de la fila")
    escuF = escuchar()
    ###############
    hablar("Digite el valor de la columna")
    escuC = escuchar()
    ###############
    hablar("El valor de la fila es:"+escuF+" y el valor de la columna es:"+escuC)
    ###############
    hablar("¿Los valores son correctos? Responda con si, si los valores son correctos.")
    escuSi = escuchar()
    print("#################Test: "+ escuSi)
    if(escuSi.lower()=="sí"):
        print("Se cambio el inicio: "+str(int(escuF)+int(escuC)))
         ##cambia los valores de destino y vuelve a imprimir 
##        global destino
##        destino=[escuF,escuC]
##        creaTablero1()
    else:
        hablar("Repita los valores por favor")
        cambiarFinal()
    return True

def limpiar():
    ##Limpia la ruta
    #limpiaRuta()
    #creaTablero1()
    return True

def ayuda():
    ##hablar("Debe hablar claro y cerca del microfono al momento de dar las indicaciones, esto hara que el sistema trabaje mejor")
    hablar("Diga la palabra A si quiere informacion para crear cuadricula, la palabra B si quiere informacion para mostrar ruta, la palabra C si quiere informacion para cambiar inicio, la palabra D si quiere informacion para cambiar final o la palabra e para un consejo adicional")
    escuA = escuchar()
    if(escuA.lower()=="a"):
        hablar("Se le pediran las medidas M, N y A, debe decirlas de forma clara y luego se le preguntara si son correctas, debe indicar si lo son o desea volver a repetirlas, luego de eso se ejecutara el comando")
    elif(escuA.lower()=="b"):
        hablar("Despues de decir el comando mostrar ruta, se ejecutara automaticamente")
    elif(escuA.lower()=="c"):
        hablar("Se le pedira el numero de fila y seguidamente el numero de columnas, se pedira que confirma si los valores son correctos y si confirma que si se ejecutara el comando")
    elif(escuA.lower()=="d"):
        hablar("Se le pedira el numero de fila y seguidamente el numero de columnas, se pedira que confirma si los valores son correctos y si confirma que si se ejecutara el comando")
    elif(escuA.lower()=="e"):
        hablar("Hablar de forma clara, cerca del microfono y con poco ruido ambiente ayudara a la comprension de los comandos para su ejecucion")
    else:
        hablar("La opcion no ha sido encontrada, le repetimos las opciones.")
        
    return True
def salir():
    hablar("Siempre es un placer ayudarle")
    sys.exit()

def comandos(argument):
    switcher = {
        "crear cuadrícula": crearCuadricula,
        "mostrar ruta": mostrarRuta,
        "cambiar inicio": cambiarInicio,
        "cambiar final": cambiarFinal,
        "limpiar": limpiar,
        "ayuda": ayuda,
        "salir": salir
    }
    # Obtener la función del diccionario del switch
    func = switcher.get(argument, lambda: False)
    # Ejecuta la funcion
    return func()


##################################################################################
#Maria Jose
#crear tablero
def creaTablero(A,M,N):   
    
    x=90
   
    global tamanho,y
    y=0
    tamanho=A
    global tablero

    
    #rellena la matriz con ceros
    for r in range(M):
        r=[0]*N
        tablero.append(r)

    #coloca a Sara en la matriz
    tablero[origen[0][0]][origen[0][1]]=3

    #coloca a la salida en la matriz
    tablero[destino[0][0]][destino[0][1]]=6
    
    #Coloca obstaculos en la matriz
    creaRutaMatriz()
    creaObstaculosMatriz()
    #Coloca las imagenes de las paredes, los obstaculos y Sara
    for i in range(len(tablero)):
        y=y+A
        x=90
        j=0
        for j in range(len(tablero[0])):
            if(tablero[i][j]==2):
                canvas.create_image(x,y,image=photo1)#coloca obstaculo
            elif(tablero[i][j]==3):
                canvas.create_image(x,y,image=photo3)#coloca a Luna
            elif(tablero[i][j]==6):
                canvas.create_image(x,y,image=photo4)#coloca a Luna
            else:
                canvas.create_image(x,y,image=photo2)#coloca piso
            x = x+A

#crear tablero despues de limpiar ruta
def creaTablero1():   
    
    x=90
    y=0
    global tamanho
    global tablero

    #coloca a Sara en la matriz
    tablero[origen[0][0]][origen[0][1]]=3

    #coloca a la salida en la matriz
    tablero[destino[0][0]][destino[0][1]]=6
    
    #Coloca las imagenes de las paredes, los obstaculos y Sara
    for i in range(len(tablero)):
        y=y+tamanho
        x=90
        j=0
        for j in range(len(tablero[0])):
            if(tablero[i][j]==2):
                canvas.create_image(x,y,image=photo1)#coloca obstaculo
            elif(tablero[i][j]==3):
                canvas.create_image(x,y,image=photo3)#coloca a Luna
            elif(tablero[i][j]==6):
                canvas.create_image(x,y,image=photo4)#coloca a Luna
            else:
                canvas.create_image(x,y,image=photo2)#coloca piso
            x = x+tamanho

#muestra la ruta
def creaRuta():
    x=90
   
    global tamanho
    global tablero

    y=0 
    creaRutaMatriz()
    #Coloca las imagenes de las paredes, los obstaculos y Sara
    for i in range(len(tablero)):
        y=y+tamanho
        x=90
        j=0
        for j in range(len(tablero[0])):
            if(tablero[i][j]==2):
                canvas.create_image(x,y,image=photo1)#coloca obstaculo
            elif(tablero[i][j]==3):
                canvas.create_image(x,y,image=photo3)#coloca a Luna
            elif(tablero[i][j]==5):
                canvas.create_image(x,y,image=photo4)#coloca ruta
            else:
                canvas.create_image(x,y,image=photo2)#coloca piso
            x = x+tamanho
            
##Limpia el camino de la ruta
def limpiaRuta(): 
    for iiii in range(len(tablero)):
        for jjjj in range(len(tablero[0])-1):
            if(tablero[iiii][jjjj]==5):
                tablero[iiii][jjjj]=0

##Crea ruta
def creaRutaMatriz():
    for iii in range(len(listaRuta)):
        for jjj in range(len(listaRuta[0])-1):
            tablero[listaRuta[iii][jjj]][listaRuta[iii][jjj-1]]=5

##Crea obstaculos
def creaObstaculosMatriz():
    #Coloca obstaculos en la matriz
    for ii in range(len(listaObstaculos)):
        for jj in range(len(listaObstaculos[0])-1):
            tablero[listaObstaculos[ii][jj]][listaObstaculos[ii][jj+1]]=2


      
def creaCanvas(A,M,N):
    ##creacion del canvas
    tk= Tk()


    ##Creacion de los scrollbars
    xscrollbar = Scrollbar(tk, orient=HORIZONTAL)
    yscrollbar = Scrollbar(tk, orient=VERTICAL)
    yscrollbar.pack(side = RIGHT, fill= Y)
    xscrollbar.pack(side = BOTTOM, fill= X)

    global canvas
    canvas = Canvas(tk,width=500, height=500, xscrollcommand = xscrollbar.set, yscrollcommand = yscrollbar.set, scrollregion= (0, 0, 5000, 5000))
    xscrollbar.config(command=canvas.xview)
    yscrollbar.config(command=canvas.yview)

    #Imagenes
    global photo1,photo2,photo3,photo4
    image1 = Image.open('pasto.jpeg')
    image1 = image1.resize((A,A), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open('piso.jpeg')
    image2 = image2.resize((A,A), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open('Sara.jpeg')
    image3 = image3.resize((A,A), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)

    image4 = Image.open('pared.jpeg')
    image4 = image4.resize((A,A), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)

    creaTablero(A,M,N)

    canvas.pack()


         
