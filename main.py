"""
Main file to start ITS.
"""
import sys
from PyQt5.QtWidgets import QApplication
from MainWindow.main_window_widget import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
