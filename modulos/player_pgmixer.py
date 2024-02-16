from pygame import mixer
from tkinter import StringVar
import os

class PLAYER:

    def __init__(self):

        mixer.init()
        self.defaultMedia = StringVar()
        self.defaultMedia.set(os.path.abspath(os.curdir) + '\\sound\\4PLAY-Floating.mp3')
        self.mediaPath = StringVar()
        self.mediaName = StringVar()
        self.newMedia_name = StringVar()
        self.media = None
        self.newMedia_name.set(self.defaultMedia.get())
        self.mediaPath.set(self.defaultMedia.get())

    def play(self):
        # if self.mediaPath.get():
        mixer.music.play()

    def stop(self):
        mixer.music.stop()
        self.mediaPath.set(self.defaultMedia.get())
        mixer.music.load(self.mediaPath.get())

    def newMedia(self, media):
        self.media = media
        if type(self.media) != type(''):
            self.mediaName.set(self.media.name)
        else:
            self.mediaName.set(self.media.split('/')[-1])
        mixer.music.load(self.media)

    def reset(self):
        self.mediaPath.set(self.defaultMedia.get())
        self.newMedia_name.set(self.mediaPath.get())


if __name__ == '__main__':
    from tkinter import Tk, filedialog, Button
    w = Tk()
    p = PLAYER()

    def load():
        media = filedialog.askopenfile("r")
        p.newMedia(media)
        # p.mediaPath.set(media)

    b_load = Button(w, text='load', command=load).pack()
    b_play = Button(w, text='play', command=p.play).pack()
    b_stop = Button(w, text='stop', command=p.stop).pack()
    w.mainloop()
else:
    pass