from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Table Widget")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

       
        self.create_table()

        self.show()


    def create_table(self):
        vbox = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(5)
        table_widget.setColumnCount(3)

        table_widget.setItem(0,0, QTableWidgetItem("Name"))
        table_widget.setItem(0,1, QTableWidgetItem("Email"))
        table_widget.setItem(0,2, QTableWidgetItem("Phone No"))

        table_widget.setItem(1,0, QTableWidgetItem("Bob"))
        table_widget.setItem(1,1, QTableWidgetItem("Bob@gmail.com"))
        table_widget.setItem(1,2, QTableWidgetItem("11111111"))

        table_widget.setItem(2,0, QTableWidgetItem("Pariz"))
        table_widget.setItem(2,1, QTableWidgetItem("Pariz@gmail.com"))
        table_widget.setItem(2,2, QTableWidgetItem("22222222"))

        vbox.addWidget(table_widget)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())