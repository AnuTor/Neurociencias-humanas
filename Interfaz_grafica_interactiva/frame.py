# Conjunto de funciones destinada a modificar el GUI presente, agregando frames a la ventana
# y configurandolos con el grosor, posicion y fondo adecuado
# 
# (Como una medida de optimización, se pueden llevar las funciones a una clase, y asi no tener que
#  asignar en cada momento los mismos parametros, independientemente de lo que se quiera crear)
#

from tkinter import *

def add_frame(mi_frame, width, height, pos, bg, bd=15, relief="sunken", cursor="hand2"):
	#La funcion add_frame agrega un frame a "mi_frame", con una altura y anchura determinada, junto
	#a su pocicion y color de fondo. El ancho, tipo del borde, y el puntero del cursor pueden ser
	#modificados tambien.

	frame = Frame(mi_frame)
	pos_frame = frame
	pos_frame.grid(row=pos[0], column=pos[1], padx= 5, pady= 5, sticky= "nw")
	frame.config(bg= bg)   # dale un color al frame
	frame.config(width=str(width),height=str(height))
	frame.config(bd=bd)  # defino ancho de borde
	frame.config(relief= relief)  ## defino tipo de borde
	frame.config(cursor= cursor)  ##  cambia el puntero del  cursor
	
	return frame

def add_label(mi_frame, texto, pos, sticky = "e", padx = 5, pady = 5):
	#La funcion add_label agrega un label al frame "mi_frame", en una posicion predeterminada (Pasada como lista)
	#junto a un texto anexado a dicho label. El ancho, tipo del borde, y el puntero del cursor pueden ser
	#modificados tambien.

	label = Label(mi_frame, text=str(texto))
	label.grid(row=pos[0], column=pos[1], sticky=sticky, padx=padx, pady=pady)

	return label

def add_entry(mi_frame, textvar, pos, fg, hide=False, padx=5, pady=5, background="white", justify="center", width="20", columnspan=1):

	#La funcion add_entry agrega una entrada de texto al frame "mi_frame", en una posicion predeterminada 
	#(Pasada como lista) junto a una variablede texto. El ancho, la justificacion, color de fondo y tamaño
	#de letra puede ser modificados tambien.

	entry = Entry(mi_frame, textvariable= textvar)
	entry.grid(row = pos[0], column=pos[1], padx=padx, pady=pady, columnspan=columnspan)
	entry.config(fg=str(fg), justify=str(justify), background=str(background), width=str(width))

	if hide:
		entry.config(show="*")

	return entry

def add_text(mi_frame, width, height, pos, fg, padx=5, pady=5):

	#La funcion add_text agrega una entrada de texto de multiples lineas al frame "mi_frame", en una 
	#posicion predeterminada pasada como lista, un ancho y altura, posicion en el frame, y color de 
	#letra. El ancho del borde puede ser modificado.

	text = Text(mi_frame, width=width, height=height) ##  TENEMOS QUE DELIMITAR EL TAMAÑO LUEGO DEL FRAME
	text.grid(row=pos[0], column=pos[1], padx=padx, pady=pady) # este metodo hace un cuadro de texto
	text.config(fg=str(fg))

	return text

def add_scroll(mi_frame, command, pos, padx=5, pady=5):

	#La funcion add_scroll agrega un scrollbar al frame "mi_frame", anexandolo al cuadro de texto en la
	#posicion contigua (ingresada como una lista). El ancho del borde puede ser modificado.
	
	scroll = Scrollbar(mi_frame, command= command) # con esta instruccion construyo el scrollbar pero falta colocarlo
	scroll.grid(row=pos[0], column= pos[1], padx= padx, pady= pady, sticky= "snew") ##  con el parametro sticky lo hacemos de la misma altura que el Text

	return scroll

def add_button(mi_frame, texto, pos, width=0, height=0, padx=5, pady=5, background=None, fg="black"):

	#La funcion add_button agrega un boton interactivo al frame "mi_frame". Dicho boton presenta un texto
	# y una posicion predeterminada (ingresada a la funcion como una lista de coordenadas). El alto, ancho,
	#fondo y color de la letra del boton puede ser modificado, pero presentan configuraciones por defecto.
	###El comando del boton (la funcion que este cumple), se ingresa fuera de la funcion (Posible opt)### 

	button = Button(mi_frame, text=str(texto), width=width, background=background, fg=fg)  ## para lograr que el boton ejecute una accion tengo que agregar el parametro command)
	button.grid(row=pos[0], column=pos[1], padx=padx, pady=pady)
	#botonEscribir.pack(side="left",  anchor="w" )
	#botonGuardar.pack(side="left",  anchor="s" )
	return button