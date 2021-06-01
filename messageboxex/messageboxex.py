from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 MessageBox")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        vbox = QVBoxLayout()
        btn = QPushButton("Open MessageBox", self)
        btn.clicked.connect(self.create_messagebox)

        vbox.addWidget(btn)

        self.setLayout(vbox)
      

        self.show()


    def create_messagebox(self):
        # message = QMessageBox.information(self, "Info MessageBox", "This is a messagebox")
        # message = QMessageBox.warning(self, "Warn MessageBox", "This is a messagebox")
        # message = QMessageBox.about(self, "About MessageBox", "This is messagebox")
        message = QMessageBox.question(self, "Choice MessageBox", "Do you like Python ?", 
                                        QMessageBox.Yes | QMessageBox.No)

        if message == QMessageBox.Yes:
            print("Yes i like python")
        else:
            print("No I don't like it")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())