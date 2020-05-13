from tkinter import StringVar

class LEDSS:
    '''
        simula pantalla de led.
    ''' 

    def __init__(self, string=''):
        self.string = StringVar()
        self.string.set(string.rjust(len(string) + 5, chr(32)))
        self.output = StringVar()
        self.output.set(self.string.get())

    def update(self, string):
        self.string.set(string.rjust(len(string) + 5, chr(32)))

    def roll(self):
        outGoingCharacter = self.string.get()[0]
        displayedCharacters = self.string.get()[1:len(self.string.get()) - 1]
        inComingCharacters = self.string.get()[len(self.string.get()) - 1:len(self.string.get())] + outGoingCharacter
        self.string.set(displayedCharacters + inComingCharacters)
        self.output.set(displayedCharacters + inComingCharacters[0])
        return self.output.get()
