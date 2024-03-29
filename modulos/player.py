# -*coding: utf-8 -*-

from tkinter import Button, StringVar
from numpy import empty
from win32com import client
import os
cwd = os.getcwd()

class PLAYER:
    '''
        WINDOWS MEDIA PLAYER COM OBJECT
    '''
    def __init__(self):
        self.player = client.Dispatch('WMPlayer.OCX')
        # self.player = client.gencache.EnsureDispatch('WMPlayer.OCX')
        self.defaultMedia = StringVar()
        self.defaultMedia.set(os.path.join(cwd + os.sep + 'sound' + os.sep, '4PLAY-Floating.mp3'))
        print(cwd)
        self.mediaPath = StringVar()
        self.mediaPath.set(self.defaultMedia.get())

        self.mediaName = StringVar()
        self.newMedia_name = StringVar()
        self.newMedia_name.set(self.mediaPath.get())

    def play(self):
        if len(self.player.currentPlayList) == 0:
            self.mediaName.set("")
            self.player.currentPlaylist.insertItem(0, self.player.newMedia(self.mediaPath.get()))
            self.mediaName.set(self.player.newMedia(self.mediaPath.get()).getItemInfo('Title'))
        
        self.player.controls.play()

    def status(self):
        return self.player.status()

    def currentMarker(self):
        return self.player.controls.currentMarker

    def currentPosition(self):
        return self.player.controls.currentPosition

    def currentPositionString(self):
        return self.player.controls.currentPositionString

    def duration(self):
        return self.player.currentPlaylist.Item(0).duration

    def durationString(self):
        return self.player.currentPlaylist.Item(0).durationString

    def stop(self):
        self.player.controls.stop()

    def albumArtist(self):
        return self.player.newMedia(self.mediaPath.get()).getItemInfo('WM/AlbumArtist')

    def newMedia(self, media):
        self.mediaName.set("")
        self.player.currentPlaylist.insertItem(0, self.player.newMedia(media))
        self.mediaName.set(self.player.newMedia(media).getItemInfo('Title'))
        try:
            self.player.currentPlaylist.removeItem(self.player.currentPlaylist.Item(1))
        except:
            pass

    def reset(self):
        self.mediaPath.set(self.defaultMedia.get())
        self.newMedia(self.mediaPath.get())

    def launchWMP(self, mediaTest):
        '''
            este metodo solo se utiliza
            para probar la instancia del
            windows media player
        '''

        print('Title :' + self.player.newMedia(mediaTest).getItemInfo('Title'))
        print('AlbumArtist :' + self.player.newMedia(mediaTest).getItemInfo('WM/AlbumArtist'))
        print('Album Title :' + self.player.newMedia(mediaTest).getItemInfo('WM/AlbumTitle'))
        print('Album cover URL :' + self.player.newMedia(mediaTest).getItemInfo('WM/AlbumCoverURL'))
        try:
            print('Album cover URL :' + self.player.currentPlaylist.Item(0).getItemInfo('WM/AlbumCoverURL'))
            print('Album ID :' + self.player.newMedia(mediaTest).getItemInfo('AlbumID'))
        except:
            pass


        self.newMedia_name.set(mediaTest)
        self.player.openPlayer(mediaTest)

    def imgURL(self):
        return self.player.newMedia(self.mediaPath.get()).getItemInfo('WM/AlbumCoverURL')


if __name__ == '__main__':
    '''
        una muestra del Objeto WMPlayer
    '''
    from tkinter import Tk, Button
    from slct_file import FILESELECTOR

    app = Tk()
    player = PLAYER()

    def play():
        print(player.mediaPath.get())
        player.launchWMP(player.mediaPath.get())

    def test():
        player.mediaPath.set(selector.newSelectionPath.get())
        print(player.mediaPath.get())
        player.launchWMP(selector.newSelectionPath.get())
        selector.selectorTitle.set(player.albumArtist())
        selector.currentSelection.set(player.mediaName.get())
        selector.updateSelectorTitle()
        selector.updateSelectorLabel()

    btn = Button(app, text="play default", command=play).grid(column=0, row=0)
    selector = FILESELECTOR(app, 1, 0, 2, 'PRUEBA DE WMPlayer', command=test)
    selector.ledScreenSimulation()
    app.mainloop()
else:
    '''
        modulo : player.py
    '''
    pass