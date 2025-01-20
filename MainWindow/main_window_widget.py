"""
This file handles the loading and configuring of the Main Window.
"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    """
    This class handles the loading and configuring of the Main Window.
    """
    def __init__(self):
        super().__init__()
        loadUi("MainWindow/main_window.ui", self)
        