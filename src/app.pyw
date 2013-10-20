import playerui
from PyQt4 import QtGui
import sys
import os
import ctypes


app_id = 'localhost.RandomPlayer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
app = QtGui.QApplication(sys.argv)
app.setWindowIcon( QtGui.QIcon( os.path.join( playerui.DATA_DIR, 'app.ico' ) ) )
myui = playerui.MyUI()
myui.show()
app.exec_()
