# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stackFIgLAQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import adminResource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 399)
        MainWindow.setMinimumSize(QSize(736, 399))
        MainWindow.setStyleSheet(u"QTimeEdit {\n"
"    /* Your general styling for QTimeEdit */\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    /* Styling for the drop-down arrow button */\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 15px;\n"
"    border-left: 1px solid #ccc;\n"
"    background-color: #e0e0e0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.caedFrame = QWidget(self.body)
        self.caedFrame.setObjectName(u"caedFrame")
        self.horizontalLayout_19 = QHBoxLayout(self.caedFrame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.caedFrame)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(200, 25))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.profile_2 = QPushButton(self.widget_6)
        self.profile_2.setObjectName(u"profile_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_2.sizePolicy().hasHeightForWidth())
        self.profile_2.setSizePolicy(sizePolicy)
        self.profile_2.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_2.setIcon(icon)
        self.profile_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.profile_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.label_27 = QLabel(self.widget_6)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)
        self.label_27.setMinimumSize(QSize(125, 30))
        self.label_27.setMaximumSize(QSize(125, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"color: rgb(37, 150, 190);\n"
"")
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_27, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_19.addWidget(self.widget_6, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.caedFrame)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.seachFrame_2 = QFrame(self.widget_7)
        self.seachFrame_2.setObjectName(u"seachFrame_2")
        self.seachFrame_2.setMinimumSize(QSize(160, 0))
        self.seachFrame_2.setStyleSheet(u"")
        self.seachFrame_2.setFrameShape(QFrame.StyledPanel)
        self.seachFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.seachFrame_2)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 10, 0, 5)
        self.stackedWidget_2 = QStackedWidget(self.seachFrame_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_5 = QHBoxLayout(self.page)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setPixmap(QPixmap(u":/icons/search.svg"))

        self.horizontalLayout_5.addWidget(self.label_28, 0, Qt.AlignRight|Qt.AlignTop)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setStyleSheet(u"background-color: transparent;\n"
"border-radius:10px;\n"
"border:1.5px solid #2596be")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lineEdit_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_2.addWidget(self.page_2)

        self.horizontalLayout_22.addWidget(self.stackedWidget_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_21.addWidget(self.seachFrame_2)


        self.horizontalLayout_19.addWidget(self.widget_7, 0, Qt.AlignRight)

        self.widget_8 = QWidget(self.caedFrame)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.sideMenuButton_2 = QPushButton(self.widget_8)
        self.sideMenuButton_2.setObjectName(u"sideMenuButton_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sideMenuButton_2.sizePolicy().hasHeightForWidth())
        self.sideMenuButton_2.setSizePolicy(sizePolicy3)
        self.sideMenuButton_2.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/align-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sideMenuButton_2.setIcon(icon1)
        self.sideMenuButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.sideMenuButton_2, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_19.addWidget(self.widget_8)


        self.verticalLayout.addWidget(self.caedFrame)

        self.mainFrame = QWidget(self.body)
        self.mainFrame.setObjectName(u"mainFrame")
        self.horizontalLayout_24 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.mainFrame)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 12)
        self.card1_3 = QWidget(self.widget_9)
        self.card1_3.setObjectName(u"card1_3")
        self.card1_3.setMinimumSize(QSize(160, 0))
        self.card1_3.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_10 = QVBoxLayout(self.card1_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_9 = QFrame(self.card1_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border:none;\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_29 = QLabel(self.frame_9)
        self.label_29.setObjectName(u"label_29")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"border:none;")

        self.horizontalLayout_26.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(20, 20))
        self.label_30.setMaximumSize(QSize(20, 20))
        self.label_30.setStyleSheet(u"border:none;")
        self.label_30.setPixmap(QPixmap(u":/icons/shopping-cart.svg"))
        self.label_30.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_30)


        self.verticalLayout_10.addWidget(self.frame_9)

        self.label_31 = QLabel(self.card1_3)
        self.label_31.setObjectName(u"label_31")
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"border:none;")

        self.verticalLayout_10.addWidget(self.label_31, 0, Qt.AlignTop)


        self.horizontalLayout_25.addWidget(self.card1_3)

        self.card2_3 = QWidget(self.widget_9)
        self.card2_3.setObjectName(u"card2_3")
        self.card2_3.setMinimumSize(QSize(160, 0))
        self.card2_3.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_11 = QVBoxLayout(self.card2_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_10 = QFrame(self.card2_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:none;\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"border:none;")

        self.horizontalLayout_27.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(20, 20))
        self.label_33.setMaximumSize(QSize(20, 20))
        self.label_33.setStyleSheet(u"border:none;")
        self.label_33.setPixmap(QPixmap(u":/icons/activity.svg"))
        self.label_33.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_33)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.label_34 = QLabel(self.card2_3)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"border:none;")

        self.verticalLayout_11.addWidget(self.label_34, 0, Qt.AlignTop)


        self.horizontalLayout_25.addWidget(self.card2_3)

        self.card3_3 = QWidget(self.widget_9)
        self.card3_3.setObjectName(u"card3_3")
        self.card3_3.setMinimumSize(QSize(160, 0))
        self.card3_3.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_12 = QVBoxLayout(self.card3_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_11 = QFrame(self.card3_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:none;\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_35 = QLabel(self.frame_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font1)
        self.label_35.setStyleSheet(u"border:none;")

        self.horizontalLayout_28.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(20, 20))
        self.label_36.setMaximumSize(QSize(20, 20))
        self.label_36.setStyleSheet(u"border:none;")
        self.label_36.setPixmap(QPixmap(u":/icons/send.svg"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_36)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.label_37 = QLabel(self.card3_3)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"border:none;")

        self.verticalLayout_12.addWidget(self.label_37, 0, Qt.AlignTop)


        self.horizontalLayout_25.addWidget(self.card3_3)

        self.card4_3 = QWidget(self.widget_9)
        self.card4_3.setObjectName(u"card4_3")
        self.card4_3.setMinimumSize(QSize(160, 0))
        self.card4_3.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_13 = QVBoxLayout(self.card4_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_12 = QFrame(self.card4_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:none;\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_38 = QLabel(self.frame_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"border:none;")

        self.horizontalLayout_29.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(20, 20))
        self.label_39.setMaximumSize(QSize(20, 20))
        self.label_39.setStyleSheet(u"border:none;")
        self.label_39.setPixmap(QPixmap(u":/icons/message-square.svg"))
        self.label_39.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_39)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.label_40 = QLabel(self.card4_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"border:none;")

        self.verticalLayout_13.addWidget(self.label_40, 0, Qt.AlignTop)


        self.horizontalLayout_25.addWidget(self.card4_3)


        self.horizontalLayout_24.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.mainFrame, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.schedule = QWidget()
        self.schedule.setObjectName(u"schedule")
        self.verticalLayout_3 = QVBoxLayout(self.schedule)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.schedule)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: rgb(37, 149, 188);")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(254, 254, 255);")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget)

        self.tableWidget = QTableWidget(self.schedule)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setStyleSheet(u"background-color: rgb(254, 254, 255);")

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.schedule)
        self.feedback = QWidget()
        self.feedback.setObjectName(u"feedback")
        self.verticalLayout_6 = QVBoxLayout(self.feedback)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.feedback)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setStyleSheet(u"background-color: rgb(37, 149, 188);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(254, 254, 255);")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.tableWidget_2 = QTableWidget(self.feedback)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy4.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy4)
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(254, 254, 255);")

        self.verticalLayout_6.addWidget(self.tableWidget_2)

        self.stackedWidget.addWidget(self.feedback)
        self.addTrain = QWidget()
        self.addTrain.setObjectName(u"addTrain")
        self.verticalLayout_7 = QVBoxLayout(self.addTrain)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_4 = QWidget(self.addTrain)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setStyleSheet(u"background-color: rgb(254, 254, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(22, 28))
        font4 = QFont()
        font4.setFamily(u"Gill Sans Ultra Bold")
        font4.setPointSize(22)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"color: rgb(37, 150, 190);")

        self.verticalLayout_8.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.addTrain)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be;\n"
