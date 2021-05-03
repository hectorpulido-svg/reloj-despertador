# -*coding: utf-8 -*-
# =======================================================================
#
from tkinter import Tk, LabelFrame, Label, StringVar
import winsound
import time


class CRONO(LabelFrame):
    '''
        Cronometro con entradas para minutos y segundos.

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
        self.minuts = StringVar()
        self.seconds = StringVar()
        self.minuts.set('00')
        self.seconds.set('00')
        self.textColor = textColor
        self.display_font = display_font
        self.text_font = text_font
        self.state = False
        self.swapState = lambda x: x==False
        self.config(
            text='cronometro',
            labelanchor='n',
            fg='white',
            bg=self.master['bg'],
            padx=15,
            font = self.text_font
            )
        self.grid(row=self.row, column=self.column)
        self.displayMinuts = TWODIGITBRICK(self, 0, 0, textColor=self.textColor, display_font=self.display_font)
        self.separator = Label(self)
        self.separator.config(
            text=':',
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            fg =self.textColor,
            bg = self.master['bg']
            )
        self.separator.grid(row=0, column=1)
        self.displaySeconds = TWODIGITBRICK(self, 0, 2, textColor=self.textColor, display_font=self.display_font)
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
            self.after_cancel(self.tcd)


    def reset(self):
        self.displaySeconds.focus_set()
        self.displaySeconds.reset()
        self.displayMinuts.focus_set()
        self.displayMinuts.reset()
    
    def startCountDown(self):
        if self.displayMinuts.get() == '00' and self.displaySeconds.get() == '00':
            pass
        else:
            self.minuts.set(self.displayMinuts.get())
            self.seconds.set(self.displaySeconds.get())
            time.sleep(1)
            self.countDown()

    def countDown(self):
        '''
            cuenta regresiva
        '''
        
        if (int(self.displayMinuts.get()) > 0 or int(self.displaySeconds.get()) > 0) and self.state == False:
            pass
        else:
            if int(self.seconds.get()) > 0:
                self.seconds.set(int(self.seconds.get()) - 1)
                if len(self.seconds.get()) <= 1:
                    self.seconds.set('0' + self.seconds.get()[0])

            elif int(self.displayMinuts.get()) > 0 and int(self.displaySeconds.get()) <= 0:
                self.minuts.set(int(self.minuts.get()) - 1)
                self.seconds.set('59')
                if len(self.minuts.get()) <= 1:
                    self.minuts.set('0' + self.minuts.get()[0])


        if (int(self.displayMinuts.get()) <= 0 and int(self.displaySeconds.get()) <= 0) and self.state == True:
            self.timeOver()

        elif (int(self.displayMinuts.get()) > 0 or int(self.displaySeconds.get()) > 0) and self.state == True:
            self.tcd = self.after(1000, self.countDown)

        self.displaySeconds.displayValue.set(self.seconds.get())
        self.displaySeconds.update()
        self.displayMinuts.displayValue.set(self.minuts.get())
        self.displayMinuts.update()
        print(self.displayMinuts.get(), self.displaySeconds.get())

    def timeOver(self):
        if (int(self.displayMinuts.get()) <= 0 and int(self.displaySeconds.get()) <= 0) and self.state == False:
            pass
        else:
            winsound.Beep(1500, 500)
            self.after(1000, self.timeOver)


if __name__ == '__main__':
    from tkinter import Button
    # from btn import CBUTTON
    from utils.twodigitbrick import TWODIGITBRICK
    app = Tk()
    app.config(bg='black')
    testcrono = CRONO(app)
    testcrono.displayMinuts.focus_set()
    testcrono.displayMinuts.select_adjust(1)
    # testbutton = CBUTTON(app, row=1, column=0, Ltext='start', Rtext='stop', command=testcrono.startStop)
    startbutton = Button(app, text='start/stop', command=testcrono.startStop())
    startbutton.grid(row=1, column=0)
    resetbutton = Button(app, text='reiniciar', command=testcrono.reset)
    resetbutton.grid(row=2, column=0)
    app.mainloop()

else:
    from .utils.twodigitbrick import TWODIGITBRICK
