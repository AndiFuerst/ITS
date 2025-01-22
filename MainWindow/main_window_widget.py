"""
This file handles the loading and configuring of the Main Window.
"""
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    """
    This class handles the loading and configuring of the Main Window.
    """
    def __init__(self):
        super().__init__()
        loadUi("MainWindow/main_window.ui", self)
        
        # Adding a Log In Menu Option on Right Side of Screen
        new_menu_bar = QMenuBar(self.menu_bar)
        menu = QMenu("Log In", new_menu_bar)
        new_menu_bar.addMenu(menu)
        self.menu_bar.setCornerWidget(new_menu_bar)
