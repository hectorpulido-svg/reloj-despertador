# -*coding: utf-8 -*-
from tkinter import LabelFrame, Label, Entry, StringVar
import time


class ALARM(LabelFrame):
    '''
        Display para la entrada de la Alarma

        args, kwrds:

            (master: contenedor, row: int, column: int, display_font: {}, text_font: {}, textColor=color)

        propiedades publicas:

            display_font: La tipografia para los digitos {font: nombre, size: int, type: normal | italic | bold}
            text_font: La tipografia para los textos {font: nombre, size: int, type: normal | italic | bold}
            textColor: string => 'white' el color de los digitos por defecto blanco 

                    NOTA:
                        si en algun momento se decide cambiar alguna o ambas propiedades
                        se debe ejecutar el metodo update() inmediatamente despues.

        propiedades protegidas:

            _meridian: am | pm

            displayMinust  
            displayMinuts: Estas propiedad son especiales ya que se utilizan para
                            dar el foco y seleccionar el primer elemento del dislay
                            por medio de los metodos: focus_set(), select_adjust()
                                 
                                 

                    NOTA:
                        no es comveniente manipular otras propiedades o metodos
                        vinculados a ella

        metodos:

            update(): Actualiza el display

    '''

    def __init__(self, master, row, column, textColor='white', display_font={}, text_font={}):
        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.display_font = display_font
        self.text_font = text_font
        self.textColor = textColor
        self.alarmTime = StringVar()
        self.config(
            text='Alarma',
            bg = self.master['bg'],
            fg=self.textColor,
            pady=18,
            padx=5,
            bd=2,
            relief='ridge'
            )
        self.grid(row=self.row, column=self.column)
        ###########################################
        #             DISPLAY HOURS               #
        self.displayHours = TWODIGITBRICK(self, 1, 0, textColor=self.textColor, display_font=self.display_font)
        #               SEPARADOR                 #
        self.separator = Label(self)
        self.separator.config(
            text=':',
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            fg =self.textColor,
            bg = self.master['bg']
            )
        self.separator.grid(row=1, column=1)
        #             DISPLAY MINUTS              #
        ###########################################
        self.displayMinuts = TWODIGITBRICK(self, 1, 2, textColor=self.textColor, display_font=self.display_font)
        ###########################################
        #                AM/PM ALARMA             #
        ###########################################
        self._meridian = StringVar()
        self._meridian.set(time.strftime('%p').lower())
        self.display_meridian = Label(self)
        self.display_meridian.config(
            fg=self.textColor,
            bg=self.master['bg'],
            textvariable=self._meridian,
            pady=0,
            padx=0,
            bd=0
        )
        self.display_meridian.grid(row=0, column=2, sticky='ne')
        self.displayHours.bind('<KeyRelease>', self.updateTime)
        self.displayMinuts.bind('<KeyRelease>', self.updateTime)
        self.displayHours.bind('<KeyPress>', self.focusOnHours)
        self.displayMinuts.bind('<KeyPress>', self.focusOnMinuts)
        self.am_pm_switcher = (lambda x: 'pm' if x=='am' else 'am')

    def updateTime(self, e):
        self.alarmTime.set(self.displayHours.get() + ':' + self.displayMinuts.get())

    def focusOnHours(self, e):
        if e.keycode == 13:
            self.displayMinuts.focus_set()
            self.displayMinuts.select_range(0, 1)

    def focusOnMinuts(self, e):
        if e.keycode == 13:
            self.displayHours.focus_set()
            self.displayHours.select_range(0, 1)
    
    def am_pm(self):
        self._meridian.set(self.am_pm_switcher(self._meridian.get()))
        self.display_meridian.config(textvariable=self._meridian)

    def update(self):
        self.config(
            font = (self.text_font['font'], self.text_font['size'], self.text_font['type']))
            
        self.display_meridian.config(
            font = (self.text_font['font'], self.text_font['size'], self.text_font['type']))

    def reset(self):
        self.displayHours.reset()
        self.displayMinuts.reset()
        self.updateTime(None)
        self.displayHours.focus_set()
        self.displayHours.select_range(0, 1)




if __name__ == '__main__':
    '''
        una muestra del Objeto
    '''
    from tkinter import Tk
    from utils.twodigitbrick import TWODIGITBRICK
    app = Tk()
    app.config(bg='black')
    entry = ALARM(app, row=0, column=0, display_font={'font':'SF Digital Readout', 'size':30, 'type':'normal'}, text_font= {'font':'Arial', 'size':10, 'type':'normal'}, textColor = 'red')
    entry.displayHours.focus_set()
    entry.displayHours.select_adjust(1)
    app.mainloop()
else:
    '''
        modulo alarmEntry.py
    '''
    from .utils.twodigitbrick import TWODIGITBRICK
    # pass
