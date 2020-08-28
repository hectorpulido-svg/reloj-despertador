# -*coding: utf-8 -*-
from tkinter import LabelFrame, Label, PhotoImage, StringVar
import os
import sys

class CBUTTON(LabelFrame):
    '''
        Widget de clase Boton con texto en sus extremos depende de imagenes externas
    '''

    def __init__(self, master, row, column, Ltext='true', Rtext='false', command=None):
        super().__init__(master)
        self.row = row
        self.column = column
        self.LT = Ltext
        self.RT = Rtext
        self.Rtext = StringVar()
        self.Ltext = StringVar()
        self.command = command
        self.state = False
        self.config(bg=master['bg'], padx=2, pady=5)
        self.grid(row=self.row, column=self.column)
        self.imagePath = StringVar()
        self.imagePath.set(btnoffimg)
        self.button = Label(self)
        self.button.config(cursor='hand2', bg=master['bg'])
        self.button.bind('<Button-1>', self.onClick)
        self.button.bind('<ButtonRelease-1>', self.onRelease)
        self.button.grid(row=1, column=1)
        self.leftTextlabel = Label(self)
        self.leftTextlabel.config(bg=master['bg'], fg='white')
        self.leftTextlabel.grid(row=1, column=0)
        self.rightTextlabel = Label(self)
        self.rightTextlabel.config(bg=master['bg'], fg='white')
        self.rightTextlabel.grid(row=1, column=2)
        self.updatebutton()
        self.swapState = (lambda x: (x==False))
        self.swapImage = (lambda x: (btnoffimg) if x else (btnonimg))

    def onClick(self, event):
        '''
            actualiza el estado del boton
        '''
        self.imagePath.set((self.swapImage)(self.state))
        self.state = self.swapState(self.state)

        self.updatebutton()

    def onRelease(self, event):
        '''
            ejecuta la acción
            dada por la instancia de clase
            en el parametro command al soltar el click
        '''
        if self.command is not None:
            self.command()

    def updatebutton(self):
        '''
            actualiza la imagen del boton
        '''
        self.Ltext.set(self.LT)
        self.Rtext.set(self.RT)
        self.rightTextlabel.config(textvariable=self.Rtext)
        self.leftTextlabel.config(textvariable=self.Ltext)
        self.btn_image = PhotoImage(file = self.imagePath.get())
        self.button.config(image=self.btn_image)

if __name__ == '__main__':
    '''
        **********************************************************
               Aquí se implementa una muestra del objeto
        **********************************************************
    '''
    from tkinter import Tk
    app = Tk()
    app.config(bg='black')
    cd = os.curdir
    btnoffimg = cd + '\\img\\grey\\BTN_OFF.png'
    btnonimg = cd + '\\img\\grey\\BTN_ON.png'
    test_btn = CBUTTON(app, row=0, column=0, command=None)
    test_btn.grid(columnspan=2)
    app.mainloop()

else:
    '''
        modulo btn.py
    '''
    cd = os.path.dirname(sys.argv[0])
    btnoffimg = os.path.join(cd, 'img\\grey\\BTN_OFF.png')
    btnonimg = os.path.join(cd, 'img\\grey\\BTN_ON.png')
    # pass