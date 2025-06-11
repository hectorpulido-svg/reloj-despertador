from pygame import mixer
from tkinter import StringVar
import os
<<<<<<< HEAD
=======
cwd = os.getcwd()
>>>>>>> d3281149ec38ae7a0729dc7a12305626118c1d46

class PLAYER:

    def __init__(self):

        mixer.init()
        self.defaultMedia = StringVar()
<<<<<<< HEAD
        self.defaultMedia.set(os.path.abspath(os.curdir) + '\\sound\\4PLAY-Floating.mp3')
        self.mediaPath = StringVar()
        self.mediaName = StringVar()
        self.newMedia = StringVar()
        self.media = None
        self.newMedia.set(self.defaultMedia.get())
        self.mediaPath.set(self.defaultMedia.get())

    def play(self):
        if '.mp3' in self.mediaPath.get():
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
        self.newMedia.set(self.mediaPath.get())
=======
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
>>>>>>> d3281149ec38ae7a0729dc7a12305626118c1d46


if __name__ == '__main__':
    from tkinter import Tk, filedialog, Button
    w = Tk()
    p = PLAYER()

    def load():
<<<<<<< HEAD
        media = filedialog.askopenfile()
        p.newMedia.set(media)
=======
        media = filedialog.askopenfile("r")
        p.newMedia(media)
        # p.mediaPath.set(media)
>>>>>>> d3281149ec38ae7a0729dc7a12305626118c1d46

    b_load = Button(w, text='load', command=load).pack()
    b_play = Button(w, text='play', command=p.play).pack()
    b_stop = Button(w, text='stop', command=p.stop).pack()
    w.mainloop()
else:
    pass