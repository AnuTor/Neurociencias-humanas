
from tkinter import *  ##  es una libreria que trabaja tambien con imagenes gif y png
#------->>

raiz= Tk()

raiz.title("SERIES DE TIEMPO")  # metodo para titulo de ventana raiz

#raiz.resizable(True,True)   # Dimensiones modificables de la ventana raiz "ancho-alto (true, false)"



######################################################################
######################################################################
##---------------------    INICIO BLOQUE N° 1   --------------------##



######  ---------      MARCO de Frame3 & Frama4     ----------  ######




miFrame3= Frame()
miFrame3.pack(side= "left", anchor= "n", fill="both", expand= "True")

miFrame4= Frame()
miFrame4.pack(side= "left", anchor= "n", fill="both", expand= "True")


##--VARIABLES GLOBALES DE FUNCIONES INTERNAS  AUN CUANDO SE LAS LLAME DESDE OTRO FRAME DEBE IR AFUERA
##------------------//
operacion="" # sintaxis de una variable globa pego la asignacion al simbolo del igual
resultado=0
##-----------------//

def mostrarFrame3():
    
    miFrame3.config(bg="green")
    miFrame3.config(width="300", height="300")
      #---------------------   Titulos -------------------------------///
    #  sintaxis   variableEntry= Label(contenedor, opciones)
    nombreLabel=Label(miFrame3, text="NOMBRE: ")
    nombreLabel.grid(row=0, column=0, sticky= "e", padx= 5, pady= 5)
    apellidoLabel=Label(miFrame3, text="APELLIDO: ")
    apellidoLabel.grid(row=1, column=0, sticky= "e", padx= 5, pady= 5)
    formacionLabel=Label(miFrame3, text="FORMACION: ")
    formacionLabel.grid(row=2, column=0, sticky= "e", padx= 5, pady= 5)
    passLabel=Label(miFrame3, text="PASSWORD: ")
    passLabel.grid(row=3, column=0, sticky= "e", padx= 5, pady= 5)
    ##-----------------------##------------------------------------------##
    miNombre=StringVar()
    miApellido=StringVar()
    #--------------------   Cuadros de Texto -------------------------///
    cuadro1Texto=Entry(miFrame3, textvariable= miNombre)
    cuadro1Texto.grid(row=0, column= 1,  padx= 5, pady= 5) 
    cuadro1Texto.config(fg= "green", justify= "center")
    cuadro2Texto=Entry(miFrame3, textvariable= miApellido)
    cuadro2Texto.grid(row=1, column= 1) # este metodo hace una grilla o tabla
    cuadro2Texto.config(fg= "blue", justify= "center")
    cuadro3Texto=Entry(miFrame3)
    cuadro3Texto.grid(row=2, column= 1) 
    cuadro4Texto=Entry(miFrame3)
    cuadro4Texto.grid(row=3, column= 1) 
    cuadro4Texto.config(show= "*",  fg= "blue")

    #--------------------   Ventana Comentarios  ---------------------///
    comentarioLabel=Label(miFrame3, text="Comentarios: ")
    comentarioLabel.grid(row=4, column=0, sticky= "e", padx= 5, pady= 5)
    textoComentario=Text(miFrame3, width= 22, height= 3)  ##  TENEMOS QUE DELIMITAR EL TAMAÑO LUEGO DEL FRAME
    textoComentario.grid(row=4, column= 1,  padx= 5, pady= 5) # este metodo hace un cuadro de comentarios
    scrollVert= Scrollbar(miFrame3, command= textoComentario.yview) # con esta instruccion construyo el scrollbar pero falta colocarlo
    scrollVert.grid(row= 4, column= 2, padx= 5, pady= 5, sticky= "snew") ##  con el parametro sticky lo hacemos de la misma altura que el Text
    textoComentario.config(fg= "blue", yscrollcommand = scrollVert.set)  ##  con el comando yscrollcommand = scrollVert.set  el posicionador del scrollbar me sigue en el Text

   #-------   Botones y Funcion de los Botones ---------------------///

   # BOTON 1
    def codigoBoton1():                            
        dato1= miNombre.get() 
        print("El nombre del Usuario es: ", dato1)
    botonGuardar= Button(miFrame3, text="GUARDAR", command= codigoBoton1)  
    botonGuardar.grid(row=5, column= 0, padx= 5, pady= 5)  

   # BOTON 2
    def codigoBoton2():                                    
        dato2= miApellido.set("DIAZ")
    botonEscribir= Button(miFrame3, text="ESCRIBIR", command= codigoBoton2)
    botonEscribir.grid(row=5, column= 1, padx= 5, pady= 5)  
   #botonEscribir.pack(side="left",  anchor="w" )

def cerrarFrame3():
    valor1= messagebox.askokcancel("Cerrar", "¿Deseas cerrar la Frame3?")
    if valor1== True:
       miFrame3.destroy()

#########################################################
#########################################################
       
