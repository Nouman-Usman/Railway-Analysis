from ui_InterFace import *
import sys
from Custom_Widgets import *
from PySide2.QtWidgets import QApplication, QMainWindow

import os

class MyMainWindow(QMainWindow):
    def __init__(self,parent = None):
        QmainWindow.__init__(self)
        self.iu = Ui_MainWindow()
        self.iu.setupUi(self)

    ########################################################################
# APPLY JSON STYLESHEET
########################################################################
# self = QMainWindow class
# self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
########################################################################
        self.show()
        self.ui.settBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expand())
        self.ui.HelpBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expand())
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.centralMenuContainer.expand())
        self.ui.HelpBtn.clicked.connect(lambda: self.ui.centralMenuContainer.collapsMenu())

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
