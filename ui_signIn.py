# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_signInRZSwaB.ui'
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


class Ui_SignIn(object):
    def setupUi(self, SignIn):
        if SignIn.objectName():
            SignIn.setObjectName(u"SignIn")
        SignIn.setEnabled(True)
        SignIn.resize(741, 800)
        SignIn.setStyleSheet(u"")
        self.widget = QWidget(SignIn)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, -10, 700, 711))
        self.widget.setMaximumSize(QSize(700, 800))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 29, 201, 651))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 30, 411, 651))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 90, 161, 61))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rbga(0,0,0,200)")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 350, 361, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color:rgba(150,123,111,255);\n"
"}")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 120, 181, 141))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 540, 191, 20))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        self.label_4.setFont(font3)
        self.CreateAcc = QLabel(self.widget)
        self.CreateAcc.setObjectName(u"CreateAcc")
        self.CreateAcc.setGeometry(QRect(440, 540, 131, 21))
        self.CreateAcc.setFont(font3)
        self.CreateAcc.setCursor(QCursor(Qt.PointingHandCursor))
        self.CreateAcc.setStyleSheet(u"color: rgb(0, 106, 181);")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(240, 420, 31, 41))
        self.frame.setStyleSheet(u"image: url(:/images/google-icon.png);\n"
"border-radius:10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Google_btn_2 = QPushButton(self.widget)
        self.Google_btn_2.setObjectName(u"Google_btn_2")
        self.Google_btn_2.setGeometry(QRect(220, 420, 361, 41))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        font4.setPointSize(12)
        self.Google_btn_2.setFont(font4)
        self.Google_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Google_btn_2.setLayoutDirection(Qt.RightToLeft)
        self.Google_btn_2.setStyleSheet(u"QPushButton#Google_btn_2{\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#Google_btn_2:hover {\n"
"	background-color: rgb(208, 208, 208);\n"
"}")
        self.lineEdit_9 = QLineEdit(self.widget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(220, 250, 351, 41))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(10)
        self.lineEdit_9.setFont(font5)
        self.lineEdit_9.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)
        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(220, 180, 351, 41))
        self.lineEdit_7.setFont(font5)
        self.lineEdit_7.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 250, 201, 231))
        self.frame_2.setStyleSheet(u"image: url(:/images/train4.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        self.label_4.raise_()
        self.CreateAcc.raise_()
        self.Google_btn_2.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_7.raise_()
        self.frame.raise_()
        self.frame_2.raise_()

        self.retranslateUi(SignIn)

        QMetaObject.connectSlotsByName(SignIn)
    # setupUi

    def retranslateUi(self, SignIn):
        SignIn.setWindowTitle(QCoreApplication.translate("SignIn", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.pushButton.setText(QCoreApplication.translate("SignIn", u"Sign In", None))
        self.label_8.setText(QCoreApplication.translate("SignIn", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Railway</span></p><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Analysis</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("SignIn", u"Do not have an account?", None))
        self.CreateAcc.setText(QCoreApplication.translate("SignIn", u"Register Now", None))
        self.Google_btn_2.setText(QCoreApplication.translate("SignIn", u"Sign In with Google", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("SignIn", u"Password", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("SignIn", u"Username/Email", None))
    # retranslateUi

