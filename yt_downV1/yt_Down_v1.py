#!/usr/bin/insert python3

import sqlite3 as sql
from pytube import YouTube, Playlist
from pytube.cli import on_progress


def create_and_gesting_DB(dates):
    DB = sql.connect("REGISTRO_DE_NOMBRES.db")
    DB.commit()
    DB.close()
    if dates == True:
        print("pass")

while True:
    print("")
    what_download = int(input("1 video comun: 2 playlist: "))
    if what_download == 1:
        print("")
        l = input("coloca el enlace $")
        yt = YouTube(l,on_progress_callback=on_progress)
        yt.streams.filter(only_audio=True).first()
        yt.streams.filter(file_extension='mp4').first()
        down = yt.streams.order_by('abr').desc().first()
        create_and_gesting_DB(down.default_filename)
        print("descargando....%s" % down.default_filename)
        down.download("COLOCA AQUI EN DONDE QUIERES QUE SE DESCARGUE EL ARCHIVO")

    else:
        l = input("coloca el enlace de la playlist $")
        playlist = Playlist(l)
        for i in playlist.video_urls:
            yt = YouTube(i)
            down = yt.streams.order_by('abr').desc().first()
            print("descargando....%s" % down.default_filename)
            down.download("COLOCA AQUI EN DONDE QUIERES QUE SE DESCARGUE EL ARCHIVO")
