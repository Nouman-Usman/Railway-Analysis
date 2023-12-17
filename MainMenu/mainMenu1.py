from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QMessageBox
from MainMenu import ui_dialog, ui_error
from MainMenu.graph import Graph
from MainMenu.ui_function import UIFunction
from MainMenu.ui_main import Ui_MainWindow
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.name12 = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        applicationName = "Railway Analysis"
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle(
            applicationName)
        UIFunction.labelTitle(self,
                              applicationName)
        UIFunction.initStackTab(self)
        UIFunction.constantFunction(self)
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_booking.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_booking'))
        # self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        self.ui.bn_schedule.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        UIFunction.stackPage(self)
        self.diag = ui_dialog.dialogUi()
        self.error = ui_error.errorUi()
        self.dragPos = self.pos()
        self.load_location_comboboxes()
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.confirm_booking)
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.update_label_amount)
        self.ui.comboBox_TicketType.currentIndexChanged.connect(self.update_label_amount)
        self.ui.comboBox_TicketCount.currentIndexChanged.connect(self.update_label_amount)
        self.ui.start_Location.currentIndexChanged.connect(self.update_label_amount)
        self.ui.end_Location.currentIndexChanged.connect(self.update_label_amount)
        print(self.name12)
        self.ui.User_Name.setText('Nouman')
        pixmap = QPixmap('Images/profile.png')
        self.ui.profilePic.setPixmap(pixmap)
        self.ui.profilePic.setScaledContents(True)

        def moveWindow(event):
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_appname.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def confirm_booking(self):
        if not self.ui.radioButton_5.isChecked():
            self.show_popup("Attention", "Please agree all the terms and conditions to proceed")
            return
        self.update_label_amount()
        print("Booking Confirmed")
        self.show_popup("Congratulations", "You Ticket Has Been Confirmed")
        return

    def show_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def load_location_comboboxes(self):
        locations_df = pd.read_csv("MainMenu/Database/Locations.csv")
        locations = locations_df.iloc[:, 0].tolist()[0:]  # Exclude the header
        self.ui.start_Location.addItems(locations)
        self.ui.end_Location.addItems(locations)

    def update_label_amount(self):
        # Get the selected source and target locations from combo boxes
        source_location = self.ui.start_Location.currentText()
        target_location = self.ui.end_Location.currentText()
        if source_location == target_location:
            self.show_popup("Error", "Start and End Location should be different")
            return
        ticket_type = self.ui.comboBox_TicketType.currentText()
        ticket_count = int(self.ui.comboBox_TicketCount.currentText())
        graph = Graph()
        edges = [
            ('Lahore', 'Karachi', 5),
            ('Lahore', 'Quetta', 4),
            ('Lahore', 'Rawalpindi', 1),
            ('Quetta', 'Karachi', 3),
            ('Quetta', 'Multan', 5),
            ('Lahore', 'Peshawar', 6),
            ('Karachi', 'Peshawar', 8)
        ]
        for edge in edges:
            graph.add_edge(*edge)
        shortest_path = int(graph.dijkstra(source_location, target_location)) * 200 * ticket_count
        if ticket_type == "Standard":
            shortest_path *= 2 * ticket_count
        elif ticket_type == "Premium":
            shortest_path *= 3 * ticket_count
        if shortest_path == "No Path":
            self.show_popup("Error", "No Destination Found")
        else:
            self.ui.label_Amount.setText(str(shortest_path) + ' PKR')

    def dialogexec(self, heading, message, icon, btn1, btn2):
        ui_dialog.dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()


def errorexec(self, heading, icon, btnOk):
    ui_error.errorUi.errorConstrict(self.error, heading, icon, btnOk)
    self.error.exec_()


def build(app, name):
    window1 = MainWindow()
    window1.name12 = name
    window1.show()
