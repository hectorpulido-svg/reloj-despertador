#---------------------------------------
# -*-codig: utf-8 -*-
from tkinter import Tk, Frame, LabelFrame
from modulos import CRONO
from modulos import CBUTTON
from modulos.alarmEntry_new import ALARMNEW


# class RUNCRONOASMODULE(Frame):
    
#     def __init__(self, master, row, column):

#         super().__init__()
#         self.row = row
#         self.column = column
#         self.cronoGroup = LabelFrame(self.master, text='cronometro prueba', labelanchor='n')
#         self.cronoGroup.grid(row=self.row, column=self.column)
#         self.crono = CRONO(self.cronoGroup, row=0, column=0, display_font={'font': 'Arial', 'size':30, 'type':'normal'})
#         self.startbutton = CBUTTON(self.master, row=1, column=0, btn_type='grey', Ltext='start', Rtext='stop', command=self.testmethod)

#     def testmethod(self):
#         self.crono.state = self.startbutton.state
#         self.crono.startCountDown()

def runapp():
    # app = Tk()
    # app.config(bg='black')
    # cronotest = RUNCRONOASMODULE(app, row=0, column=0)
    # cronotest.crono.displayMinuts.display.focus_set()
    # cronotest.crono.displayMinuts.display.select_adjust(1)
    app = Tk()
    app.config(bg='black')
    entry = ALARMNEW(app, row=0, column=0, digitsFont={'font':'SF Digital Readout', 'size':30, 'type':'normal'}, textFont= {'font':'Arial', 'size':10, 'type':'normal'}, textColor = 'red')
    entry.displayMinuts.display.focus_set()
    entry.displayMinuts.display.select_adjust(1)
    app.mainloop()



if __name__=='__main__':
    runapp()
