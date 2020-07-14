

from tkinter import *  ##  es una libreria que trabaja tambien con imagenes gif y png
#------->>
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
from miFrameB import *


import sqlite3
#from turtle import Screen
#pantalla= Screen()
# ------>>
#from calculos import operacion 
#from frame import *



    

##-------------------CREACION DE VENTANA RAIZ-----------------------##

#raiz= Tk()
raiz=Toplevel()  #### CUANDO CAMBIASTE ESTA OPCION TE PERMITI ALTERNAR ENTRE LOS RADIO_BUTTON Y CARGAR DOS FOTOS 
#---->>

barraMenu= Menu(raiz)

foto= PhotoImage(file="OrganigramaLab.png")  # no me acepta archivos jpeg
foto2= PhotoImage(file="cerebro_circuito3.png")  
#---->>

raiz.title("LABORATORIO NEUROCIENCIAS HUMANAS")  # metodo para titulo de ventana raiz

raiz.resizable(True,True)   # Dimensiones modificables de la ventana raiz "ancho-alto (true, false)"
raiz.geometry("650x300")  # Determino el  ancho y el alto por defecto
#raiz.iconbitmap("imagen.ico") #  poner por ruta de arhcivo pequeño 15kb
####  Para que solo nos habra la Ventana GUI
####    y no la consola debo podificar cambiar  .py  por .pyw
raiz.config(bg="white", menu= barraMenu)  #---> agrego la barra menu a la configuracion de la ventana raiz


#miFrame0= Frame(raiz)
#miFrame0.pack(side= "right")

#miFrameA= Frame(raiz)
#miFrameA.pack()
#miFrameA.config(bg="green")
#posicionFrameA= miFrameA
#posicionFrameA.grid(row=0, column=0, padx= 5, pady= 5,sticky= "nw") 
#miFrameA.config(width="400", height="300")

miFrame0= Frame(raiz)
miFrame0.pack(side="right", anchor= "n")
miFrame0.config(bg="brown")



miFrame1= Frame(raiz)
miFrame1.pack(side= "left", anchor= "n", fill="both", expand= "True")
miFrame2= Frame(raiz)
miFrame2.pack(side= "left", anchor= "n", fill="both", expand= "True")
miFrame3= Frame()
miFrame3.pack(side= "left", anchor= "n", fill="both", expand= "True")
miFrame4= Frame()
miFrame4.pack(side= "left", anchor= "n", fill="both", expand= "True")

##--VARIABLES GLOBALES DE FUNCIONES INTERNAS  AUN CUANDO SE LAS LLAME DESDE OTRO FRAME DEBE IR AFUERA
##------------------//
varOpcion= IntVar()
##------------------//

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

def mostrarOrganigrama():
       a= Label(raiz, image=foto).pack()