def mostrarFrame4():
    miFrame4.config(bg="orange")
    miFrame4.config(width="200", height="340")

    ######################################################################
    ######################################################################
    ##---------------------    INICIO BLOQUE N° 4  --------------------##
    ######  -----------     MARCO de Frame4   ------------  #####



    ######################################################################
    ### //////////   INICION DEL DESARROLO DE LA FUNCIONALIDAD   /////####
    ######################################################################

    #  Objetivos:
    #           a)  Escribi numeros en pantalla
    #           b) Concatenar la escritura cuando corresponda
    #           c) Realizar las funciones de calculos de los botones operacionales
    def numeroPulsado(num):            ## num es el parametro que toma del boton pulsado       donde defini el parametro num?                
        global operacion
        
        if operacion != "":  # esto significa que el usuario ya pulso el boton suma  
           numeroPantalla.set(num)
           operacion=""         
        else:
           numeroPantalla.set(numeroPantalla.get() + num)

    # ### ---- funcion PULSAR BOTONES OPERACIONES EN TECLADO --> Objetivo: Retener dos o mas numeros y operar con ellos
    # sintaxis:

    ###     Funciones de Calculos

    ##======= Funcion SUMA ========##
    def suma(num): #le paso el parametro num que es el numero en pantalla que pretendo sumar
        global operacion
        global resultado
       
        resultado+= int(num)  # paso la variable numerica de un strings a un entero
        # la sintaxis anterior es como poner, resultado= resultado + int(num)
       
        operacion= "suma"
        numeroPantalla.set(resultado)
    ##=====Funcion  El RESULTADO =====##
       
    def el_resultado(): #le paso el parametro num que es el numero en pantalla que pretendo sumar       
        global resultado
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado=0
       
     ######################################################################
     ### //////////   FIN DEL DESARROLO DE LA FUNCIONALIDAD   //////////###
     ######################################################################

     ##############################################################################
     ###=======================   OBJETOS EN UNA INTERFAZ    ===================###
     ##############################################################################

     ##==================  Inicio Objeto PANTALLA  ==============================///
     ##############################################################################


    numeroPantalla= StringVar()
    pantalla=Entry(miFrame4, textvariable= numeroPantalla)
    pantalla.grid(row=0, column= 0, padx=10, pady= 10, columnspan=4, rowspan=1) # el argumento columnspan unifica columnas en una celda
    pantalla.config(background= "black", fg="white", justify="right", width="40")

      #############################################################################
      #==================== Fin Objeto Pantalla  ==============================///

      #==================== Inicio Objeto BOTONES =============================///
      #############################################################################

      #-------------fila 1---------------------------------------------

    boton7= Button(miFrame4, text="7", width= 7, background="yellow", fg= "blue",  command= lambda:numeroPulsado("7"))
    boton7.grid(row=1, column= 0, padx=5, pady= 5)
    boton8= Button(miFrame4, text="8", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("8"))
    boton8.grid(row=1, column= 1, padx=5, pady= 5)
    boton9= Button(miFrame4, text="9", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("9"))
    boton9.grid(row=1, column= 2, padx=5, pady= 5)
    botonMulti= Button(miFrame4, text="x", width= 7, background="yellow", fg= "blue")
    botonMulti.grid(row=1, column= 3, padx=5, pady= 5)

       #-------------fila 2---------------------------------------------
       
    boton4= Button(miFrame4, text="4", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("4"))
    boton4.grid(row=2, column= 0, padx=5, pady= 5)
    boton5= Button(miFrame4, text="5", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("5"))
    boton5.grid(row=2, column= 1, padx=5, pady= 5)
    boton6= Button(miFrame4, text="6", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("6"))
    boton6.grid(row=2, column= 2, padx=5, pady= 5)
    botonDiv= Button(miFrame4, text="/ ", width= 7, background="yellow", fg= "blue")
    botonDiv.grid(row=2, column= 3, padx=5, pady= 5)

      #-------------fila 3---------------------------------------------

    boton1= Button(miFrame4, text="1", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("1"))
    boton1.grid(row=3, column= 0, padx=5, pady= 5)
    boton2= Button(miFrame4, text="2", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("2"))
    boton2.grid(row=3, column= 1, padx=5, pady= 5)
    boton3= Button(miFrame4, text="3", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("3"))
    boton3.grid(row=3, column= 2, padx=5, pady= 5)
    botonMenos= Button(miFrame4, text="-", width= 7, background="yellow", fg= "blue")
    botonMenos.grid(row=3, column= 3, padx=5, pady= 5)

      #-------------fila 4---------------------------------------------
     
    botonIgual= Button(miFrame4, text=" = ", width= 7, background="yellow", fg= "blue", command= lambda:el_resultado())
    botonIgual.grid(row=4, column= 0, padx=5, pady= 5)
    boton0= Button(miFrame4, text="0", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado("0"))
    boton0.grid(row=4, column= 1, padx=5, pady= 5)
    botonComa= Button(miFrame4, text=" , ", width= 7, background="yellow", fg= "blue", command= lambda:numeroPulsado(","))
    botonComa.grid(row=4, column= 2, padx=5, pady= 5)
    botonMas= Button(miFrame4, text=" + ", width= 7, background="yellow", fg= "blue", command= lambda:suma(numeroPantalla.get()))
    botonMas.grid(row=4, column= 3, padx=5, pady= 5)

    #####################################################################
    #==================== Fin Objeto Boton============================///


    ##---------------------    FIN BLOQUE N° 4 -----------------------##
     ##---------------------    FIN Frame 4        -----------------------## 
    ######################################################################
    ######################################################################




    

