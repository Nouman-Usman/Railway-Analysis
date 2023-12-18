from PySide2.QtWidgets import QApplication, QStackedWidget, QWidget, QLabel
from PySide2.QtCore import Qt
from ui_signIn import Ui_SignIn
from ui_signUp import Ui_SignUp
import sys

class SignInApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Create instances of the UI forms
        self.ui_signin = Ui_SignIn()
        self.ui_signup = Ui_SignUp()