##-------------------------------------##
def mostrarFrame1():
    miFrame1.config(bg="red")
    miFrame1.config(width="300", height="300")
    miConexion= sqlite3.connect("Base de Datos Pacientes")
    miCursor= miConexion.cursor()
    ##------>> CREAR
    miCursor.execute('''CREATE TABLE PACIENTES (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE VARCHAR(50),
                     APELLIDO VARCHAR(50) ,
                     DNI VARCHAR(50) UNIQUE,
                     EDAD INTEGER,
                     DIRECCION VARCHAR(50) ,
                     DIAGNOSTICO VARCHAR (20))                
    ''')

    variosPacientes=[
        ("Juan Manuel", "Diaz",29208554, 38, "Lagunilla 2725", "Cientifico Loco"),
        ("Victoria", "Flores",29208555, 36, "Nuevo Hogar", "Psicopecadora"),
        ("Lyhuen", "Diaz Flores",29208556, 11, "Cama de al lado", "Fortnite dependiente"),
        ("Kumelen", "Diaz Flores",29208557, 10, "Pieza Grande", "Hipercreatividad"),
        ("Suyai", "Diaz Flores",29208558, 6, "Cama Chica ", "Danzarina Maniaca")
    ]
    ##------->> INSERTAR POR PRIMERA VEZ MUCHOS
    miCursor.executemany("INSERT INTO PACIENTES VALUES (NULL,?,?,?,?,?,?)", variosPacientes)
    ##miCursor.execute("INSERT INTO PACIENTES VALUES('Juan Manuel', 'Diaz',38, 'Lagunilla 2725', 'Cientifico Loco')")  ##instruccion ingresar dato
    '''variosProductos=[
      ('Camiseta', 10, 'Deportes'),
       ('Jarron', 90, 'Ceramica'),
      ('Camion', 20, 'Jugueteria')
      ]'''  ## INSERTAR VARIOS PACIENTES POR PRIMERA VEZ

    ##------->>  LEER
    '''miCursor.execute("SELECT* FROM PACIENTES")
    variosPacientes= miCursor.fetchall()
    print(variosPacientes)
    for Paciente in variosPacientes:
        print("Apellido del Paciente: ", Paciente[1], ",  Diagnostico: ", Paciente[4] )'''
    ##-------->>
    '''variosProductos=[
      ('Camiseta', 10, 'Deportes'),
       ('Jarron', 90, 'Ceramica'),
      ('Camion', 20, 'Jugueteria')
      ]'''
    miConexion.commit()
    miConexion.close()


       
def cerrarFrame1():
    valor1= messagebox.askokcancel("Cerrar", "¿Deseas cerrar la Frame1?")
    if valor1== True:
       miFrame1.destroy()
##--------------------------------------##  
def mostrarFrame2():
    miFrame2.config(bg="blue")
    miFrame2.config(width="300", height="300")
    
    def imprimir():
       
        eleccion= varOpcion.get()
        if eleccion != 1:
             print("El usuario selecciono: MIEMBRO")
             etiqueta.config(text= "Has elegido Miembro del Laboratorio de Neurociencias Humanas")
        else:    
             print("El usuario selecciono : INVITADO")
             etiqueta.config(text= "Has elegido: Invitado del Laboratorio") 
         
               
    Label(miFrame2, text= "Relacion de Pertenencia.").pack()

        ### Los Radiobutton son para preguntas excluyentes donde puede elegir solo una opcion posible
   
    Radiobutton(miFrame2, text= "Invitado", variable= varOpcion, value= 1, command= imprimir ).pack()
    Radiobutton(miFrame2, text= "Miembro", variable= varOpcion, value= 2, command= imprimir ).pack()

    etiqueta= Label(miFrame2)
    etiqueta.pack()

    Label(miFrame2, text= "Tu Formacion es: ").pack()
    Checkbutton(miFrame2, text= "Ingeniero").pack()
    Checkbutton(miFrame2, text= "Bioquimico").pack()
    Checkbutton(miFrame2, text= "Médico").pack()
    Checkbutton(miFrame2, text= "Psicologo").pack()
    Checkbutton(miFrame2, text= "Biologo").pack()
    Checkbutton(miFrame2, text= "Fisico").pack()

        ### Los Checkbutton  son para elecciones multiples 
    Label(miFrame2, image=foto2).pack()
        ########################################################################
        ########################################################################
        ########################################################################




   

    
def cerrarFrame2():
    valor1= messagebox.askokcancel("Cerrar", "¿Deseas cerrar la Frame2?")
    if valor1== True:
       miFrame2.destroy()

##----------------------------------##
def add_mostrarFrame3():
      
    return mostrarmiFrame3()

def add_cerrarFrame3():
    return cerrarFrame3()
##----------------------------------##
def add_mostrarFrame4():
    return mostrarmiFrame4()
    
def add_cerrarFrame4():
     return cerrarFrame4()
      
##---------------------------------##

    
#---->>
#botonAbrir=add_button(miFrame1, "Abrir Fichero", [6,0])
#botonAbrir.config(command= abreFichero)
#botonAbrir.config(command=codigoBoton3)  ### NO FUNCIONA ASI EL CODIGO!!!!!!!
#---->>

