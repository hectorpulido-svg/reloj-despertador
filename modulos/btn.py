# -*coding: utf-8 -*-
from tkinter import Frame, LabelFrame, Label, PhotoImage, StringVar

class CBUTTON(Frame):
    '''
        Widget de clase Boton con texto en sus extremos depende de imagenes externas
    '''

    def __init__(self, master, row, column, btn_type='sliderButtons', Ltext='true', Rtext='false', command=None):
        super().__init__()
        self.row = row
        self.column = column
        self.LT = Ltext
        self.RT = Rtext
        self.Rtext = StringVar()
        self.Ltext = StringVar()
        self.command = command
        self.state = False
        self.buttonGroup = LabelFrame(master)
        self.buttonGroup.config(bg=master['bg'], padx=5, pady=5)
        self.buttonGroup.grid(row=self.row, column=self.column)
        self.btn_types = {"sliderButtons":"sliderButtons", "red":"red", 'grey': 'grey', 'clasicbuttons': 'clasicbuttons'}
        self.btn_type = self.btn_types[btn_type]
        self.imagePath = StringVar()
        self.imagePath.set('.\\img\\' + self.btn_type + '\\BTN_OFF.png')
        self.button = Label(self.buttonGroup)
        self.button.config(cursor='hand2', bg=master['bg'])
        self.button.bind('<Button-1>', self.onClick)
        self.button.bind('<ButtonRelease-1>', self.onRelease)
        self.button.grid(row=1, column=1)
        self.leftTextlabel = Label(self.buttonGroup)
        self.leftTextlabel.config(bg=master['bg'], fg='white')
        self.leftTextlabel.grid(row=1, column=0)
        self.rightTextlabel = Label(self.buttonGroup)
        self.rightTextlabel.config(bg=master['bg'], fg='white')
        self.rightTextlabel.grid(row=1, column=2)
        self.updatebutton()
        self.swapState = (lambda x: (x==False))
        self.swapImage = (lambda x: ('.\\img\\' + self.btn_type + '\\BTN_OFF.png') if x else ('.\\img\\' + self.btn_type + '\\BTN_ON.png'))

    def onClick(self, event):
        '''
            actualiza el estado del boton
        '''
        # if self.state:
        #     self.state = False
        #     self.imagePath.set('.\\img\\' + self.btn_type + '\\BTN_OFF.png')
        # else:
        #     self.state = True
        #     self.imagePath.set('.\\img\\' + self.btn_type + '\\BTN_ON.png')
        self.imagePath.set((self.swapImage)(self.state))
        self.state = self.swapState(self.state)

        self.updatebutton()
        # self.button.bind('<ButtonRelease-1>', self.onRelease)

    def onRelease(self, event):
        '''
            ejecuta la acción
            dada por la instancia de clase
            en el parametro command
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
        
    test_btn = CBUTTON(app, row=0, column=0, command=None)
    test_btn.grid(columnspan=2)
    app.mainloop()

else:
    '''
        modulo btn.py
    '''
    pass