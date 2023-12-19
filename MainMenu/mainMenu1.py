from PyQt5.uic.properties import QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from MainMenu import ui_dialog, ui_error
from MainMenu.graph import Graph
from MainMenu.ui_function import UIFunction
from MainMenu.ui_main import Ui_MainWindow
from MainMenu.linkedlist import LinkedList
from MainMenu.Algorithm import merge_sort, quick_sort
import pandas as pd



class MainWindow(QMainWindow):
    def __init__(self, name=None, *args, **kwargs):
        self.name12 = name
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        applicationName = "Railway Analysis"
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle(applicationName)
        UIFunction.labelTitle(self, applicationName)
        UIFunction.initStackTab(self)
        UIFunction.constantFunction(self)
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_booking.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_booking'))
        self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        self.ui.bn_schedule.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        UIFunction.stackPage(self)

        # Load schedule table data
        self.load_schedule_table()
        self.ui.label_search.textChanged.connect(self.search_and_highlight)

        self.load_location_comboboxes()
        # Connect the event to check for the constraint
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.confirm_booking)
        self.ui.pushButton_ConfirmBooking.clicked.connect(self.update_label_amount)
        self.ui.comboBox_TicketType.currentIndexChanged.connect(self.update_label_amount)
        self.ui.comboBox_TicketCount.currentIndexChanged.connect(self.update_label_amount)
        self.ui.start_Location.currentIndexChanged.connect(self.update_label_amount)
        self.ui.end_Location.currentIndexChanged.connect(self.update_label_amount)

        # Connect the sorting function to the combo box change event
        self.ui.comboBox_sort.currentIndexChanged.connect(self.sort_table)
        self.ui.User_Name.setText(self.name12)
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

    def reset_booking_page(self):
        # Reset labels and combo boxes
        self.ui.comboBox_TicketType.setCurrentIndex(0)
        self.ui.comboBox_TicketCount.setCurrentIndex(0)
        self.ui.radioButton_5.setChecked(False)
        self.ui.label_Amount.clear()

    def confirm_booking(self):
        if not self.ui.radioButton_5.isChecked():
            self.show_error_popup("Error", "Please agree all the terms and conditions to proceed")
            return

        self.update_label_amount()
        if self.all_constraints_met():
            self.show_info_popup("Congratulations", "Booking confirmed successfully! Enjoy your journey!")
            self.reset_booking_page()
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(self.ui.page_home))

    def all_constraints_met(self):
        if self.ui.start_Location.currentText() != self.ui.end_Location.currentText():
            if self.ui.radioButton_5.isChecked():
                return True

    def show_error_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def show_info_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def load_location_comboboxes(self):
        locations_df = pd.read_csv("MainMenu/Database/Locations.csv")
        locations = locations_df.iloc[:, 0].tolist()[0:]  # Exclude the header
        self.ui.start_Location.addItems(locations)
        self.ui.end_Location.addItems(locations)

    def load_schedule_table(self):
        schedule_data = pd.read_csv("MainMenu/Database/Train and Time.csv")
        headers = list(schedule_data.columns)
        data = schedule_data.values.tolist()

        # Create a linked list to store the data
        self.schedule_linked_list = LinkedList()

        # Add each row of data as a list to the linked list
        for row in data:
            self.schedule_linked_list.append_list(row)

        # Display the data in the table
        self.display_linked_list_in_table()
        self.ui.table_schedule.setColumnCount(4)
        self.ui.table_schedule.setHorizontalHeaderLabels(["Train Name", "Departure Time", "Seats", "From-To"])
        self.display_linked_list_in_table()

    def display_linked_list_in_table(self):
        # Clear existing table content
        self.ui.table_schedule.setRowCount(0)

        current_node = self.schedule_linked_list.head
        row_position = 0

        # Iterate through the linked list and add data to the table
        while current_node:
            print(current_node.data)  # Add this line for debugging

            self.ui.table_schedule.insertRow(row_position)
            for col_position, data in enumerate(current_node.data):
                item = QTableWidgetItem(str(data))
                self.ui.table_schedule.setItem(row_position, col_position, item)
            current_node = current_node.next
            row_position += 1

    def search_and_highlight(self, text):
        self.clear_table_highlights()
        if text == "":
            return
        current_node = self.schedule_linked_list.head
        row_position = 0
        while current_node:
            for col_position, data in enumerate(current_node.data):
                item_text = str(data)
                item = self.ui.table_schedule.item(row_position, col_position)
                if text.lower() in item_text.lower():
                    item.setBackground(QtGui.QColor(255, 255, 0))
            current_node = current_node.next
            row_position += 1

    def clear_table_highlights(self):
        for row in range(self.ui.table_schedule.rowCount()):
            for col in range(self.ui.table_schedule.columnCount()):
                item = self.ui.table_schedule.item(row, col)
                if item:
                    item.setBackground(QtGui.QColor(0, 255, 255))

    def update_label_amount(self):
        source_location = self.ui.start_Location.currentText()
        target_location = self.ui.end_Location.currentText()

        if source_location == target_location:
            self.show_error_popup("Error", "Start and End Location should be different")
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
            self.show_error_popup("Error", "No Destination Found")
        else:
            self.ui.label_Amount.setText(str(shortest_path) + ' PKR')

    def dialogexec(self, heading, message, icon, btn1, btn2):
        ui_dialog.dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()

    def errorexec(self, heading, icon, btnOk):
        ui_error.errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()

    def sort_table(self):
        sort_option = self.ui.comboBox_sort.currentText()

        if sort_option == "Name":
            # Sort by Name using Merge Sort
            self.sort_table_by_name()
        elif sort_option in ["Time", "Seats"]:
            # Sort by Time or Seats using Quick Sort
            self.sort_table_by_quick_sort()

    def sort_table_by_name(self):
        # Assuming 'data' is a list of lists representing your table data
        data = self.get_table_data()
        col_index = 0  # Assuming you want to sort by the first column
        # Assuming 'table_schedule' is your QTableWidget
        self.sort_table_column(col_index, data, merge_sort)

    def sort_table_by_quick_sort(self):
        # Assuming 'data' is a list of lists representing your table data
        data = self.get_table_data()
        col_index = 1  # Assuming you want to sort by the second column
        # Assuming 'table_schedule' is your QTableWidget
        self.sort_table_column(col_index, data, quick_sort)

    def sort_table_column(self, column, data, sort_algorithm):
        col_index = self.ui.table_schedule.horizontalHeader().visualIndex(column)
        column_data = [row[col_index] for row in data]
        sorted_column_data = sort_algorithm(data, col_index)

        # Assuming 'table_schedule' is your QTableWidget
        self.display_sorted_column(col_index, sorted_column_data)

    def display_sorted_column(self, col_index, sorted_column_data):
        # Assuming 'table_schedule' is your QTableWidget
        for row, row_data in enumerate(sorted_column_data):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.ui.table_schedule.setItem(row, col, item)

    def get_table_data(self):
        # Assuming 'table_schedule' is your QTableWidget
        data = []
        for row in range(self.ui.table_schedule.rowCount()):
            row_data = [self.ui.table_schedule.item(row, col).text() for col in
                        range(self.ui.table_schedule.columnCount())]
            data.append(row_data)
        return data


def build(name):
    # app = QApplication(sys.argv)
    window = MainWindow(name)
    window.show()
    # sys.exit(app.exec_())
