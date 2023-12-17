import os
import shutil
import sys
import threading
import time

import mysql.connector
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *
from MainMenu import mainMenu1
import signInWithGoogle
from ui_signIn import Ui_SignIn
from ui_signUp import Ui_SignUp
import bcrypt


class SignInApp(QStackedWidget):
    def __init__(self):
        super().__init__()
        # Create instances of the UI forms
        self.ui_signin = Ui_SignIn()
        self.ui_signup = Ui_SignUp()
        self.resize(704, 800)
        self.widget_signin = QWidget()
        self.widget_signup = QWidget()
        self.ui_signin.setupUi(self.widget_signin)
        # Set up the sign-up form
        self.ui_signup.setupUi(self.widget_signup)
        # Add forms to the stacked widget
        self.addWidget(self.widget_signin)
        self.addWidget(self.widget_signup)

        # Connect signals to slots
        self.ui_signin.CreateAcc.mousePressEvent = self.show_signup_form
        self.ui_signup.LogIn.mousePressEvent = self.show_signin_form
        self.ui_signin.pushButton.clicked.connect(
            lambda: self.check(self.ui_signin.lineEdit_7.text(), self.ui_signin.lineEdit_9.text()))
        self.ui_signup.pushButton_3.clicked.connect(
            lambda: self.signup(self.ui_signup.lineEdit_7.text(), self.ui_signup.lineEdit_8.text(),
                                self.ui_signup.lineEdit_9.text()))
        self.ui_signup.UploadPic.clicked.connect(self.upload)
        self.ui_signin.Google_btn_2.clicked.connect(self.googleSignIN)
        self.ui_signup.Google_btn.clicked.connect(self.googleSignIN)

    def upload(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Upload Picture', '/upload', 'Image files (*.png)')
        if fname:
            self.ui_signup.profilePic.clear()
            original_pixmap = QPixmap(fname)
            size = self.ui_signup.profilePic.size()
            passport_size_pixmap = original_pixmap.scaled(71, 61)
            self.ui_signup.profilePic.setPixmap(passport_size_pixmap)
            self.ui_signup.profilePic.setAutoFillBackground(True)
            destination_file_name = 'Images/profile.png'
            destination_path = os.path.join(os.getcwd(), destination_file_name)
            shutil.copy(fname, destination_path)
            print("File copied successfully.")

    def connectDB(self):
        host = "127.0.0.1"
        user = "root"
        password = "1242"
        database = "student"

        try:
            self.db = mysql.connector.connect(host=host, user=user, password=password, database=database)
            if self.db.is_connected():
                cursor = self.db.cursor()
                # Execute SQL statements to create tables
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS signup (
                                username VARCHAR(50) NOT NULL UNIQUE,
                                email VARCHAR(100) NOT NULL UNIQUE,
                                password VARCHAR(255) NOT NULL
                            )
                        """)
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def googleSignIN(self):
        threading.Thread(target=signInWithGoogle.main).start()
        signInWithGoogle.MyRequestHandler.authentication_event.wait(timeout=12)
        if signInWithGoogle.MyRequestHandler.close_window_flag:
            print("Signed Up Successfully")
            print(signInWithGoogle.MyRequestHandler.name)
            self.open_main_menu(signInWithGoogle.MyRequestHandler.name)
        else:
            print("Authentication failed or timed out")

    def check(self, username, password):
        try:
            self.connectDB()
            cursor = self.db.cursor()
            check_user_query = """
                            SELECT * FROM signup
                            WHERE (username = %s )
                        """
            user_data = (username,)
            cursor.execute(check_user_query, user_data)
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[2].encode('utf-8')):
                    print(f"User {username} signed in successfully!")
                    self.open_main_menu(username)
                else:
                    print("Invalid username or password")
            else:
                print("Record Invalid")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def signup(self, username, email, password):
        try:
            # if username.text() = '' or
            self.connectDB()
            if email.__contains__('@'):
                print('Email is verified')
                cursor = self.db.cursor()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                # SQL statement to insert a new user
                insert_user_query = """
                    INSERT INTO signup (username, password, email)
                    VALUES (%s, %s, %s)
                """
                user_data = (username, hashed_password, email)
                cursor.execute(insert_user_query, user_data)
                self.db.commit()

                print(f"User {username} signed up successfully!")
                # self.close()
                self.open_main_menu(username)
            else:
                self.ui_signup.lineEdit_8.setText('')
                self.ui_signup.lineEdit_8.setFocus()
                self.ui_signup.lineEdit_8.setStyleSheet(
                    'background-color: rgba(0, 0, 0, 0); '
                    'border: none; '
                    'border-bottom: 2px solid rgba(46, 82, 101, 200); '
                    'color: rgb(255, 0, 0);'
                    'padding-bottom: 7px;'
                )
                self.ui_signup.lineEdit_8.setPlaceholderText('Enter Correct Email')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def show_signup_form(self, event):
        self.setCurrentIndex(1)

    def show_signin_form(self, event):
        self.setCurrentIndex(0)

    def open_main_menu(self, name):
        self.close()
        print('Main Menu')
        mainMenu1.build(SignInApp, name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = SignInApp()
    mainWindow.show()
    sys.exit(app.exec_())
