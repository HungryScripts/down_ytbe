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

#LINK: https://youtube.com/playlist?list=PLTTWYoZ7oot_6RURFsirMrvaMulB7t8sO&si=ZblqTi-n0GmZ82pR
while True:
    print("")
    what_download = int(input("1 video comun: 2 playlist: "))
    if what_download == 1:
        print("")
        l = input("coloca el enlace $")
        yt = YouTube(l,on_progress_callback=on_progress)
        yt.streams.filter(only_audio=True).first()
        yt.streams.filter(file_extension='mp4').first()
        #yt.streams.filter(res='360p').first()
        down = yt.streams.order_by('abr').desc().first()
        create_and_gesting_DB(down.default_filename)
        print("descargando....%s" % down.default_filename)
        down.download("C:/Users/FileType/Downloads/programacion/PROYECTOS Y EJERCICIOS DE PYTHON/automatizaciones/yt_downV1")

    else:
        l = input("coloca el enlace l$")
        playlist = Playlist(l)
        for i in playlist.video_urls:
            yt = YouTube(i)
            down = yt.streams.order_by('abr').desc().first()
            print("descargando....%s" % down.default_filename)
            down.download("C:/Users/FileType/Downloads/programacion/PROYECTOS Y EJERCICIOS DE PYTHON/automatizaciones/yt_downV1")
