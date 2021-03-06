# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 22:43:28 2012

@author: lusaisai
"""

import os
import pickle

from PyQt4 import QtCore, QtGui

import audio
import video
import mainwindow
import configwindow
import musicupd


APP_DIR = os.path.join( os.path.realpath(__file__), '..', '..' )
DATA_DIR = os.path.join( APP_DIR, 'data' )
CFG_FILE = os.path.join( DATA_DIR, 'app.cfg' )
DB_FILE = os.path.join( DATA_DIR, 'musics.db' )

class ConfigUI(QtGui.QDialog):
    """
    This is a pop-up config window to setup the music and video players and directories
    """
    def __init__(self, parent=None):
        super(ConfigUI, self).__init__(parent)
        self.ui = configwindow.Ui_Dialog()
        self.ui.setupUi(self)
        self.load_cfg()

        self.connect(self.ui.set_music_player, QtCore.SIGNAL("clicked()"), self.set_music_player)
        self.connect(self.ui.set_music_dir, QtCore.SIGNAL("clicked()"), self.set_music_dir)
        self.connect(self.ui.set_video_player, QtCore.SIGNAL("clicked()"), self.set_video_player)
        self.connect(self.ui.set_video_dir, QtCore.SIGNAL("clicked()"), self.set_video_dir)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.save_cfg)

    def load_cfg(self):
        configs = { 'music_player': '', 'music_dir': '', 'video_player': '', 'video_dir': '' }
        try:
            file_configs = pickle.load( open( CFG_FILE, "rb" ) )
            configs.update(file_configs)
        except IOError:
            pass
        self.ui.music_player.setText(configs['music_player'])
        self.ui.music_dir.setText(configs['music_dir'])
        self.ui.video_player.setText(configs['video_player'])
        self.ui.video_dir.setText(configs['video_dir'])


    def save_cfg(self):
        configs = dict( music_player=self.ui.music_player.text(),
                        music_dir=self.ui.music_dir.text(),
                        video_player=self.ui.video_player.text(),
                        video_dir=self.ui.video_dir.text()
                      )
        pickle.dump( configs, open( CFG_FILE, "wb" ) )

    def set_music_player(self):
        player = QtGui.QFileDialog.getOpenFileName()
        self.ui.music_player.setText(player)

    def set_music_dir(self):
        music_dir = QtGui.QFileDialog.getExistingDirectory()
        self.ui.music_dir.setText(music_dir)

    def set_video_player(self):
        player = QtGui.QFileDialog.getOpenFileName()
        self.ui.video_player.setText(player)

    def set_video_dir(self):
        music_dir = QtGui.QFileDialog.getExistingDirectory()
        self.ui.video_dir.setText(music_dir)




class MyUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(MyUI, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionConfig.setIcon( QtGui.QIcon( os.path.join( DATA_DIR, 'settings.ico' ) ) )
        self.ui.action_db_update.setIcon( QtGui.QIcon( os.path.join( DATA_DIR, 'db.ico' ) ) )
        self.connect(self.ui.songPlay, QtCore.SIGNAL("clicked()"), self.call_audio)
        self.connect(self.ui.videoPlay, QtCore.SIGNAL("clicked()"), self.call_video)
        self.connect(self.ui.actionConfig, QtCore.SIGNAL("triggered()"), self.call_config)
        self.connect(self.ui.action_db_update, QtCore.SIGNAL("triggered()"), self.call_db_upd)

    def read_cfg(self):
        try:
            return pickle.load( open( CFG_FILE, "rb" ) )
        except IOError:
            return {}


    def call_config(self):
        config = ConfigUI(self)
        config.show()

    def call_audio(self):
        configs = self.read_cfg()
        music_player = audio.RandomAudioPlay(DB_FILE, configs['music_player'])
        music_player.song_num = int(self.ui.songNum.text())
        music_player.search_pattern = self.ui.songPattern.text().split(" ")
        music_player.set_query().get_songs().play()
    
    def call_video(self):
        configs = self.read_cfg()
        video_player = video.RandomVideoPlay(configs['video_dir'], DATA_DIR, configs['video_player'])
        video_player.get_videos().play()
        self.ui.statusbar.showMessage("Now playing %s ..." % video_player.current_video)

    def call_db_upd(self):
        configs = self.read_cfg()
        self.ui.statusbar.showMessage("Updating Music Database ...")
        m = musicupd.MusicDBUpd(DATA_DIR, configs['music_dir'])
        m.db_upd()
        self.ui.statusbar.showMessage("Completed!")


