from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Menu & Toolbar")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))


        self.createMenu()


        self.show()


    def createMenu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        edit_menu = main_menu.addMenu("Edit")
        view_menu = main_menu.addMenu("View")

        copyAction = QAction(QIcon("icons/copy.png"), "Copy", self)
        copyAction.setShortcut("Ctrl+c")
        file_menu.addAction(copyAction)

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+s")
        edit_menu.addAction(saveAction)

        exitAction = QAction(QIcon("icons/exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+x")
        exitAction.triggered.connect(self.exit_window)
        file_menu.addAction(exitAction)

        # toolbar
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)



    def exit_window(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())