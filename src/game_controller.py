from PySide6.QtWidgets import QApplication

from src.gui import SnakeGameGUI, PlayScreen


class GameController:
    def __init__(self):
        self.app = QApplication([])

        # Create instances of SnakeGameGUI and PlayScreen
        self.main_menu = SnakeGameGUI(self)
        self.play_screen = PlayScreen(self)

        # Show the main menu initially
        self.main_menu.show()

    def start(self):
        # Start the application event loop
        self.app.exec_()

    def show_play_screen(self):
        # Hide the main menu and show the play screen
        self.main_menu.hide()
        self.play_screen.show()

    def show_main_menu(self):
        # Hide the play screen and show the main menu
        self.play_screen.hide()
        self.main_menu.show()