##---------- DEFINICION DE PESTAÑAS  PARA MENU  COMO OBJETOS INFORMATICO  -------------##


#-------------------------   Pestaña BIENVENIDOS  ---------------------------///

bienvenidosMenu= Menu(barraMenu, tearoff= 0)
#### Sub_pestañas
bienvenidosMenu.add_command(label= "Historia")
bienvenidosMenu.add_command(label= "MIembros")
bienvenidosMenu.add_command(label= "Organigrama", command= mostrarOrganigrama)



#### Sub_pestañas
#--------------------##-----------------------##
tipoProyectos= Menu(bienvenidosMenu, tearoff= 0) ## ESTA ES LA VINCULACION

#### Sub_SUBpestañas

tipoProyectos.add_command(label= "Investigacion Cientifica Colaborativa")
tipoProyectos.add_command(label= "Innovacion Tecnologica en Investigacion y Desarrollo ")
tipoProyectos.add_command(label= "Formacion Recurso Humano")
tipoProyectos.add_command(label= "Impacto Social y Extension Universitaria")
bienvenidosMenu.add_cascade(label= "Proyectos", menu= tipoProyectos )  ### ESTE ES EL PRINCIPAL

#### Sub_pestañas
#--------------------##-----------------------##
bienvenidosMenu.add_command(label= "Contactos")
bienvenidosMenu.add_separator()
#bienvenidosMenu.add_command(label= "Cerrar", command= cerrarDocumento)
bienvenidosMenu.add_command(label= "Salir", command= salirAplicacion)


#-------------------------   Pestaña CAMPOS DE ESTUDIO ---------------------------///

campodeEstudio= Menu(barraMenu,tearoff= 0)

#### Sub_pestañas
#--------------------##-----------------------##

datoEstudio= Menu(campodeEstudio, tearoff= 0) ## ESTA ES LA VINCULACION
#### Sub_SUBpestañas
datoEstudio.add_command(label= "Neuropsicologicos-Neurocognitivos  (papel)")
datoEstudio.add_command(label= "Neuroimagenes  (DICOM)")
datoEstudio.add_command(label= "Series de Tiempo Electrofisiologicas  (txt-csv-ascii-edf)")
datoEstudio.add_command(label= "Bioquimica y Fisiologia  (??)")
datoEstudio.add_command(label= "Genetico y Moleculares  (??)")
datoEstudio.add_command(label= "Neurofarmacologicos y Psicofarmacovigilancia (??)")
datoEstudio.add_command(label= "Audio_Visuales  (mp4-mpeg)")
datoEstudio.add_command(label= "Interactivos  (??)")
campodeEstudio.add_cascade(label= "Tipo de Datos", menu=datoEstudio )  ### ESTE ES EL PRINCIPAL

#### Sub_pestañas
#--------------------##-----------------------##
diseñoPesquisa= Menu(campodeEstudio, tearoff= 0) ## ESTA ES LA VINCULACION
diseñoPesquisa.add_command(label= "Estudios Transversales")
diseñoPesquisa.add_command(label= "Estudios de Cohorte")
diseñoPesquisa.add_command(label= "Estudios de Caso-Controles")
diseñoPesquisa.add_command(label= "Estudios de Intervención- Ensayo Clinico")
diseñoPesquisa.add_command(label= "Estudios de Ecologicos")
campodeEstudio.add_cascade(label= "Metodologia", menu=diseñoPesquisa)  ### ESTE ES EL PRINCIPAL

#### Sub_SUBpestañas


#### Sub_pestañas
#--------------------##-----------------------##

tematicaEstudio= Menu(campodeEstudio, tearoff= 0)  ### ESTA ES LA VINCULACION
#### Sub_SUBpestañas
tematicaEstudio.add_command(label= "Interfaz Cerebro-Computadora")
tematicaEstudio.add_command(label= "Psiconeuropatologia")
tematicaEstudio.add_command(label= "Neurodesarrollo y Ontogenia")
tematicaEstudio.add_command(label= "Aprendizaje y Funciones Mentales Superiores")
tematicaEstudio.add_command(label= "Modelado y Simulacion en Neurociencias")
tematicaEstudio.add_command(label= "Marcos Epistemologicos e Inferencia Cientifica")
tematicaEstudio.add_command(label= "Neurotecnologias")
campodeEstudio.add_cascade(label= "Tematica", menu=tematicaEstudio ) ###  ESTE ES EL PRINCIPAL
#--------------------##-----------------------##

