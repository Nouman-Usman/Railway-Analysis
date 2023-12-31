import csv
import os
import shutil
import sys
import threading
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

import MainMenu.adminMenu
from MainMenu import mainMenu1
# from MainMenu import ui_error
# from MainMenu import ui_dialog
import signInWithGoogle
from ui_signIn import Ui_SignIn
from ui_signUp import Ui_SignUp
import requests
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
        self.ui_signup.setupUi(self.widget_signup)
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

    # def showAdminMenu(self):

    def connect_csv(self):
        csv_file = 'MainMenu/Database/users.csv'
        # Create the CSV file if it doesn't exist
        try:
            with open(csv_file, 'r') as _:
                pass
        except FileNotFoundError:
            with open(csv_file, 'w', newline='') as csvfile:
                fieldnames = ['username', 'email', 'password']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    def googleSignIN(self):
        threading.Thread(target=signInWithGoogle.main).start()
        signInWithGoogle.MyRequestHandler.authentication_event.wait()
        if signInWithGoogle.MyRequestHandler.close_window_flag:
            url = signInWithGoogle.MyRequestHandler.profile_url
            download_thread = threading.Thread(target=self.download_image, args=(url,))
            download_thread.start()
            download_thread.join()
            self.open_main_menu(signInWithGoogle.MyRequestHandler.name)
        else:
            mainMenu1.MainWindow.show_error_popup(self, 'Error ', 'Authentication Failed')

    def download_image(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            with open("Images/profile.png", "wb") as file:
                file.write(response.content)
        else:
            mainMenu1.MainWindow.show_error_popup(self, 'Warning',
                                                  f"Failed to download image. Status code: {response.status_code}")

    def check(self, username, password):
        try:
            if not username or not password:
                mainMenu1.MainWindow.show_error_popup(self, 'Warning',
                                                      "Please fill out all the fields.")
            elif username == 'admin' and password == 'admin':
                MainMenu.adminMenu.buildAdminMenu()
            else:
                self.connect_csv()
                with open('MainMenu/Database/users.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    user_row = next((row for row in reader if row['username'] == username), None)

                if user_row:
                    stored_password = user_row['password']
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        mainMenu1.MainWindow.show_info_popup(self, 'Hurrah ',
                                                             f"User {username} signed in successfully!")
                        self.open_main_menu(username)
                    else:
                        mainMenu1.MainWindow.show_error_popup(self, 'Ooops', "Invalid username or password")

                else:
                    mainMenu1.MainWindow.show_error_popup(self, 'Ooops', "Record Invalid")

        except Exception as e:
            mainMenu1.MainWindow.show_error_popup(self, 'Attention', f'Error: {e}')
            raise

    def signup(self, username, email, password):
        try:
            if not username or not email or not password:
                mainMenu1.MainWindow.show_error_popup(self, 'Attention', f'Please fill out all the fields.')
            else:
                self.connect_csv()
                with open('MainMenu/Database/users.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    if any(row['username'] == username or row['email'] == email for row in reader):
                        mainMenu1.MainWindow.show_error_popup(self, 'No Brother', 'Username or email already exists.')
                    else:
                        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
                        new_user = {'username': username, 'email': email, 'password': hashed_password}

                        with open('MainMenu/Database/users.csv', 'a', newline='') as csvfile:
                            fieldnames = ['username', 'email', 'password']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                            # Write header only if the file is empty
                            if not csvfile.tell():
                                writer.writeheader()
                            writer.writerow(new_user)
                        mainMenu1.MainWindow.show_error_popup(self, 'Huraaaaaaah!!!', f'User {username} signed up Successfully')
                        # breakpoint()
                        self.open_main_menu(username)
        except Exception as e:
            print(e)
            mainMenu1.MainWindow.show_error_popup(self, 'Attention', f'Error: {e}')

    def show_signup_form(self, event):
        self.setCurrentIndex(1)

    def show_signin_form(self, event):
        self.setCurrentIndex(0)

    def open_main_menu(self, name):
        self.hide()
        mainMenu1.build(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = SignInApp()
    mainWindow.show()
    sys.exit(app.exec_())
