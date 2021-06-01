from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
import sys
from PyQt5.QtGui import QIcon, QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Adding Image")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))


        hbox = QHBoxLayout()

        image_label = QLabel(self)
        pixmap = QPixmap("images/pyqt.png")
        image_label.setPixmap(pixmap)

        hbox.addWidget(image_label)

        self.setLayout(hbox)


        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())