"color: rgb(37, 150, 190);")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"border:none;")

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"border:none;")

        self.verticalLayout_9.addWidget(self.label_5)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_12 = QWidget(self.widget_3)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_14 = QVBoxLayout(self.widget_12)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 12)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"border:none;")
        self.gridLayout = QGridLayout(self.widget_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_3 = QLineEdit(self.widget_13)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        self.lineEdit_3.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 2px;\n"
"border-bottom: 1.5px solid #2596be;")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 0, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"border:none;")
        self.verticalLayout_15 = QVBoxLayout(self.widget_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lineEdit_4 = QLineEdit(self.widget_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 2px;\n"
"border-bottom: 1.5px solid #2596be;")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.lineEdit_4)


        self.verticalLayout_14.addWidget(self.widget_14)


        self.horizontalLayout.addWidget(self.widget_12)

        self.widget_10 = QWidget(self.widget_3)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be;\n"
"color: rgb(37, 150, 190);")
        self.verticalLayout_16 = QVBoxLayout(self.widget_10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"border:none;")

        self.verticalLayout_16.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"border:none;")

        self.verticalLayout_16.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_3)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"border-radius:10px;\n"
"border:1px solid #2596be")
        self.verticalLayout_19 = QVBoxLayout(self.widget_11)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_11)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_17 = QVBoxLayout(self.widget_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"border:none;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox = QSpinBox(self.widget_17)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background-color: #f0f0f0;")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(50)
        self.spinBox.setSingleStep(1)
        self.spinBox.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout_17.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setStyleSheet(u"border:none;")
        self.verticalLayout_18 = QVBoxLayout(self.widget_18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.timeEdit = QTimeEdit(self.widget_18)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy5)
        font6 = QFont()
        font6.setFamily(u"Times New Roman")
        font6.setPointSize(9)
        font6.setBold(False)
        font6.setWeight(50)
        self.timeEdit.setFont(font6)
        self.timeEdit.setAutoFillBackground(False)
        self.timeEdit.setStyleSheet(u" background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 2px;")

        self.verticalLayout_18.addWidget(self.timeEdit)


        self.verticalLayout_17.addWidget(self.widget_18)


        self.verticalLayout_19.addWidget(self.widget_16)


        self.horizontalLayout.addWidget(self.widget_11)


        self.verticalLayout_7.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.widget_15 = QWidget(self.addTrain)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy4.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")

        self.horizontalLayout_3.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.widget_15)
        self.widget_20.setObjectName(u"widget_20")

        self.horizontalLayout_3.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_15)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_20 = QVBoxLayout(self.widget_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.viewMore = QPushButton(self.widget_21)
        self.viewMore.setObjectName(u"viewMore")
        self.viewMore.setMinimumSize(QSize(150, 35))
        self.viewMore.setMaximumSize(QSize(120, 20))
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.viewMore.setFont(font7)
        self.viewMore.setStyleSheet(u"background-color: rgb(254, 254, 255);\n"
"color: rgb(37, 150, 190);\n"
"border-radius:10px;\n"
"border:1.5px solid #2596be;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/arrow-down-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.viewMore.setIcon(icon2)

        self.verticalLayout_20.addWidget(self.viewMore, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.widget_21)


        self.verticalLayout_7.addWidget(self.widget_15)

        self.stackedWidget.addWidget(self.addTrain)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.body)

        self.sideMenu = QFrame(self.centralwidget)
        self.sideMenu.setObjectName(u"sideMenu")
        sizePolicy4.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy4)
        self.sideMenu.setMinimumSize(QSize(0, 0))
        self.sideMenu.setMaximumSize(QSize(0, 16777215))
        self.sideMenu.setStyleSheet(u"\n"
"color: rgb(0, 170, 255);")
        self.verticalLayout_26 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.sideMenu)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 25, 0)
        self.label_22 = QLabel(self.widget_24)
        self.label_22.setObjectName(u"label_22")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"border:none;")
        self.label_22.setPixmap(QPixmap(u":/icons/activity.svg"))

        self.horizontalLayout_18.addWidget(self.label_22)

        self.label_19 = QLabel(self.widget_24)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"border:none;")

        self.horizontalLayout_18.addWidget(self.label_19)


        self.verticalLayout_26.addWidget(self.widget_24, 0, Qt.AlignRight|Qt.AlignTop)

        self.widget_25 = QWidget(self.sideMenu)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy7)
        self.widget_25.setMinimumSize(QSize(200, 0))
        self.verticalLayout_27 = QVBoxLayout(self.widget_25)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.toolBox_2 = QToolBox(self.widget_25)
        self.toolBox_2.setObjectName(u"toolBox_2")
        sizePolicy7.setHeightForWidth(self.toolBox_2.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy7)
        self.toolBox_2.setFont(font)
        self.toolBox_2.setStyleSheet(u"background-color: rgb(254, 254, 255);")
        self.toolBox_2.setFrameShape(QFrame.NoFrame)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 182, 279))
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statsBut = QPushButton(self.page_5)
        self.statsBut.setObjectName(u"statsBut")
        self.statsBut.setStyleSheet(u"background-color: rgb(37, 150, 190);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1.5px solid #2596be")
        icon3 = QIcon()
        icon3.addFile(u":/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statsBut.setIcon(icon3)
        self.statsBut.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.statsBut)

        self.feedbackBut = QPushButton(self.page_5)
        self.feedbackBut.setObjectName(u"feedbackBut")
        self.feedbackBut.setStyleSheet(u"background-color: rgb(37, 150, 190);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1.5px solid #2596be")
        icon4 = QIcon()
        icon4.addFile(u":/icons/airplay.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.feedbackBut.setIcon(icon4)
        self.feedbackBut.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.feedbackBut)

        self.addTrainBut = QPushButton(self.page_5)
        self.addTrainBut.setObjectName(u"addTrainBut")
        self.addTrainBut.setStyleSheet(u"background-color: rgb(37, 150, 190);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:1.5px solid #2596be")
        icon5 = QIcon()
        icon5.addFile(u":/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addTrainBut.setIcon(icon5)
        self.addTrainBut.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.addTrainBut)

        icon6 = QIcon()
        icon6.addFile(u":/icons/chevron-down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_2.addItem(self.page_5, icon6, u"Main Menu")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 182, 279))
        self.verticalLayout_29 = QVBoxLayout(self.page_6)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_6)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy8)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_6)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        font8 = QFont()
        font8.setFamily(u"Times New Roman")
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setWeight(50)
        self.label_23.setFont(font8)
        self.label_23.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_23, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_29.addWidget(self.frame_6)

        self.toolBox_2.addItem(self.page_6, icon6, u"About")

        self.verticalLayout_27.addWidget(self.toolBox_2)


        self.verticalLayout_26.addWidget(self.widget_25)


        self.horizontalLayout_4.addWidget(self.sideMenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.profile_2.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Admin Menu", None))
        self.label_28.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Something", None))
        self.sideMenuButton_2.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"200,0000", None))
        self.label_30.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"PKR", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"+30", None))
        self.label_33.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Trains", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"58", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Arrived", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Feedbacks", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Train Schedule", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Feedbacks", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Add Train Route", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Point", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"End Point", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Lahore", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Multan", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Distance", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Train Start Time", None))
        self.viewMore.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_22.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Side Menu", None))
        self.statsBut.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.feedbackBut.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.addTrainBut.setText(QCoreApplication.translate("MainWindow", u"Add Train", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"The application is developed by Nouman, Shahbaz and Khuram ", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

