from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 ListWidget")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.create_listwidget()

        self.show()


    def create_listwidget(self):
        vbox = QVBoxLayout()

        self.list = QListWidget()
        self.list.insertItem(0, "Linux")
        self.list.insertItem(1, "Windows")
        self.list.insertItem(2, "Mac")
        self.list.insertItem(3, "Android")
        self.list.insertItem(4, "IOS")
        
        self.list.setFont(QFont("Times New Roman", 13))
        self.list.clicked.connect(self.listview_clicked)


        self.label = QLabel()
        self.label.setFont(QFont("Times New Roman", 13))


        vbox.addWidget(self.list)
        vbox.addWidget(self.label)
        self.setLayout(vbox)


    def listview_clicked(self):
        item = self.list.currentItem()
        self.label.setText(str(item.text()))
        self.label.setStyleSheet('color:red')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())