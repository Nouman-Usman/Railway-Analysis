import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide2.QtCore import QTimer

from ui_stack import Ui_MainWindow
import random


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.LoadTrains()
        self.loadfeeds()  # Call the loadfeeds function
        self.LoadWghts(self.tableWidget, [2, 3])

        self.update_label_timer = QTimer(self)
        self.update_label_timer.timeout.connect(self.updateLabel)
        self.update_label_timer.start(45000)  # Start the timer for every 45 seconds
        self.closeEvent = self.saveData

        self.sideMenuButton_2.clicked.connect(self.sideMenuChange)
        self.statsBut.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.statsBut.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.addTrainBut.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.addTrainBut.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
        self.feedbackBut.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.feedbackBut.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        print("Called the functions")
        self.viewMore.clicked.connect(self.addTrainToCSV)

    def LoadTrains(self):
        file_path = 'MainMenu/Database/TAT.csv'
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.tableWidget.setRowCount(len(lines))
                self.tableWidget.setColumnCount(len(lines[0].split(',')))
                count = (len(lines)) - 1
                self.label_32.setText("+ " + str(count))
                print("+" + str(len(lines)))
                header = lines[0].strip().split(',')
                self.tableWidget.setHorizontalHeaderLabels(header)
                for row, line in enumerate(lines[1:]):
                    items = line.strip().split(',')
                    for col, item in enumerate(items):
                        table_item = QTableWidgetItem(item)
                        self.tableWidget.setItem(row, col, table_item)
                        print(row, col, item)
                self.tableWidget.resizeColumnsToContents()
                self.tableWidget.resizeRowsToContents()
            column_widths = [100, 150, 120, 80]
            for col, width in enumerate(column_widths):
                self.tableWidget.setColumnWidth(col, width)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def loadfeeds(self):
        file_path = 'MainMenu/Database/feedback.txt'
        try:

            with open(file_path, 'r') as file:
                paragraphs = file.read().split('\n\n')
                self.tableWidget_2.setRowCount(len(paragraphs))
                max_lines = max(len(para.split('\n')) for para in paragraphs) - 1
                self.tableWidget_2.setColumnCount(max_lines)
                print("Columns: ", max_lines)
                print("Rows: ", len(paragraphs))
                self.label_38.setText(str(len(paragraphs)))
                for row, paragraph in enumerate(paragraphs):
                    lines = paragraph.strip().split('\n')
                    for col, line in enumerate(lines):
                        item = QTableWidgetItem(line)
                        self.tableWidget_2.setItem(row, col, item)
                        # print(row, col, item)
                    self.tableWidget_2.resizeColumnsToContents()
                    self.tableWidget_2.resizeRowsToContents()
                column_widths = [100, 150, 120, 80]
                for col, width in enumerate(column_widths):
                    self.tableWidget_2.setColumnWidth(col, width)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")

    def updateLabel(self):
        current_count = int(self.label_35.text())  # Get the current count
        new_count = current_count + 1
        self.LoadRev()
        self.label_35.setText(str(new_count))  # Update the label with the new count

    def addTrainToCSV(self):

        print("Add Train")

        strt = self.lineEdit_3.text()
        end = self.lineEdit_4.text()
        wght = self.spinBox.text()
        time = self.timeEdit.text()
        print(strt, end, wght, time)
        # generate random name code
        name = ""
        for i in range(3):
            name += chr(random.randint(65, 90))
        if strt == "" or end == "" or time == "" or wght == "":
            self.label_3.setText("Please fill all the fields")
        else:
            self.label_3.setText("Train Added Successfully")
            with open('MainMenu/Database/TAT.csv', 'a') as file:
                file.write(f"\n{name},{time},{strt},{end}")
            with open('MainMenu/Database/graphAttributes.txt', 'a') as file:
                file.write(f"\n{strt},{end},{wght}")
            self.LoadTrains()

    def sideMenuChange(self):
        if self.sideMenu.width == 0:
            self.sideMenu.width = 200
        else:
            self.sideMenu.width = 0
        self.sideMenu.setFixedWidth(self.sideMenu.width)

    def saveData(self, event):
        # Save data to CSV files before closing the application
        self.saveToCSV('MainMenu/Database/TAT.csv', self.tableWidget)
        self.saveToCSV('MainMenu/Database/graphAttributes.txt', self.tableWidget_2)
        self.LoadWghts(self.tableWidget, [2, 3])

    def saveToCSV(self, file_path, table_widget):
        try:
            with open(file_path, 'w') as file:
                header_items = [table_widget.horizontalHeaderItem(i).text() for i in range(table_widget.columnCount())]
                header_line = ','.join(header_items)
                file.write(header_line + '\n')

                for row in range(table_widget.rowCount()):
                    row_items = [table_widget.item(row, col).text() for col in range(table_widget.columnCount())]
                    row_line = ','.join(row_items)
                    file.write(row_line + '\n')
        except Exception as e:
            print(f"Error saving data to {file_path}: {e}")

    def LoadWghts(self, table_widget, columns_to_save):
        path = 'MainMenu/Database/graphAttributes.txt'
        # assign random weights to the trains in the graph
        try:
            with open(path, 'w') as file:
                header_items = [table_widget.horizontalHeaderItem(i).text() for i in columns_to_save]
                header_line = ','.join(header_items)
                file.write("Graphs_Atribute" + '\n')

                for row in range(table_widget.rowCount()):
                    row_items = [table_widget.item(row, col).text() for col in columns_to_save]
                    row_line = ','.join(row_items) + ", " + str(random.randint(1, 14))
                    print(row_line)
                    file.write(row_line + '\n')
        except Exception as e:
            print(f"Error saving data to {path}: {e}")

    def LoadRev(self):
        with open('MainMenu/Database/revenue.txt', 'r') as file:
            count = file.read()
            self.label_29.setText(count)


def buildAdminMenu():
    mainWindow = MyApplication()
    mainWindow.show()
