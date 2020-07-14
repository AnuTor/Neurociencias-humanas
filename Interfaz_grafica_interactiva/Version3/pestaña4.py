##########################
##  DESARROLLAR INTERFAZ GRAFICA EN PYTHON
#### 3 COMPONENTES PRINCIPALLES    Raiz(tk)  -  Frame  -   Widgets


#########################################################################
##########################################################################
##########################################################################


####------------------  DESARROLLO DE LA VENTANA RAIZ  ---------------####



from tkinter import *  ##  es una libreria que trabaja tambien con imagenes gif y png

raiz= Tk()

raiz.title("Ventana de pruebas")  # metodo para titulo de ventana raiz

raiz.resizable(True,True)   # Dimensiones modificables de la ventana raiz "ancho-alto (true, false)"
raiz.geometry("750x500")  # Determino el  ancho y el alto por defecto
#raiz.iconbitmap("imagen.ico") #  poner por ruta de arhcivo pequeño 15kb
####  Para que solo nos habra la Ventana GUI
####    y no la consola debo podificar cambiar  .py  por .pyw
raiz.config(bg="orange")

varOpcion= IntVar()


def imprimir():
    
     eleccion= varOpcion.get()
     if eleccion != 1:
        print("El usuario selecciono: MIEMBRO")
        etiqueta.config(text= "Has elegido Miembro del Laboratorio de Neurociencias Humanas")
     else:    
        print("El usuario selecciono : INVITADO")
        etiqueta.config(text= "Has elegido: Invitado del Laboratorio") 
     
               
Label(raiz, text= "Relacion de Pertenencia.").pack()

### Los Radiobutton son para preguntas excluyentes donde puede elegir solo una opcion posible
Radiobutton(raiz, text= "Invitado", variable= varOpcion, value= 1, command= imprimir ).pack()

Radiobutton(raiz, text= "Miembro", variable= varOpcion, value= 2, command= imprimir ).pack()

etiqueta= Label(raiz)
etiqueta.pack()

# como rescatar los valores que pulsa el usuario

## Trabajar introduciendo una imagen

foto= PhotoImage(file="cerebro_circuito3.png")  # no me acepta archivos jpeg
Label(raiz, image=foto).pack()

Label(raiz, text= "Tu Formacion es: ").pack()
Checkbutton(raiz, text= "Ingeniero").pack()
Checkbutton(raiz, text= "Bioquimico").pack()
Checkbutton(raiz, text= "Médico").pack()
Checkbutton(raiz, text= "Psicologo").pack()
Checkbutton(raiz, text= "Biologo").pack()
Checkbutton(raiz, text= "Fisico").pack()

### Los Checkbutton  son para elecciones multiples 

########################################################################
########################################################################
########################################################################






raiz.mainloop()  ###  cierre del script

########################################################################
########################################################################
########################################################################
