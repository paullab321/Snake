from gui import SnakeGameGUI
from PySide6.QtWidgets import QApplication
import sys

def main():
    app = QApplication(sys.argv)
    snake_game_gui = SnakeGameGUI()
    snake_game_gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

