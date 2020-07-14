##########################
##  DESARROLLAR INTERFAZ GRAFICA EN PYTHON
#### 3 COMPONENTES PRINCIPALLES    Raiz(tk)  -  Frame  -   Widgets


#########################################################################
##########################################################################
##########################################################################


####------------------  IMPORTACION DE MODULOS RELEVANTES  ---------------####
####------------------  Version v3 Alejo ---> Juan     Lista!!     ---------------####

from tkinter import *  ##  es una libreria que trabaja tambien con imagenes gif y png
#------->>
from tkinter import messagebox
from tkinter import filedialog
# ------>>
from calculos import operacion 
from frame import *

##----------------DEFINICION DE FUNCIONES PARA BOTONES----------------##

# BOTON 1
def codigoBoton1():                                    # codigoBoton es la funcion que hace algo(script) al momento que se aprieta el boton, debe estar antes que el boton
       #miNombre.set("JUAN MANUEL")  # miNombre es una variable que yo tengo que definir que esta dentro de la funcion, que se llama al aprentar el boton
       dato1= miNombre.get() 
       print("El nombre del Usuario es: ", dato1)

# BOTON 2
def codigoBoton2():                                    # codigoBoton es la funcion que hace algo(script) al momento que se aprieta el boton, debe estar antes que el boton
       dato2= miApellido.set("DIAZ")

##--->>
# BOTON 3
def codigoBoton3():
    print("Felicitaciones Lograste Abrir un fichero, desde una programacion Modular")
    #botonAbrir.command(abreFichero)

##--->>
##--->>
# BOTONES DE ELECION RADIOBUTTON




    

##-------------------CREACION DE VENTANA RAIZ-----------------------##

raiz= Tk()
#---->>
barraMenu= Menu(raiz)
#---->>

raiz.title("Ventana de pruebas")  # metodo para titulo de ventana raiz

raiz.resizable(True,True)   # Dimensiones modificables de la ventana raiz "ancho-alto (true, false)"
raiz.geometry("850x900")  # Determino el  ancho y el alto por defecto
#raiz.iconbitmap("imagen.ico") #  poner por ruta de arhcivo pequeño 15kb
####  Para que solo nos habra la Ventana GUI
####    y no la consola debo podificar cambiar  .py  por .pyw
raiz.config(bg="blue", menu= barraMenu)  #---> agrego la barra menu a la configuracion de la ventana raiz






#########################################################################
######  ----------------      CREACION DE FRAMES     ------------  ######
#########################################################################


miFrame1 = add_frame(raiz, 450, 400, [0,0], "red")
miFrame2 = add_frame(raiz, 450, 500, [1,0], "green")
miFrame3 = add_frame(raiz, 200, 340, [0,1], "yellow")
#miFrame4 = add_frame(raiz, 200, 340, [1,1], "brown")

##  variables de funciones interactivas...(de botones)

miNombre=StringVar()
miApellido=StringVar()
miFormacion=StringVar()
miPassword=StringVar()
numeroPantalla= operacion(StringVar())




#########################################################################
######   ---------------MOFIFICACION DE FRAMES ---- -------------  ######
#########################################################################

#--------------------   Etiquetas dentro de frame---------------------///

###### ////FRAME 1//// ######

nombreLabel=add_label(miFrame1, "NOMBRE: ", [0,0])

apellidoLabel=add_label(miFrame1, "APELLIDO: ", [1,0])

formacionLabel=add_label(miFrame1, "FORMACION: ", [2,0])

passLabel=add_label(miFrame1, "PASSWORD: ", [3,0])

comentarioLabel=add_label(miFrame1, "Comentarios: ", [4,0])

###### ////FRAME 2//// ######

moduloLabel=add_label(miFrame2, "MODULO", [0,0])

funcionLabel=add_label(miFrame2, "FUNCION", [1,0])

responsableLabel=add_label(miFrame2, "RESPONSABLE", [2,0])



#--------------------   Cuadros de Texto -------------------------///

###### ////FRAME 1//// ######

nombreEntry=add_entry(miFrame1, miNombre, [0,1], "green", )
apellidoEntry=add_entry(miFrame1, miApellido, [1,1], "blue")
formacionEntry=add_entry(miFrame1, miFormacion, [2,1], "blue")
passEntry=add_entry(miFrame1, miPassword, [3,1], "blue", hide=True)
comentTexto=add_text(miFrame1, 22, 3, [4,1], "blue")
scrollvert=add_scroll(miFrame1, comentTexto.yview, [4,2])

comentTexto.config(yscrollcommand = scrollvert.set)  ##  con el comando yscrollcommand = scrollVert.set  el posicionador del scrollbar me sigue en el Text

###### ////FRAME 2//// ######

moduloEntry=add_entry(miFrame2, None, [0,1], "red")
funcionEntry=add_entry(miFrame2, None, [1,1], "red")
responsableEntry=add_entry(miFrame2, None, [2,1], "red")

##### ////FRAME 3//// ######

pantalla=add_entry(miFrame3, numeroPantalla.variable, [0,0], "white", padx=10, pady=10, background="black", 
	columnspan=4, justify="right", width="40")

#-------------------------   Botones  ---------------------------///

###### ////FRAME 1//// ######

botonGuardar=add_button(miFrame1, "GUARDAR", [5,0])
botonGuardar.config(command=codigoBoton1)
botonEscribir=add_button(miFrame1, "ESCRIBIR", [5,1])
botonEscribir.config(command=codigoBoton2)

###### ////FRAME 2//// ######



###### ////FRAME 3//// ######

