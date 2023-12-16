# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Train SelectionhxYIcy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import csv
from PySide2.QtWidgets import QTableWidgetItem, QCheckBox


class Ui_Select_Train(object):
    def setupUi(self, Select_Train):
        if not Select_Train.objectName():
            Select_Train.setObjectName(u"Select_Train")
        Select_Train.resize(300, 300)
        self.label = QLabel(Select_Train)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 47, 14))
        self.label_2 = QLabel(Select_Train)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 10, 41, 21))
        self.label_3 = QLabel(Select_Train)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 10, 71, 20))
        self.comboBox = QComboBox(Select_Train)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 10, 60, 22))
        self.tableWidget = QTableWidget(Select_Train)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(5, 80, 291, 221))

        self.retranslateUi(Select_Train)

        QMetaObject.connectSlotsByName(Select_Train)
    # setupUi
        # Modify the tableWidget to have checkboxes in the first column
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Select", "Train", "Timing"])

        # Load data from "Train and Timing.csv"
        with open("Database/Train and Timing.csv", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)

            # Set the number of rows based on the data in the CSV
            self.tableWidget.setRowCount(len(data))

            # Populate the tableWidget with checkboxes in the first column
            for row in range(len(data)):
                checkbox = QCheckBox()
                self.tableWidget.setCellWidget(row, 0, checkbox)

                for col in range(1, 3):
                    item = QTableWidgetItem(data[row][col - 1])
                    self.tableWidget.setItem(row, col, item)


    def retranslateUi(self, Select_Train):
        Select_Train.setWindowTitle(QCoreApplication.translate("Select_Train", u"Form", None))
        self.label.setText(QCoreApplication.translate("Select_Train", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("Select_Train", u"Sort", None))
        self.label_3.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Select_Train", u"Name", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Select_Train", u"Time", None))

    # retranslateUi

