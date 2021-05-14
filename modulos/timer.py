# -*coding: utf-8 -*-
# =======================================================================
#
from tkinter import Tk, LabelFrame, Label
import winsound
import time


class TIMER(LabelFrame):
    '''
        Temporizador con entradas para minutos y segundos.

        args, kwrds:

            (master: contenedor, row: int, column: int, display_font={}: Tipográfia)

        propiedades:

            state: estado (False | True), por defecto False

        metodos:

            focusOnMinuts(): Pone el foco en la entrada para minutos y selecciona el primer caracter.
            focusOnSeconds(): Pone el foco en la entrada para segundos y selecciona el primer caracter.
            startCountDown(): inicia cuenta regresiva.
    '''

    def __init__(self, master, row=0, column=0, display_font={
        'font':'SF Digital Readout', 'size':30, 'type':'normal'}, text_font= {
            'font':'Arial', 'size':10, 'type':'normal'}, textColor='red'):

        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.textColor = textColor
        self.display_font = display_font
        self.text_font = text_font
        self.state = False
        self.tcd = None
        self.stop_beep = None
        self.swapState = lambda x: x==False
        self.config(
            text='temporizador',
            fg=self.textColor,
            bg=self.master['bg'],
            pady=18,
            padx=5,
            bd=2,
            relief='ridge'
            )
        self.grid(row=self.row, column=self.column)
        self.displayMinuts = TWODIGITBRICK(self, 1, 0, textColor=self.textColor, display_font=self.display_font)
        self.separator = Label(self)
        self.separator.config(
            text=':',
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            fg =self.textColor,
            bg = self.master['bg']
            )
        self.separator.grid(row=1, column=1)
        self.displaySeconds = TWODIGITBRICK(self, 1, 2, textColor=self.textColor, display_font=self.display_font)
        self.displayMinuts.bind('<KeyRelease>', self.focusOnMinuts)
        self.displaySeconds.bind('<KeyRelease>', self.focusOnSeconds)

    def focusOnMinuts(self, e):
        if e.keycode == 13:
            self.displaySeconds.focus_set()
            self.displaySeconds.select_range(0, 1)

    def focusOnSeconds(self, e):
        if e.keycode == 13:
            self.displayMinuts.focus_set()
            self.displayMinuts.select_range(0, 1)

    def startStop(self):
        self.state = self.swapState(self.state)

        if self.state:
            self.startCountDown()
        else:
            if self.tcd is not None:
                self.after_cancel(self.tcd)
            if self.stop_beep is not None:
                self.after_cancel(self.stop_beep)


    def reset(self):
        self.displayMinuts.reset()
        self.displaySeconds.reset()
        self.displayMinuts.focus_set()
        self.displayMinuts.icursor(0)
        self.displayMinuts.select_range(0, 1)
    
    def startCountDown(self):
        if self.displayMinuts.get() == '00' and self.displaySeconds.get() == '00':
            pass
        else:
            time.sleep(1)
            self.countDown()

    def countDown(self):
        '''
            cuenta regresiva
        '''
        self.displayMinuts.delete(2, len(self.displayMinuts.get()))
        self.displaySeconds.delete(2, len(self.displaySeconds.get()))
        if self.state:
            if int(self.displaySeconds.get()) > 0:
                self.displaySeconds.displayValue.set(str(int(self.displaySeconds.displayValue.get()) - 1))
                if len(self.displaySeconds.get()) <= 1:
                    self.displaySeconds.displayValue.set('0' + self.displaySeconds.get())
            elif int(self.displaySeconds.get()) == 0:
                self.displaySeconds.displayValue.set('59')

                if int(self.displayMinuts.get()) > 0:
                    self.displayMinuts.displayValue.set(str(int(self.displayMinuts.displayValue.get()) - 1))
                    if len(self.displayMinuts.get()) <= 1:
                        self.displayMinuts.displayValue.set('0' + self.displayMinuts.get())

        if (int(self.displayMinuts.get()) <= 0 and int(self.displaySeconds.get()) <= 0) and self.state:
            self.timeOver()

        elif (int(self.displayMinuts.get()) > 0 or int(self.displaySeconds.get()) > 0) and self.state:
            self.tcd = self.after(1000, self.countDown)

        print(self.displayMinuts.get(), self.displaySeconds.get())

    def timeOver(self):
        winsound.Beep(1500, 500)
        self.stop_beep = self.after(1000, self.timeOver)


if __name__ == '__main__':
    from tkinter import Button
    from utils.twodigitbrick import TWODIGITBRICK
    app = Tk()
    app.config(bg='black')
    testcrono = TIMER(app)
    testcrono.displayMinuts.focus_set()
    testcrono.displayMinuts.select_adjust(1)
    startbutton = Button(app, text='start/stop', command=testcrono.startStop)
    startbutton.grid(row=1, column=0)
    resetbutton = Button(app, text='reiniciar', command=testcrono.reset)
    resetbutton.grid(row=2, column=0)
    app.mainloop()

else:
    from .utils.twodigitbrick import TWODIGITBRICK
