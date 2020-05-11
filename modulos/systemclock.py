# -*coding: utf-8 -*-

from tkinter import LabelFrame, StringVar, Label, PhotoImage
import time
import threading
#=====================================================

class SYSTEMCLOCK:
    '''
        Display para la hora del sistema

        args, kwrds:

            (master: contenedor, row: int, column: int, display_font: {}, text_font: {})

        propiedades publicas:

            display_font: La tipográfia de los digitos {font: nombre, size: int, type: normal | italic | bold}
            text_font: La tipográfia de los textos {font: nombre, size: int, type: normal | italic | bold}

                    NOTA:
                        si en algun momento se decide cambiar alguna o ambas
                        debe ejecutarse el metodo update() inmediatamente despues.

        propiedades protegidas:

            _meridian: am | pm
            currentTime: hora del sistema

        metodos:

            tictac(): Actualiza la hora.
            update() : Actualiza el display.

    '''

    def __init__(self, master, row, column, display_font={}, text_font={}, textColor='white'):
        self.__master = master
        self.__row = row
        self.__column = column
        self.display_font = display_font
        self.text_font = text_font
        self.textColor = textColor
        self.currentTime = StringVar()
        #----------------- CLOCK GROUP -------------------
        self.__clockFrame = LabelFrame(self.__master, text='Reloj')
        self.__clockFrame.config(
            fg=self.textColor,
            bg = self.__master['bg'],
            pady=7,
            padx=4,
            bd=2,
            relief='ridge'
            )
        # realif styles --> flat, groove, raised, ridge, solid, or sunken
        self.__clockFrame.grid(row=self.__row, column=self.__column)
        #----------------- CLOCK DISPLAY -------------------
        self.__clockDisplay = Label(self.__clockFrame)
        self.__glass = PhotoImage(file='.\\img\\ui\\fondoDisplays.gif')
        self.__clockDisplay.config(
            textvariable = self.currentTime,
            pady = 0,
            padx = 0,
            bd = 0,
            fg = self.textColor,
            image = self.__glass,
            compound = 'center'
        )
        self.__clockDisplay.grid(row=1, column=0, padx=4, pady=4)
        #------------  AM/PM -----------
        self._meridian = StringVar()
        self._meridian.set(time.strftime('%p').lower())
        self.__meridianDisplay = Label(self.__clockFrame)
        self.__meridianDisplay.config(
            fg=self.textColor,
            bg=self.__master['bg'],
            textvariable=self._meridian,
            pady=0,
            padx=0,
            bd=0
        )
        self.__meridianDisplay.grid(row=0, column=0, sticky='ne')
        self.hide_show_separator = (lambda x: time.strftime('%I %M') if x % 2 == 0 else time.strftime('%I:%M'))
        self.update()

    def tictac(self):
        '''
            Actualiza la hora
        '''
        self.seconds = int(time.strftime('%S'))

        self.currentTime.set(
            (self.hide_show_separator)(self.seconds)
            )

        self._meridian.set(time.strftime('%p').lower())
        self.__clockFrame.after(1000, self.tictac)

    def update(self):
        '''
            Actualiza el Display
        '''
        self.__clockFrame.config(
            font = (self.text_font['font'], self.text_font['size'], self.text_font['type']))
        self.__clockDisplay.config(
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']), fg = self.textColor)
        self.__meridianDisplay.config(
            font = (self.text_font['font'], self.text_font['size'], self.text_font['type']))


if __name__ == '__main__':
    '''
        Esta es una muestra del Objeto
    '''
    from tkinter import Tk
    app = Tk()
    app.config(bg='black')
    systemclock = SYSTEMCLOCK(app, row=0, column=0, display_font={'font':'SF Digital Readout', 'size':30, 'type':'normal'}, text_font={'font': 'Arial', 'size': 10, 'type': 'normal'}, textColor = 'red')
    systemclock.tictac(0)
    app.mainloop()
else:
    '''
        modulo systemclock.py
    '''
    pass