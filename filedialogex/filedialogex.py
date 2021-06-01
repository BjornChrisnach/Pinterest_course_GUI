from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QVBoxLayout, QPushButton, QLabel
import sys
from PyQt5.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 File Dialog")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        vbox = QVBoxLayout()
        btn = QPushButton("Browse Image")
        btn.clicked.connect(self.browse_image)
        vbox.addWidget(btn)

        self.label = QLabel("")
        vbox.addWidget(self.label)

        self.setLayout(vbox)


        self.show()


    def browse_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files' '(*.jpg, *.png)')
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())