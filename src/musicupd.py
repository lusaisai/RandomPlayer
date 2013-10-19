# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:45:37 2012

@author: lusaisai
"""

import os
import re
import sqlite3

class MusicDBUpd:
    audio_suffix = ( 'ape', 'mp3', 'flac', 'm4a' )
    audio_pattern = '.*(' + '|'.join(audio_suffix) + ')$'

    def __init__(self, data_dir, music_dir):
        self.db_file = os.path.realpath( os.path.join( data_dir, 'musics.db') )
        self.music_dir = music_dir
        self.conn = None #initialized in another method
        self.db_init()

    def db_init(self):
        try:
            os.remove(self.db_file)
        except WindowsError:
            pass
        self.conn = sqlite3.connect(self.db_file)
        self.conn.execute('create table music(full_path text);')

    def search_file(self, directory):
        dirs = os.listdir(directory)
        for filename in dirs:
            full_path = os.path.join( directory, filename)
            if os.path.isdir(full_path):
                self.search_file( full_path )
            else:
                if re.match(MusicDBUpd.audio_pattern, full_path, re.IGNORECASE ):
                    self.conn.execute( 'insert into music values (?)', (full_path,) )

    def db_upd(self):
        self.search_file(self.music_dir)
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    m = MusicDBUpd(os.path.join( os.path.realpath(__file__), '..', '..', 'data' ), r'H:\Music')
    m.db_upd()