#El FRAME 3 presenta una cantidad de 16 botones, con comandos recursivos. A fin de ahorrar espacio
#en código, se crea un bucle de columnas y filas predeterminadas, junto a los 16 distintos textos
#a insertar en cada boton.

filas=4
columnas=4
boton = []
textos = ["7","8","9","*","4","5","6","/","1","2","3","-","=","0",",","+"]

for i in range(filas):
	for j in range(columnas):
		boton.append(add_button(miFrame3,textos[(columnas*i+j)],[i+1,j], fg="blue", background="orange", width=7))
		if textos[(columnas*i+j)] != "=":
			key = textos[(columnas*i+j)]
			boton[-1].config(command=lambda key=key:numeroPantalla.press(key))
		else:
			boton[-1].config(command=lambda:numeroPantalla.equal())


##############################################################################
##---------------------    FIN MODIFICACION FRAMES   -----------------------##
##############################################################################


##############################################################################
##---------------------    BARRA DE MENU DE RAIZ  inicio   -----------------##
##############################################################################

##----------------------    DEFINICION DE FUNCIONES PARA MENU  -----------------------##

def infoAdicional():
	messagebox.showinfo("Procesador de Series de Tiempo", "Análisis de Series de Tiempo version 2020")

## Para cambiar la funcionalidad de la ventana SOLO DEBO CAMBIAR EL METODO del messagebox
# Tipos de metodos para ventanas emergentes

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    valor= messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") # Este metodo devuelve un valor por lo que se puede lo transformar en una variable
    if valor== "yes":
       raiz.destroy()

def cerrarDocumento():
    valor2= messagebox.askretrycancel("Reintentar", "No es posible cerrar, Documento bloqueado") #  este metodo devuelve un booleano
    if valor2== False:
       raiz.destroy()

def cerrarAplicacion():
    valor1= messagebox.askokcancel("Cerrar", "¿Deseas cerrar la Aplicación?")
    if valor1== True:
       raiz.destroy()

##-------    DEFINICION DE FUNCIONES PARA BOTON DE FICHERO  ----------------##
def abreFichero():
    fichero= filedialog.askopenfilename(title="Abrir", initialdir="/home/juan/programacion Python juan/DESARROLLO INTERFAZ GRAFICA MODULAR/InterfazGrafica1v2/") 
# la funcion debe definir la ruta donde buscara el archivo en tu compu por defecto
# ademas te imprime la ruta en la shell
    print(fichero)	

#---->>
botonAbrir=add_button(miFrame1, "Abrir Fichero", [6,0])
botonAbrir.config(command= abreFichero)
#botonAbrir.config(command=codigoBoton3)  ### NO FUNCIONA ASI EL CODIGO!!!!!!!
#---->>

##---------- DEFINICION DE PESTAÑAS  PARA MENU  COMO OBJETOS INFORMATICO  -------------##


#-------------------------   Pestaña ARCHIVO  ---------------------------///


archivoMenu= Menu(barraMenu,tearoff= 0)
#### Sub_pestañas
archivoMenu.add_command(label= "Nuevo")
archivoMenu.add_command(label= "Guardar")
archivoMenu.add_command(label= "Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label= "Cerrar", command= cerrarDocumento)
archivoMenu.add_command(label= "Salir", command= salirAplicacion)


#-------------------------   Pestaña EDICION ---------------------------///

archivoEdicion= Menu(barraMenu,tearoff= 0)
#### Sub_pestañas
archivoEdicion.add_command(label= "Copia")
archivoEdicion.add_command(label= "Cortar")
archivoEdicion.add_command(label= "Pegar")

#-------------------------   Pestaña HERRAMIENTAS ---------------------------///

archivoHerramientas= Menu(barraMenu)

#-------------------------   Pestaña AYUDA ---------------------------///

archivoAyuda= Menu(barraMenu,tearoff= 0)
#### Sub_pestañas
archivoAyuda.add_command(label= "Licencia", command= avisoLicencia)
archivoAyuda.add_command(label= "Acerca de ...", command= infoAdicional)

##---------- DEFINICION DE INTEFAZ GRAFICA PARA PESTAÑAS DEL MENU  -------------##

barraMenu.add_cascade(label= "Archivo", menu= archivoMenu)
barraMenu.add_cascade(label= "Edicion", menu= archivoEdicion)
barraMenu.add_cascade(label= "Herramientas", menu= archivoHerramientas)
barraMenu.add_cascade(label= "Ayuda", menu= archivoAyuda)




###### ////FRAME 4//// ######

varOpcion= IntVar()


def imprimir():
    
     eleccion= varOpcion.get()
     if eleccion != 1:
        print("El usuario selecciono: MIEMBRO")
        #etiqueta.config(text= "Has elegido Miembro del Laboratorio de Neurociencias Humanas")
     else:    
        print("El usuario selecciono : INVITADO")
        etiqueta.config(text= "Has elegido: Invitado del Laboratorio") 
     
               
Label(raiz, text= "Relacion de Pertenencia.")#.pack()

### Los Radiobutton son para preguntas excluyentes donde puede elegir solo una opcion posible
Radiobutton(raiz, text= "Invitado", variable= varOpcion, value= 1, command= imprimir )#.pack()

Radiobutton(raiz, text= "Miembro", variable= varOpcion, value= 2, command= imprimir )#.pack()

etiqueta= Label(raiz)
#etiqueta.pack()


##############################################################################
##---------------------    BARRA DE MENU DE RAIZ  fin      -----------------##
##############################################################################


raiz.mainloop()  ###  cierre del script

########################################################################
########################################################################
########################################################################

