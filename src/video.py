# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:37:17 2012

@author: lusaisai

This program will randomly choose and play a video file.
"""
import os
import random
import re
import subprocess
import pickle

class RandomVideoPlay(object):
    def __init__(self, video_dir, data_dir, player):
        self.video_dir = video_dir
        self.player = player
        self.video_suffix = [ 'avi', 'mp4', 'rm', 'rmvb', 'wmv', 'mkv', 'mpg', 'mpeg', 'vob', 'mov' ]
        self.pattern = '.*(' + '|'.join(self.video_suffix) + ')$'
        self.all_videos = { video_dir: {} }
        self.current_video = ''
        self.stats = os.path.realpath( os.path.join( data_dir, 'video_stats.p') )

    def find(self, top_dir):
        os.chdir(top_dir)
        all_files = os.listdir(top_dir)
        for file in all_files:
            full_path = os.path.join(top_dir, file)
            if re.match(self.pattern, file, re.IGNORECASE ):
                self.all_videos[self.video_dir][full_path] = 0
            elif os.path.isdir(full_path):
                self.find(full_path)
            else:
                pass
        return self

    def get_videos(self):
        self.find(self.video_dir)
        return self

    def read_stats(self):
        try:
            stat = pickle.load( open( self.stats, "rb" ) )
            if hasattr( self.all_videos, self.video_dir ):
                self.all_videos[self.video_dir].update( stat[self.video_dir] )

        except IOError:
            pass

    def save_stats(self):
        try:
            stat = pickle.load( open( self.stats, "rb" ) )
            stat.update( self.all_videos )
            pickle.dump( stat, open( self.stats, "wb" ) )
        except IOError:
            pass


    def choose_file(self):
        count = self.all_videos[self.video_dir].values()
        min_count = min(count)
        candidates = [ x for x in self.all_videos[self.video_dir].keys() if self.all_videos[self.video_dir][x] == min_count ]
        return random.choice(candidates)

    # Play the File
    def play(self):
        self.read_stats()
        video = self.choose_file()
        self.current_video = video
        command = [ self.player, video ]
        black_hole = open(os.devnull)
        subprocess.Popen( command, stdout = black_hole, stderr = black_hole )
        self.all_videos[self.video_dir][video] += 1
        self.save_stats()

