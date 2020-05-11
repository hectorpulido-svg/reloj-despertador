# -*coding: utf-8 -*-

from tkinter import Button, LabelFrame, StringVar, filedialog
import threading


class FILESELECTOR:
    '''
        Widget de clase Button que abre un filedialog y permite al usuario seleccionar un archivo.
        El nombre de archivo es utilizado como texto del botón.

                NOTA:
                    en este caso el filedilog esta configurado
                    para archivos con extención .mp3 | .wav | .wma

    '''
    def __init__(self, master, row, column, columnspan, text, command=None):
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.text = text
        self.command = command
        self.currentSelection = StringVar() # la dirección del archivo de sonido(file full path)
        self.currentSelection.set('  select sound/mp3')
        self.newSelectionPath = StringVar()
        self.newSelectionPath.set('')
        self.selectorTitle = StringVar()
        self.selectorTitle.set(self.text)
        self.currentSelectionName = StringVar() # el nombre del archivo de sonido sin extensión(file name)
        self.currentSelectionName.set(self.currentSelection.get())
        self.frame = LabelFrame(master, text=self.selectorTitle.get(), labelanchor='n')
        self.frame.grid(row=self.row, column=self.column, columnspan=self.columnspan)
        self.frame.config(bg='black', fg='white', padx=len(self.currentSelection.get()))
        self.btn = Button(self.frame, textvariable=self.currentSelection, width=14, command=self.fld)
        self.btn.grid(row=0, column=0, ipadx=len(self.currentSelection.get()))
        self.btn.config(bg='red', fg='white')
        self.ledSS = ledSS.LEDSS(string=self.currentSelection.get())

    def fld(self):
        '''
            abre la ventana de dialogo para
            permitir la selección de 
            archivos en este caso de sonido mp3, wav, wma.
        '''
        ftypes = [("mp3, wav, wma files","*.mp3 *.wav *.wma"),("all files","*.*")]
        dlg = filedialog.Open(filetypes=ftypes)
        phfl = dlg.show()      
        if phfl != '':
            self.newSelectionPath.set(phfl)
            if self.command is not None:
                self.command()

    def ledScreenSimulation(self):
        '''
            usa el nombre del archivo seleccionado como
            texto para el botón y aplica una animación.
        '''
        self.currentSelection.set(self.ledSS.roll())
        self.btn.config(textvariable=self.currentSelection)
        self.btn.after(round(3000 / len(self.currentSelection.get())), self.ledScreenSimulation)
    
    def updateSelectorTitle(self):
        self.frame.config(text=self.selectorTitle.get())

    def updateSelectorLabel(self):
        self.ledSS.update(self.currentSelection.get())

    def reset(self):
        self.selectorTitle.set('Selección')
        self.currentSelection.set('  select sound/mp3')
        self.updateSelectorTitle()
        self.updateSelectorLabel()
        
if __name__ == '__main__':
    '''
        una muestra del Objeto
    '''
    from tkinter import Tk
    from utils import ledSS
    app = Tk()

    def test():
        selector.currentSelectionName.set(selector.newSelectionPath.get())
        selector.ledSS.update(selector.currentSelectionName.get())

    selector = FILESELECTOR(app, 0, 0, 2, 'PRUEBA DE FILEDIALOG', command=test)
    selector.ledScreenSimulation()
    app.mainloop()

else:
    '''
        modulo slct_file.py
    '''
    from .utils import ledSS