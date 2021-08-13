# -*- coding: utf-8 -*-
#!user/bin/env python3
#------------------------------------------------------
# Autor: Hector Miguel Pulido Garcia
# Python 3
# Aplicación: Reloj Despertador Version 1.0
# para windows o linux x64/86 bits 
# usando WINDOWS MEDIA PLAYER o PYGAME.MIXER_MUSIC
#------------------------------------------------------
from tkinter import Tk, PhotoImage, messagebox, StringVar, Frame
from modulos import SYSTEMCLOCK, ALARM, SYSDATE,CBUTTON, FILESELECTOR, PLAYER
import os
import sys

# cd = os.path.sys.path[0]

class ALARMCLOCK(Frame):

    def __init__(self, master, row=0, column=0):
        super().__init__(master)
        self.master = master
        self.row = row
        self.column = column
        self.master.resizable(width=False, height=False)
        self.systemclock = SYSTEMCLOCK(self.master, row=0, column=0,
                            display_font={
                                'font': 'Arial',
                                'size': 30,
                                'type': 'normal'
                                },
                            text_font={
                                'font': 'Arial',
                                'size': 10,
                                'type': 'normal'
                                })
        self.alarm = ALARM(self.master, row=0, column=1,
                            display_font={
                                'font': 'Arial',
                                'size': 30,
                                'type': 'normal'
                                },
                            text_font={
                                'font':'Arial',
                                'size':10,
                                'type':'normal'
                                })
        self.sysdate = SYSDATE(
                self.master, row=1, column=0, columnspan=2,
                display_font={'font': 'Arial', 'size': 15, 'type': 'normal'}
                )
        self.btn_power = CBUTTON(
                self.master, row=2, column=0,
                Ltext='On',
                Rtext='Off',
                command=self.on_off
                )
        self.btn_am_pm = CBUTTON(
            self.master, row=2, column=1,
            Ltext=(lambda x: 'pm' if x == 'am' else 'am')(self.systemclock._meridian.get()),
            Rtext=(lambda x: 'pm' if x == 'pm' else 'am')(self.systemclock._meridian.get()),
            command=self.alarm.am_pm
            )
        self.selector = FILESELECTOR(
                self.master, row=3, column=0, columnspan=2,
                text='Selección', command=self.selection
                )
        self.player = PLAYER()
        self.time_over = False

        self.grid(row=self.row, column=self.column)

    def on_off(self):
        if self.btn_power.state:
            self.alarm.updateTime(None)
            if self.alarm.alarmTime.get() == '00:00':
                messagebox.showinfo(title='Alarma', message='especifique una hora de alarma')
                self.btn_power.onClick('ButtonPress-1')
            else:
                self.alarmOn()
        else:
            self.alarmOff()

    def selection(self):
        '''
            envia al PLAYER la dirección del archivo de sonido seleccionado,
            el PLAYER retorna el nombre del archivo y lo usa como texto del botón.
        '''
        self.player.mediaPath.set(self.selector.newSelectionPath.get())
        self.player.newMedia(self.player.mediaPath.get())
        self.selector.currentSelection.set(self.player.mediaName.get().rjust(len(self.player.mediaName.get()) + 8, chr(32)))
        self.selector.selectorTitle.set(self.player.albumArtist())
        self.selector.updateSelectorTitle()
        self.selector.updateSelectorLabel()

    def alarmOn(self):
        if (self.systemclock.currentTime.get() == self.alarm.alarmTime.get()) and (self.systemclock._meridian.get() == self.alarm._meridian.get()):
            self.time_over = True
        elif ((self.systemclock.currentTime.get() == '12:00') and (self.systemclock._meridian.get() == 'am')):
            self.sysdate.updateDisplay()

        self.checker = self.after(1000, self.alarmOn)
        self.wakeUp()
        
    def alarmOff(self):
        self.player.stop()
        self.time_over = False
        self.after_cancel(self.checker)
        self.alarm.reset()
        self.selector.reset()
        self.player.reset()

    def wakeUp(self):
        self.play = (self.time_over and self.btn_power)
        if self.play:
            self.player.play()

            
def runapp():
    app = Tk()
    cd = os.path.dirname(sys.argv[0])
    icon = os.path.join(cd, 'img\\icon\\TimeAlarmclock.ico')
    i = PhotoImage(icon)
    app.iconbitmap(i)
    app.config(bg='black')
    app.title('Reloj Despertador')
    Despertador = ALARMCLOCK(app)
    Despertador.alarm.displayHours.focus_set()
    Despertador.alarm.displayHours.select_adjust(1)
    Despertador.systemclock.tictac()
    Despertador.sysdate.updateDisplay()
    Despertador.sysdate.ledScreenSimulation()
    Despertador.selector.ledScreenSimulation()
    app.mainloop()


if __name__ == '__main__':
    runapp()