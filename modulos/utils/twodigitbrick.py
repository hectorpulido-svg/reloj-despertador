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
    def __init__(self, master, row=0, column=0, width=2, textColor='white', display_font={}):
        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.width = width
        self.textColor = textColor
        self.display_font = display_font
        #******************** TWO DIGIT ENTRY *******************
        self.displayValue = StringVar()
        self.displayValue.set('00')
        self.config(
            width=self.width,
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            textvariable=self.displayValue,
            fg=self.textColor,
            bg=self.master['bg'],
            bd=0,
            justify='right',
            validate = 'all',
            relief='flat'
            )
        self.grid(row=self.row, column=self.column)
        command_key = self.register(self.__Validate), '%d', '%i', '%S', '%V'
        self.config(validatecommand=command_key)
        self.valid = False
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

    def __Validate(self, codigo, indice, caracter, validacionTipo):
        # if validacionTipo == 'focusin' or validacionTipo == 'focusout':
        #     self.displayValue.set(self.get()[0:2])

        indx = int(indice)
        if codigo == '1':
            if indx >= 1:
                indx = 0

        if self.valid:
            self.focus_displayof().icursor(indx)
            self.focus_displayof().select_range(indx, indx + 1)
            self.focus_displayof().displayValue.set(self.focus_displayof().get())
        else:
            if int(codigo) <= 0:
                pass
            else:
                self.bell()
                
        self.valid = caracter.isdigit()
        return self.valid

    def update(self):
        # self.config(font=(self.display_font['font'], self.display_font['size'], self.display_font['type']), fg=self.textColor)
        self.config(textvariable=self.displayValue)

    def reset(self):
        for i, c in enumerate(self.get()):
            self.focus_displayof().icursor(0)
            self.focus_displayof().select_range(0, 1)
            self.focus_displayof().insert(0, '0')
            self.focus_displayof().delete(2, len(self.focus_displayof().get()))

        self.displayValue.set(self.focus_displayof().get())
        self.focus_displayof().icursor(0)
        self.focus_displayof().select_range(0, 1)


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