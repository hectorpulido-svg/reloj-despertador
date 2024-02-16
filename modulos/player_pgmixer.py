from pygame import mixer
from tkinter import StringVar
import os
cwd = os.getcwd()

class PLAYER:

    def __init__(self):

        mixer.init()
        self.defaultMedia = StringVar()
        self.defaultMedia.set(os.path.join(cwd + os.sep + 'sound' + os.sep, '4PLAY-Floating.mp3'))

        self.mediaPath = StringVar()
        self.mediaPath.set(self.defaultMedia.get())

        self.mediaName = StringVar()
        self.mediaName.set(self.defaultMedia.get())

        self.newMedia_name = StringVar()
        self.newMedia_name.set(self.defaultMedia.get())

    def play(self):
        try:
            mixer.music.play()
        except:
            self.load(self.defaultMedia.get())
            mixer.music.play()


    def stop(self):
        mixer.music.stop()

    def newMedia(self, media=None):
        if media is None:
            media = self.defaultMedia.get()
        else:
            if type(media) != type(''):
                self.mediaName.set(media)
            else:
                self.mediaName.set(media.split('/')[-1])

        self.load(media)

    def load(self, media):
        mixer.music.load(media)

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