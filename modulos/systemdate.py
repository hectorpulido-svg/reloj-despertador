# -*coding: utf-8 -*-

from tkinter import Label, StringVar
import time
import threading

# Diccionarios de traducción
day = {'monday': 'lunes', 'tuesday': 'martes', 'wednesday': 'miercoles', 'thursday': 'jueves', 'friday': 'viernes', 'saturday': 'sábado', 'sunday': 'domingo'}
month = {'january': 'enero', 'february': 'febrero', 'march': 'marzo', 'april': 'abril', 'may': 'mayo', 'june': 'junio', 'july': 'julio', 'august': 'agosto', 'september': 'septiembre', 'october': 'octubre', 'november': 'noviembre', 'december': 'diciembre'}

class SYSDATE(Label):
    '''
        Display para la fecha.

        args, kwrds:

            (master: contenedor, row: int, column: int, columnspan:int, display_font={})

        propiedades publicas:

            display_font: La tipográfia del texto {font: nombre, size: int, type: normal | italic | bold}
            
                NOTA:
                    si en algun momento se decide cambiarla
                    se debe ejecutar el metodo update() inmediatamente despues.

        metodos:

            update(): Actualiza la fecha
    '''

    def __init__(self, master, row, column, columnspan=1, display_font={}, textColor='white'):
        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.sisdate = StringVar()
        self.display_font = display_font
        self.textColor = textColor
        self.sisdate.set('')
        self.config(
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            textvariable = self.sisdate,
            fg = self.textColor,
            bg = self.master['bg'],
            padx = 5,
            pady = 10
        )
        self.grid(row=self.row, column=self.column, columnspan=self.columnspan)
        self.ledSS = ledSS.LEDSS(self.sisdate.get())

    def updateDisplay(self):

        self.sisdate.set(day[time.strftime('%A').lower()] + chr(32) + time.strftime('%d') + chr(32) + month[time.strftime('%B').lower()])
        self.config(textvariable=self.sisdate, font = (self.display_font['font'], self.display_font['size'], self.display_font['type']))
        self.ledSS.update(self.sisdate.get())

    def ledScreenSimulation(self):
        '''
            usa el nombre del archivo seleccionado como
            texto para el botón y aplica una animación.
            
        '''
        self.sisdate.set(self.ledSS.roll())
        self.config(textvariable=self.sisdate)
        self.after(round(3000 / len(self.sisdate.get())), self.ledScreenSimulation)

if __name__ == '__main__':

    from tkinter import Tk
    from utils import ledSS
    '''
        una muestra del widget
    '''
    app = Tk()
    app.config(bg='black')
    D = SYSDATE(app, 0, 0, display_font = {'font': 'Impact', 'size': 20, 'type': 'normal'}, textColor='red')
    D.updateDisplay()
    D.ledScreenSimulation()
    app.mainloop()
else:
    '''
        modulo
    '''
    from .utils import ledSS