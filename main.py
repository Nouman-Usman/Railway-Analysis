import sys
import threading
import mysql.connector
from PySide2.QtWidgets import *
import signInWithGoogle
from ui_signIn import Ui_SignIn
from ui_signUp import Ui_SignUp
import hashlib
import bcrypt
import secrets

class SignInApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Create instances of the UI forms
        self.ui_signin = Ui_SignIn()
        self.ui_signup = Ui_SignUp()
        self.resize(704, 800)
        self.widget_signin = QWidget()
        self.widget_signup = QWidget()

        # Set up the sign-in form
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
        self.ui_signin.Google_btn_2.clicked.connect(self.googleSignIN)

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
        print('google')
        threading.Thread(target=signInWithGoogle.main).start()

    def check(self, username, password):
        try:
            self.connectDB()

            # Assuming you have a cursor object
            cursor = self.db.cursor()

            # SQL statement to check if the user exists
            check_user_query = """
                    SELECT * FROM signup
                    WHERE (username = %s AND password = %s )
                """
            user_data = (username, password)
            cursor.execute(check_user_query, user_data)
            result = cursor.fetchone()

            if result:
                print(f"User {username} signed in successfully!")
            else:
                print("Invalid username or password")

        except mysql.connector.Error as err:
            # Handle errors appropriately in your application
            print(f"Error: {err}")

    def signup(self, username, email, password):
        try:
            self.connectDB()
            if email.__contains__('@'):
                print('Email is verified')
                cursor = self.db.cursor()

                # SQL statement to insert a new user
                insert_user_query = """
                    INSERT INTO signup (username, password, email)
                    VALUES (%s, %s, %s)
                """
                user_data = (username, password, email)
                cursor.execute(insert_user_query, user_data)
                self.db.commit()

                print(f"User {username} signed up successfully!")
            else:
                print('Please enter correct email address')
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def show_signup_form(self, event):
        # Switch to the sign-up form
        self.setCurrentIndex(1)

    def show_signin_form(self, event):
        # Switch to the sign-in form
        self.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = SignInApp()
    mainWindow.show()
    sys.exit(app.exec_())