def cerrarFrame4():
    valor1= messagebox.askokcancel("Cerrar", "¿Deseas cerrar la Frame4?")
    if valor1== True:
       miFrame4.destroy()
      
    
'''##  variables de funciones interactivas...(de botones)

#miNombre=StringVar()
#miApellido=StringVar()



######   -----------------------------------------------------  ######


#---------------------   Titulos -------------------------------///
#  sintaxis   variableEntry= Label(contenedor, opciones)


#nombreLabel=Label(miFrame3, text="NOMBRE: ")
#nombreLabel.grid(row=0, column=0, sticky= "e", padx= 5, pady= 5) # con el argumento sticky elijo hacia donde centrar el texto en puntos cardinales con el argumento  padx o pady, delimitamos la  distancia desde el widgets al borde del frame

apellidoLabel=Label(miFrame3, text="APELLIDO: ")
apellidoLabel.grid(row=1, column=0, sticky= "e", padx= 5, pady= 5)

formacionLabel=Label(miFrame3, text="FORMACION: ")
formacionLabel.grid(row=2, column=0, sticky= "e", padx= 5, pady= 5)

passLabel=Label(miFrame3, text="PASSWORD: ")
passLabel.grid(row=3, column=0, sticky= "e", padx= 5, pady= 5)



#--------------------   Cuadros de Texto -------------------------///


#cuadro1Texto=Entry(miFrame3, textvariable= miNombre) # con el argumento textvariable, yo le asigno el ingreso a un texto del Entry a la variable
#cuadro1Texto.grid(row=0, column= 1,  padx= 5, pady= 5) # este metodo hace una grilla o tabla # si yo delimito el pad en la primer fila y columna afecta a toda la grilla ;)
#cuadro1Texto.config(fg= "green", justify= "center")

cuadro2Texto=Entry(miFrame3, textvariable= miApellido)
cuadro2Texto.grid(row=1, column= 1) # este metodo hace una grilla o tabla
cuadro2Texto.config(fg= "blue", justify= "center")

cuadro3Texto=Entry(miFrame3)
cuadro3Texto.grid(row=2, column= 1) 

cuadro4Texto=Entry(miFrame3)
cuadro4Texto.grid(row=3, column= 1) 
cuadro4Texto.config(show= "*",  fg= "blue")



#--------------------   Ventana Comentarios  ---------------------///


comentarioLabel=Label(miFrame3, text="Comentarios: ")
comentarioLabel.grid(row=4, column=0, sticky= "e", padx= 5, pady= 5)
textoComentario=Text(miFrame3, width= 22, height= 3)  ##  TENEMOS QUE DELIMITAR EL TAMAÑO LUEGO DEL FRAME
textoComentario.grid(row=4, column= 1,  padx= 5, pady= 5) # este metodo hace un cuadro de comentarios
scrollVert= Scrollbar(miFrame3, command= textoComentario.yview) # con esta instruccion construyo el scrollbar pero falta colocarlo
scrollVert.grid(row= 4, column= 2, padx= 5, pady= 5, sticky= "snew") ##  con el parametro sticky lo hacemos de la misma altura que el Text
textoComentario.config(fg= "blue", yscrollcommand = scrollVert.set)  ##  con el comando yscrollcommand = scrollVert.set  el posicionador del scrollbar me sigue en el Text




#-------   Botones y Funcion de los Botones ---------------------///

# BOTON 1
def codigoBoton1():                                    # codigoBoton es la funcion que hace algo(script) al momento que se aprieta el boton, debe estar antes que el boton
       #miNombre.set("JUAN MANUEL")  # miNombre es una variable que yo tengo que definir que esta dentro de la funcion, que se llama al aprentar el boton
       dato1= miNombre.get() 
       print("El nombre del Usuario es: ", dato1)
botonGuardar= Button(miFrame3, text="GUARDAR", command= codigoBoton1)  ## para lograr que el boton ejecute una accion tengo que agregar el parametro command
botonGuardar.grid(row=5, column= 0, padx= 5, pady= 5) #botonGuardar.pack(side="left",  anchor="s" )


# BOTON 2
def codigoBoton2():                                    # codigoBoton es la funcion que hace algo(script) al momento que se aprieta el boton, debe estar antes que el boton
       dato2= miApellido.set("DIAZ")
botonEscribir= Button(miFrame3, text="ESCRIBIR", command= codigoBoton2)
botonEscribir.grid(row=5, column= 1)  
#botonEscribir.pack(side="left",  anchor="w" )


##---------------------    FIN BLOQUE N° 1   -----------------------##
######################################################################
######################################################################

raiz.mainloop()'''
