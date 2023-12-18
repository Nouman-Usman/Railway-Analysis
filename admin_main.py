from PySide2.QtWidgets import QApplication, QMainWindow
from admin import Ui_MainWindow  # Assuming you saved the UI code in ui_mainwindow.py


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
