# -*coding: utf-8 -*-
# =======================================================================
#
from tkinter import Tk, Entry, StringVar

class TWODIGITBRICK(Entry):
    '''
        Entry de dos digitos.

        args, kwrds:

            (master: contenedor, row: int, column: int, display_font={}: Tipográfia)

        propiedades:

            defaultValue: string

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
        self.defaultValue = StringVar()
        self.defaultValue.set('00')
        self.config(
            width=self.width,
            font = (self.display_font['font'], self.display_font['size'], self.display_font['type']),
            textvariable=self.defaultValue,
            fg=self.textColor,
            bg=self.master['bg'],
            bd=0,
            justify='left',
            validate = 'key',
            relief='flat',
            insertwidth = self.width / 2
            )
        self.grid(row=self.row, column=self.column)
        command_key = self.register(self._Validate), '%d', '%i', '%S', '%V'
        self.config(validatecommand=command_key)
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

    def _Validate(self, codigo, indice, caracter, validacionTipo):

        indx = int(indice)
        if indx >= 1:
            indx = 0
        self.valid = caracter.isdigit()
        if self.valid and codigo == '1':
            self.icursor(indx)
            self.select_range(indx, indx + 1)
        elif not self.valid and codigo =='1':
            self.bell()
        return self.valid
                
    def reset(self):
        self.delete(0, len(self.get()))
        self.insert(0, '0')
        self.insert(1, '0')

if __name__ == '__main__':
    from tkinter import Button
    app = Tk()
    app.config(bg='black')
    test = TWODIGITBRICK(app, display_font={'font':'Arial', 'size':30, 'type':'normal'})
    def resetTest():
        test.reset()

    btn = Button(app, text='reset', command=resetTest)
    btn.grid(row=1, column=0)
    test.focus_set()
    test.select_adjust(1)
    app.mainloop()
else:
    '''
    modulo
    '''
    pass