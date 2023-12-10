# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_signUpXAjEjg.ui'
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

import res_rc

class Ui_SignUp(object):
    def setupUi(self, SignUp):
        if SignUp.objectName():
            SignUp.setObjectName(u"SignUp")
        SignUp.resize(704, 800)
        self.widget = QWidget(SignUp)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, -10, 700, 800))
        self.widget.setMinimumSize(QSize(700, 800))
        self.widget.setMaximumSize(QSize(700, 800))
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 29, 201, 651))
        self.label_13.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-top-left-radius: 50px;")
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(200, 30, 411, 651))
        self.label_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(230, 90, 331, 61))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color:rbga(0,0,0,200)")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 420, 361, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color:rgba(150,123,111,255);\n"
"}")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 120, 181, 141))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_7 = QLineEdit(self.widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(220, 180, 351, 41))
        font3 = QFont()
        font3.setFamily(u"Times New Roman")
        font3.setPointSize(10)
        self.lineEdit_7.setFont(font3)
        self.lineEdit_7.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_8 = QLineEdit(self.widget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(220, 250, 351, 41))
        self.lineEdit_8.setFont(font3)
        self.lineEdit_8.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_9 = QLineEdit(self.widget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(220, 320, 351, 41))
        self.lineEdit_9.setFont(font3)
        self.lineEdit_9.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)
        self.LogIn = QLabel(self.widget)
        self.LogIn.setObjectName(u"LogIn")
        self.LogIn.setGeometry(QRect(450, 540, 47, 21))
        font4 = QFont()
        font4.setFamily(u"Times New Roman")
        self.LogIn.setFont(font4)
        self.LogIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.LogIn.setStyleSheet(u"color: rgb(0, 106, 181);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 540, 161, 20))
        self.label.setFont(font4)
        self.Google_frame = QFrame(self.widget)
        self.Google_frame.setObjectName(u"Google_frame")
        self.Google_frame.setGeometry(QRect(230, 490, 31, 41))
        self.Google_frame.setStyleSheet(u"image: url(:/images/google-icon.png);\n"
"border-radius:10px")
        self.Google_frame.setFrameShape(QFrame.StyledPanel)
        self.Google_frame.setFrameShadow(QFrame.Raised)
        self.Google_btn = QPushButton(self.widget)
        self.Google_btn.setObjectName(u"Google_btn")
        self.Google_btn.setGeometry(QRect(220, 490, 361, 41))
        font5 = QFont()
        font5.setFamily(u"Times New Roman")
        font5.setPointSize(12)
        self.Google_btn.setFont(font5)
        self.Google_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Google_btn.setLayoutDirection(Qt.RightToLeft)
        self.Google_btn.setStyleSheet(u"QPushButton#Google_btn{\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton#Google_btn:hover {\n"
"	background-color: rgb(208, 208, 208);\n"
"}")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 250, 201, 231))
        self.frame.setStyleSheet(u"image: url(:/images/train4.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton_3.raise_()
        self.label_18.raise_()
        self.lineEdit_7.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.LogIn.raise_()
        self.label.raise_()
        self.Google_btn.raise_()
        self.Google_frame.raise_()
        self.frame.raise_()

        self.retranslateUi(SignUp)

        QMetaObject.connectSlotsByName(SignUp)
    # setupUi

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(QCoreApplication.translate("SignUp", u"Form", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("SignUp", u"Create Account", None))
        self.pushButton_3.setText(QCoreApplication.translate("SignUp", u"Create Account", None))
        self.label_18.setText(QCoreApplication.translate("SignUp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Anonymous</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Analytics</span></p></body></html>", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("SignUp", u"Username", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("SignUp", u"Email Adress", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("SignUp", u"Password", None))
        self.LogIn.setText(QCoreApplication.translate("SignUp", u"Log In", None))
        self.label.setText(QCoreApplication.translate("SignUp", u"Already have an account?", None))
        self.Google_btn.setText(QCoreApplication.translate("SignUp", u"Sign In with Google", None))
    # retranslateUi

