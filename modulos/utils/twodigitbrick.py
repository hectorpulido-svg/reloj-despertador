# -*coding: utf-8 -*-
# =======================================================================
#
from tkinter import Tk, Entry, StringVar
# import winsound

class TWODIGITBRICK(Entry):
    '''
        Entry de dos digitos.

        args, kwrds:

            (master: contenedor, row: int, column: int, display_font={}: Tipográfia)

        propiedades:

            displayValue: string

        metodos:

            update(): actuliza el color del texto y la tipografia
    '''
    def __init__(self, master, row=0, column=0, textColor='white', display_font={}):
        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.textColor = textColor
        self.display_font = display_font
        #******************** TWO DIGIT ENTRY *******************
        self.displayValue = StringVar()
        self.displayValue.set('00')
        self.config(
            width=2,
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            textvariable=self.displayValue,
            fg=self.textColor,
            bg=self.master['bg'],
            bd=0,
            justify='left',
            validate = 'all',
            relief='flat'
            )
        self.grid(row=self.row, column=self.column)
        comando = self.register(self.__Validate), '%d', '%i', '%S', '%s'
        self.config(validatecommand=comando)
    #########################################################
    #             VALIDA LA ENTRADA DE DIGITOS              #
    #########################################################
    # sustituciones de caracter validas(tkinter Entry)
    # %d = tipo de acción (1=insertar, 0=borrar, -1 otros)
    # %i = indice en la cadena para el caracter a insertar/borrar, ó -1
    # %P = valor de la cadena si la edición es permitida
    # %s = valor de la entrada antes de la edición
    # %S = el caracter a ser insertado o borrado si lo hay
    # %v = el tipo de validación asignada
    # %V = el tipo de validación que dispara la llamada
    #      (all, key, focusin, focusout, forced)
    # %W = el nombre del widget

    def __Validate(self, codigo, indice, insertaEste, valorEntrada):
        self.bind('<KeyRelease>', self.testKey)
        indx = int(indice)
        if codigo == '1':
            if indx >= 1:
                indx = 0
        valid = insertaEste.isdigit()
        if valid:
            self.icursor(indx)
            self.select_range(indx, indx + 1)
            print(codigo, indice, insertaEste, valorEntrada)
            self.displayValue.set(self.get())
        else:
            if codigo == '-1':
                pass
            elif codigo == '0':
                self.index(indx - 1)
            else:
                self.bell()
            print(codigo, indice, insertaEste)
                
        return valid

    def testKey(self, e):
        print(e)

    def update(self):
        # self.config(font=(self.display_font['font'], self.display_font['size'], self.display_font['type']), fg=self.textColor)
        self.config(width=2, textvariable=self.displayValue)

    def reset(self):
        for i, c in enumerate(self.get()):
            self.icursor(0)
            self.select_range(0, 1)
            self.insert(0, '0')
            self.delete(2)
        
        self.displayValue.set('00')
        self.update()
        self.icursor(0)
        self.select_range(0, 1)


if __name__ == '__main__':
    from tkinter import Button
    app = Tk()
    app.config(bg='black')
    test = TWODIGITBRICK(app, display_font={'font':'Arial', 'size':30, 'type':'normal'})
    def resetTest():
        test.reset()

    def updateTest():
        test.textColor='green'
        test.display_font={'font':'Castellar', 'size':30, 'type':'normal'}
        test.update()

    btn = Button(app, text='reset', command=resetTest)
    btn1 = Button(app, text='update', command=updateTest)
    btn.grid(row=1, column=0)
    btn1.grid(row=2, column=0)
    test.focus_set()
    test.select_adjust(1)
    app.mainloop()
else:
    '''
    modulo
    '''
    pass