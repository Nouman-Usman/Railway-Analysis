from PySide2 import QtCore, QtGui
from PySide2.QtCore import (QTime, Qt)
from MainMenu.ui_main import Ui_MainWindow
import pandas as pd
from MainMenu.ui_dialog import Ui_Dialog
from MainMenu.ui_error import Ui_Error

from MainMenu.ui_function import *


class dialogUi(QDialog):
    def __init__(self, parent=None):
        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint)
        self.setAttribute(
            QtCore.Qt.WA_TranslucentBackground)
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.d.bn_close.clicked.connect(lambda: self.close())
        self.d.bn_east.clicked.connect(lambda: self.close())
        self.d.bn_west.clicked.connect(lambda: self.close())
        self.dragPos = self.pos()

        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.d.frame_top.mouseMoveEvent = movedialogWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)


class errorUi(QDialog):
    def __init__(self, parent=None):
        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.e.bn_ok.clicked.connect(lambda: self.close())
        self.dragPos = self.pos()

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.e.frame_top.mouseMoveEvent = moveWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE ERRORBOX DURING MOUSE DRAG

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def errorConstrict(self, heading, icon, btnOk):
        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(btnOk)
        pixmap2 = QtGui.QPixmap(icon)
        self.e.lab_icon.setPixmap(pixmap2)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        applicationName = "Railway Analysis"
        self.setWindowTitle(
            applicationName)  # SETS THE APPLICATION NAME IN THE WINDOW TOPBAR                        ---------(C4)
        UIFunction.labelTitle(self,
                              applicationName)  # PASSING THE CODE TO SET THE TITLE TO THE CUSTOME TOPBAR IN OUR UI
        UIFunction.initStackTab(self)
        UIFunction.constantFunction(self)
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_booking.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_booking'))
        self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        self.ui.bn_schedule.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        UIFunction.stackPage(self)
        self.diag = dialogUi()
        self.error = errorUi()
        self.dragPos = self.pos()
        self.load_location_comboboxes()

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_appname.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def load_location_comboboxes(self):
        # Load locations from CSV file
        locations_df = pd.read_csv("Database/Locations.csv")
        locations = locations_df.iloc[:, 0].tolist()[1:]  # Exclude the header

        # Populate start_Location and end_Location comboboxes
        self.ui.start_Location.addItems(locations)
        self.ui.end_Location.addItems(locations)

        # Connect the button press event to check for the constraint
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.check_location_constraint)

    def check_location_constraint(self):
        start_location = self.ui.start_Location.currentText()
        end_location = self.ui.end_Location.currentText()

        # Check if start and end locations are the same
        if start_location == end_location:
            self.errorexec("Error", "icons/bugAssest 47.png", "OK")

    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()

    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # window = MainWindow()
#     # window.show()
#     sys.exit(app.exec_())
