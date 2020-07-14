##########################
##  DESARROLLAR INTERFAZ GRAFICA EN PYTHON
#### 3 COMPONENTES PRINCIPALLES    Raiz(tk)  -  Frame  -   Widgets


#########################################################################
##########################################################################
##########################################################################


####------------------  IMPORTACION DE MODULOS RELEVANTES  ---------------####


from tkinter import *  ##  es una libreria que trabaja tambien con imagenes gif y png
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

##-------------------CREACION DE VENTANA RAIZ-----------------------##

raiz= Tk()

raiz.title("Ventana de pruebas")  # metodo para titulo de ventana raiz

raiz.resizable(True,True)   # Dimensiones modificables de la ventana raiz "ancho-alto (true, false)"
raiz.geometry("750x500")  # Determino el  ancho y el alto por defecto
#raiz.iconbitmap("imagen.ico") #  poner por ruta de arhcivo pequeño 15kb
####  Para que solo nos habra la Ventana GUI
####    y no la consola debo podificar cambiar  .py  por .pyw
raiz.config(bg="blue")


#########################################################################
######  ----------------      CREACION DE FRAMES     ------------  ######
#########################################################################


miFrame1 = add_frame(raiz, 450, 300, [0,0], "red")
miFrame2 = add_frame(raiz, 450, 300, [1,0], "green")
miFrame3 = add_frame(raiz, 200, 340, [0,1], "yellow")

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

raiz.mainloop()  ###  cierre del script

########################################################################
########################################################################
########################################################################

