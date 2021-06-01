from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Calendar")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))


        vbox = QVBoxLayout()
        calendar = QCalendarWidget()
        calendar.setGridVisible(True)

        vbox.addWidget(calendar)

        self.setLayout(vbox)


        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())