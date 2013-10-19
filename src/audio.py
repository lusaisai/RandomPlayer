# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:53:09 2012

@author: lusaisai

This program will randomly pick songs to play, numbers of songs and search pattern can be provided.
In the backend, a sqlite db is needed, in which there's table called music with only one column full_path.
The sqlite db can be created use script musicDBUpd.sh.
"""

import sqlite3
import subprocess
import os

class RandomAudioPlay(object):
    def __init__( self, db_file, player, song_num=15, search_pattern=('',) ):
        self.db_file = db_file
        self.player = player
        self.song_num = song_num
        self.search_pattern = list(search_pattern)
        self.query = ''
        self.songs = []
      
    def set_query(self):
        query_head = 'select * from music '
        query_foot = ' order by random() limit %s;' % self.song_num
        try:
            if len(self.search_pattern) >= 2:
                self.search_pattern.remove('')
        except ValueError:
            pass
        patterns = list(enumerate(self.search_pattern))
        for pattern in patterns:
            if pattern[0] == 0:
                self.query = query_head + " where full_path like '%%%s%%' " % pattern[1]
            else:
                self.query += " or full_path like '%%%s%%' " % pattern[1]
        self.query += query_foot
        return self
        
        
    def get_songs(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute(self.query)
        self.songs = [cols[0] for cols in cur.fetchall()]
        cur.close()
        return self
        
    def play(self):
        black_hole = open(os.devnull)
        command = self.songs[:]
        command.insert(0, self.player)
        subprocess.Popen( command, stdout=black_hole, stderr=black_hole )