#"Interfaz Cerebro-Computadora"
#-------------------------   Pestaña BBDD PERSONAS ---------------------------///

personasBBDD= Menu(barraMenu, tearoff= 0)
#### Sub_pestañas
datosPersonalesBBDD= Menu(personasBBDD, tearoff= 0)  ## aca esta la vinculacion

#### Sub_SUBpestañas
datosPersonalesBBDD.add_command(label= "Crear Base de Datos")
datosPersonalesBBDD.add_command(label= "Leer Base de Datos")
datosPersonalesBBDD.add_command(label= "Actualizar Base de Datos")
datosPersonalesBBDD.add_command(label= "Borrar Base de Datos")

personasBBDD.add_command(label= "Estudios Realizados")
personasBBDD.add_command(label= "Participacion en Protocolos")
personasBBDD.add_command(label= "Consentimientos Informados")

personasBBDD.add_cascade(label= "Datos Personales", menu= datosPersonalesBBDD) ###  ESTE ES EL PRINCIPAL

#-------------------------   Pestaña BBDD ESTUDIIOS ---------------------------///

estudioBBDD= Menu(barraMenu, tearoff= 0)
#### Sub_pestañas

tipoNeuropsicologicos= Menu(estudioBBDD, tearoff= 0)  ## aca esta la vinculacion

tipoNeuropsicologicos.add_command(label= "Test de Barcelona-D.E")
tipoNeuropsicologicos.add_command(label= "Test de Trazo A y B")
tipoNeuropsicologicos.add_command(label= "Test de Stroop")
tipoNeuropsicologicos.add_command(label= "Test de Atencion Selectiva de Ruff")
tipoNeuropsicologicos.add_command(label= "Test de Aprendizaje Auditivo Verbal de Rey")
tipoNeuropsicologicos.add_command(label= "Test de Memoria VIsual Continua")
tipoNeuropsicologicos.add_command(label= "Test de Fluides Verbal Fonologica")
tipoNeuropsicologicos.add_command(label= "Test de Fluides Verbal Semantica")
tipoNeuropsicologicos.add_command(label= "Test de Clasificacion de Cartas- Wisconsin")
tipoNeuropsicologicos.add_command(label= "Test de 5 puntos de Regard")
tipoNeuropsicologicos.add_command(label= "Test de Ordenamiento de Digitos de Cooper")

estudioBBDD.add_cascade(label= "Neuropsicologicos", menu= tipoNeuropsicologicos) ###  ESTE ES EL PRINCIPAL
#### Sub_pestañas
#--------------------##-----------------------##
tipoNeuroimagenes= Menu(estudioBBDD, tearoff= 0)  ## aca esta la vinculacion
tipoNeuroimagenes.add_command(label= "fRMN")
tipoNeuroimagenes.add_command(label= "Tractografia RMN")
tipoNeuroimagenes.add_command(label= "RMN simple")
tipoNeuroimagenes.add_command(label= "TAC")
tipoNeuroimagenes.add_command(label= "PET")
tipoNeuroimagenes.add_command(label= "SPECT")
estudioBBDD.add_cascade(label= "Neuroimagenes", menu= tipoNeuroimagenes) ###  ESTE ES EL PRINCIPAL

#### Sub_pestañas
#--------------------##-----------------------##

tipoSerieTiempo= Menu(estudioBBDD, tearoff= 0)  ## aca esta la vinculacion
tipoSerieTiempo.add_command(label= "Electroencefalografia")
tipoSerieTiempo.add_command(label= "Magnetoencefalografia")
tipoSerieTiempo.add_command(label= "Electromiografia")
tipoSerieTiempo.add_command(label= "Poligrafia y Polisomnografia")
tipoSerieTiempo.add_command(label= "Potenciales Relacionados a Eventos")

