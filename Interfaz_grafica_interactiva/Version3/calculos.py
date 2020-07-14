

from tkinter import *

class operacion:

  #Se define una clase "operacion" sobre la cual, al asignarsele un StrinVar() de tkinter, 
  #crea una clase sobre el programa raiz, destinada a las operaciones del widget de calculadora
  #de la ventana interactiva, inicializando la expresion a sumar como una cadena vacia y el resultado
  #como 0.

  def __init__(self, variable):
    
    self.variable = variable
    self.expresion = ""
    self.resultado = 0

  def press(self, num):
    #Funcion que traspasa las teclas pulsadas en la ventana interactiva a la expresion a sumar.
    self.expresion+= str(num)
    self.variable.set(self.expresion)

  def equal(self):

    #Tomando la expresion a sumar, esta funcion realiza las operaciones necesarias, y las traspasa
    #hacia la pantalla, indicando un error en caso de ser que así ocurra uno.

    try:
      
      self.resultado=str(eval(self.expresion))

      self.variable.set(self.resultado)

      self.expresion=""

    except:
      self.variable.set(" ERROR ")

      self.expresion=""