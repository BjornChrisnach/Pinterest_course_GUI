from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 SpinBox")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))


        self.create_spinbox()

        self.show()

    def create_spinbox(self):
        vboxlayout = QVBoxLayout()

        self.spin = QSpinBox()
        self.spin.valueChanged.connect(self.spin_changed)

        self.label = QLabel()
        self.label.setFont(QFont("Times New Roman", 20))

        vboxlayout.addWidget(self.spin)
        vboxlayout.addWidget(self.label)
        self.setLayout(vboxlayout)


    def spin_changed(self):
        spin_value = self.spin.value()
        self.label.setText("Selected Value is : {} ".format(spin_value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())