estudioBBDD.add_cascade(label= "Series de Tiempo", menu=tipoSerieTiempo ) ###  ESTE ES EL PRINCIPAL


estudioBBDD.add_command(label= "Bioquimicos y Fisiologicos")
estudioBBDD.add_command(label= "Geneticos y Moleculares")
estudioBBDD.add_command(label= "Neurofarmacologicos y Psiconeurofarmacovigilancia")
estudioBBDD.add_command(label= "Interactivos")
estudioBBDD.add_command(label= "Audio_Visuales")

#-------------------------   Pestaña PUBLICACIONES DEL LAB---------------------------///

publicacionesLab= Menu(barraMenu,tearoff= 0)
#### Sub_pestañas
publicacionesLab.add_command(label= "Revistas")
publicacionesLab.add_command(label= "Congresos")
publicacionesLab.add_command(label= "Tesinas")
publicacionesLab.add_command(label= "Tesis PhD")

#-------------------------   Pestaña AYUDA---------------------------///

archivoAyuda= Menu(barraMenu,tearoff= 0)
#### Sub_pestañas
archivoAyuda.add_command(label= "Licencia", command= avisoLicencia)
archivoAyuda.add_command(label= "Acerca de ...", command= infoAdicional)

##---------- DEFINICION DE INTEFAZ GRAFICA PARA PESTAÑAS DEL MENU  -------------##

barraMenu.add_cascade(label= "Bienvenidos al LAB", menu= bienvenidosMenu)
barraMenu.add_cascade(label= "Campos de Estudio", menu= campodeEstudio)
barraMenu.add_cascade(label= "Personas BBDD", menu= personasBBDD)
barraMenu.add_cascade(label= "Estudios BBDD", menu= estudioBBDD)
barraMenu.add_cascade(label= "Publicaciones", menu= publicacionesLab)
barraMenu.add_cascade(label= "Ayuda", menu= archivoAyuda)

#barraMenu.add_cascade(label= "Interfaz Cerebro Computadora", submenu= tematicaEstudio)

#miFrame4= Frame(raiz) 
#posicionFrame4= miFrame4
#raiz.grid(row=1, column=1, padx= 5, pady= 5, sticky= "se")

#miFrame4= Frame(raiz) 
#posicionFrame4= miFrame4
#posicionFrame4.grid(row=1, column=1, padx= 5, pady= 5, sticky= "se")
#Button(miFrame4, text="Abrir fichero", command=abreFichero).pack()

#posicionFrame0= miFrame0
#posicionFrame0.grid(row=0, column=1, padx= 5, pady= 5, sticky= "se")

#----------------------------------------------------------------##
botonFrame1=Button(miFrame0, text="Abrir Frame1", command= mostrarFrame1).pack(anchor="n")
botonFrame1C=Button(miFrame0, text="Cerrar Frame1", command= cerrarFrame1).pack(anchor="n")

#----------------------------------------------------------------##
botonFrame2=Button(miFrame0, text="Abrir Frame2", command= mostrarFrame2).pack(anchor="n")
botonFrame2C=Button(miFrame0, text="Cerrar Frame2", command= cerrarFrame2).pack(anchor="n")
#----------------------------------------------------------------##
botonFrame3=Button(miFrame0, text="Abrir Frame3", command= mostrarFrame3).pack(anchor="n")
botonFrame3C=Button(miFrame0, text="Cerrar Frame3", command= cerrarFrame3).pack(anchor="n")
#----------------------------------------------------------------##
botonFrame4=Button(miFrame0, text="Abrir Frame4", command= mostrarFrame4).pack(anchor="n")
botonFrame4C=Button(miFrame0, text="Cerrar Frame4", command= cerrarFrame4).pack(anchor="n")
#----------------------------------------------------------------##








raiz.mainloop()  ###  cierre del script

########################################################################
########################################################################
########################################################################

