import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from MainMenu import ui_dialog, ui_error
from MainMenu.graph import Graph
from MainMenu.ui_function import UIFunction
from MainMenu.ui_main import Ui_MainWindow
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        applicationName = "Railway Analysis"
        self.setGeometry(100, 100, 1000, 600)
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
        self.diag = ui_dialog.dialogUi()
        self.error = ui_error.errorUi()
        self.dragPos = self.pos()

        self.load_location_comboboxes()
        # Connect the event to check for the constraint
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.confirm_booking)
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.update_label_amount)
        self.ui.comboBox_TicketType.currentIndexChanged.connect(self.update_label_amount)
        self.ui.comboBox_TicketCount.currentIndexChanged.connect(self.update_label_amount)
        self.ui.start_Location.currentIndexChanged.connect(self.update_label_amount)
        self.ui.end_Location.currentIndexChanged.connect(self.update_label_amount)

        # Connect the click event of label_Train to open the Train Selection window
        # self.ui.label_Train.mousePressEvent = self.openTrainSelection

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE: WE CHOOSE THE TOPMOST FRAME WHERE THE APPLICATION NAME IS PRESENT AS THE AREA TO MOVE THE WINDOW.
        self.ui.frame_appname.mouseMoveEvent = moveWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #############################################################

    def confirm_booking(self):
        # Check if the "radioButton_5" is checked
        if not self.ui.radioButton_5.isChecked():
            # If not checked, show a pop-up message
            self.show_popup("Error", "Please agree all the terms and conditions to proceed")
            return

        # Rest of your confirm booking logic goes here
        self.update_label_amount()

    def show_popup(self, title, message):
        # Function to show a pop-up message
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def load_location_comboboxes(self):
        # Load locations from CSV file
        locations_df = pd.read_csv("MainMenu/Database/Locations.csv")
        locations = locations_df.iloc[:, 0].tolist()[0:]  # Exclude the header

        # Populate start_Location and end_Location comboboxes
        self.ui.start_Location.addItems(locations)
        self.ui.end_Location.addItems(locations)

    def update_label_amount(self):
        # Get the selected source and target locations from combo boxes
        source_location = self.ui.start_Location.currentText()
        target_location = self.ui.end_Location.currentText()

        # Check if source and target locations are different
        if source_location == target_location:
            self.show_popup("Error", "Start and End Location should be different")
            return

        # Get the selected ticket type from the comboBox_TicketType
        ticket_type = self.ui.comboBox_TicketType.currentText()
        ticket_count = int(self.ui.comboBox_TicketCount.currentText())

        graph = Graph()

        # Add edges to the graph
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

        # Find the shortest path using Dijkstra's algorithm
        shortest_path = int(graph.dijkstra(source_location, target_location)) * 200 * ticket_count

        # Check the selected ticket type and apply the corresponding multiplier
        if ticket_type == "Standard":
            shortest_path *= 2 * ticket_count
        elif ticket_type == "Premium":
            shortest_path *= 3 * ticket_count

        # Update label_Amount with the minimum weight of the path
        if shortest_path == "No Path":
            self.show_popup("Error", "No Destination Found")
        else:
            self.ui.label_Amount.setText(str(shortest_path) + ' PKR')

    # -----> FUNCTION WHICH OPENS THE DIALOG AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION dialogexec() WITH ALL THE PARAMETER
    # NOW WHENEVER YOU WANT A DIALOG BOX TO APPEAR IN THE APP LIKE IN PRESS OF CLODE BUTTON, THIS CAN BE DONE BY CALLING THIS FUNCTION.        ----------(C11)
    # IT TAKES DIALOG OBJECT(INITIALISED EARLIER), HEADER NAME OF DIALOG BOX, MESSAGE TO BE DISPLAYED, ICON, BUTTON NAMES.
    # THIS CODE EXECUTES THE DIALOGBOX AND SO WE CAN SEE THE DIALOG BOX IN THE SCREEN.
    # DURING THE APPEARENCE OF THIS WINDOW, YOU CANNOT USE THE MAINWINDOW, YOU SHPULD EITHER PRESS ANY ONE OFT HE PROVIDED BUTTONS
    # OR JUST CLODE THE DIALOG BOX.
    def dialogexec(self, heading, message, icon, btn1, btn2):
        ui_dialog.dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()


#############################################################

# -----> FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION errorexec() WITH ALL THE PARAMETER
# SAME AS COMMEND (C11), EXCEPT THIS IS FOR THE ERROR BOX.
def errorexec(self, heading, icon, btnOk):
    ui_error.errorUi.errorConstrict(self.error, heading, icon, btnOk)
    self.error.exec_()
##############################################################


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

def build(app):
    window1 = MainWindow()
    window1.show()
