from PyQt5 import QtCore, QtGui, QtWidgets

class IRCTC_Booking_App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create main layout
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Create login/register section
        self.login_register_layout = QtWidgets.QHBoxLayout()
        self.login_button = QtWidgets.QPushButton("Login")
        self.register_button = QtWidgets.QPushButton("Register")
        self.contact_us_button = QtWidgets.QPushButton("Contact Us")
        self.ask_disha_button = QtWidgets.QPushButton("Ask Disha")
        self.login_register_layout.addWidget(self.login_button)
        self.login_register_layout.addWidget(self.register_button)
        self.login_register_layout.addWidget(self.contact_us_button)
        self.login_register_layout.addWidget(self.ask_disha_button)
        self.main_layout.addLayout(self.login_register_layout)

        # Create date and destination section
        self.date_destination_layout = QtWidgets.QHBoxLayout()
        self.from_date_label = QtWidgets.QLabel("From:")
        self.from_date_edit = QtWidgets.QDateEdit(calendarPopup=True)
        self.from_date_edit.setDate(QtCore.QDate.currentDate())
        self.to_station_label = QtWidgets.QLabel("To:")
        self.to_station_combobox = QtWidgets.QComboBox()
        # Add stations tocombobox
        self.to_station_combobox.addItem("Select Station")
        self.to_station_combobox.addItem("New Delhi")
        self.to_station_combobox.addItem("Mumbai")
        self.to_station_combobox.addItem("Chennai")
        self.to_station_combobox.addItem("Kolkata")
        self.date_destination_layout.addWidget(self.from_date_label)
        self.date_destination_layout.addWidget(self.from_date_edit)
        self.date_destination_layout.addWidget(self.to_station_label)
        self.date_destination_layout.addWidget(self.to_station_combobox)
        self.main_layout.addLayout(self.date_destination_layout)

        # Create travel preference section
        self.travel_preference_layout = QtWidgets.QHBoxLayout()
        self.travel_class_label = QtWidgets.QLabel("Class:")
        self.travel_class_combobox = QtWidgets.QComboBox()
        self.travel_class_combobox.addItem("Select Class")
        self.travel_class_combobox.addItem("Sleeper")
        self.travel_class_combobox.addItem("AC 3 Tier")
        self.travel_class_combobox.addItem("AC 2 Tier")
        self.travel_class_combobox.addItem("AC 1 Tier")
        self.divyaang_concession_checkbox = QtWidgets.QCheckBox("Divyaang Concession")
        self.flexible_with_date_checkbox = QtWidgets.QCheckBox("Flexible With Date")
        self.travel_preference_layout.addWidget(self.travel_class_label)
        self.travel_preference_layout.addWidget(self.travel_class_combobox)
        self.travel_preference_layout.addWidget(self.divyaang_concession_checkbox)
        self.travel_preference_layout.addWidget(self.flexible_with_date_checkbox)
        self.main_layout.addLayout(self.travel_preference_layout)

        # Create search button
        self.search_button = QtWidgets.QPushButton("Search Trains")
        self.main_layout.addWidget(self.search_button)

        # Set window title and show
        self.setWindowTitle("IRCTC Train Booking")

        # Apply Stylesheet
        self.setStyleSheet('''
            QPushButton {
                background-color: #3498db;
                color: #ffffff;
                padding: 10px;
                border-radius: 5px;
            }
            QLabel {
                font-size: 14px;
                color: #2c3e50;
            }
            QComboBox {
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #bdc3c7;
            }
            QCheckBox {
                color: #2c3e50;
            }
        ''')

        self.show()

# Run the application
app = QtWidgets.QApplication([])
window = IRCTC_Booking_App()
app.exec_()
