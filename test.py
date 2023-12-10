import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap


class ProfilePicUploader(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Profile Picture Uploader')

        self.profile_label = QLabel('No Image Selected')
        self.profile_image = QLabel(self)
        self.profile_image.setPixmap(QPixmap('default_profile_pic.png'))  # Set a default image

        self.upload_button = QPushButton('Upload Profile Picture', self)
        self.upload_button.clicked.connect(self.show_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.profile_label)
        layout.addWidget(self.profile_image)
        layout.addWidget(self.upload_button)

        self.setLayout(layout)

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'Image files (*.jpg *.gif *.png)')

        if fname[0]:
            # Load the original image
            original_pixmap = QPixmap(fname[0])

            # Resize the image to a specific passport size (e.g., 2x2 inches)
            passport_size_pixmap = original_pixmap.scaled(200, 200)
            # Update the profile image
            self.profile_image.setPixmap(passport_size_pixmap)
            self.profile_label.setText('Image Selected: ' + fname[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfilePicUploader()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
