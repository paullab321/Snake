from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGraphicsView, QGraphicsScene, \
    QHBoxLayout
from PySide6.QtGui import QScreen, QFont, QIcon

from src import game_controller
from src.game_controller import GameController

# Constants for width and height
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = "#8F9691"
BUTTON_STYLE = """
    QPushButton {
        background-color: #4CAF50; /* Green */
        color: white;
        border: 1px solid #4CAF50;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #45a049; /* Darker green */
    }
"""

class SnakeGameGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.game_controller: GameController = game_controller

        # Set up the main window
        self.setWindowTitle("Snake Game")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")
        self.setContentsMargins(10, 10, 10, 10)

        # Create widgets
        self.label_welcome = QLabel("Welcome to Snake Game")
        self.button_start = QPushButton("Start Game", clicked=self.start_game)
        self.button_options = QPushButton("Options", clicked=self.show_options)

        # Set font size and style for the label
        font = QFont()
        font.setPointSize(20)
        self.label_welcome.setFont(font)

        self.button_start.setFixedSize(200, 50)
        self.button_options.setFixedSize(200, 50)

        # Set up the layout
        layout = QVBoxLayout(self)

        # Add label to layout
        label_layout = QVBoxLayout()
        label_layout.addWidget(self.label_welcome, alignment=Qt.AlignTop | Qt.AlignHCenter)
        label_layout.setContentsMargins(40, 40, 40, 200)
        layout.addLayout(label_layout)

        # Add Start Game button to layout
        button_layout_start = QVBoxLayout()
        button_layout_start.addWidget(self.button_start, alignment=Qt.AlignCenter | Qt.AlignCenter)
        button_layout_start.setContentsMargins(40, 150, 40, 20)
        layout.addLayout(button_layout_start)

        # Add Button Options button to layout
        button_layout_options = QVBoxLayout()
        button_layout_options.addWidget(self.button_options, alignment=Qt.AlignCenter | Qt.AlignCenter)
        button_layout_options.setContentsMargins(40, 20, 40, 200)
        layout.addLayout(button_layout_options)

        # Center the window on the screen
        self.center_window()
        # Set fixed size to make the window not resizable
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        icon_path = "snake.png"
        self.setWindowIcon(QIcon(icon_path))

        self.button_start.setStyleSheet(BUTTON_STYLE)
        self.button_options.setStyleSheet(BUTTON_STYLE)

    def start_game(self):
        print("Starting game")
        self.game_controller.show_play_screen()

    def show_options(self):
        print("Options button clicked!")

    def center_window(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        center_position = screen.center()
        self.setGeometry(center_position.x() - WINDOW_WIDTH // 2, center_position.y() - WINDOW_HEIGHT // 2, WINDOW_WIDTH, WINDOW_HEIGHT)

class PlayScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.game_controller = game_controller

        self.setWindowTitle("Play Screen")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

        # Create widgets
        self.label_score = QLabel("Score: 0")
        self.button_return_to_menu = QPushButton("Return to Menu", clicked=self.return_to_menu)
        self.button_retry = QPushButton("Retry", clicked=self.retry)
        self.canvas_view = QGraphicsView()
        self.canvas_scene = QGraphicsScene()
        self.canvas_view.setScene(self.canvas_scene)

        # Set font size and style for the label
        font = QFont()
        font.setPointSize(16)
        self.label_score.setFont(font)

        # Set up the layout
        layout = QVBoxLayout(self)

        # Add score label to layout
        score_layout = QHBoxLayout()
        score_layout.addWidget(self.label_score, alignment=Qt.AlignLeft)
        layout.addLayout(score_layout)

        # Add return to menu and retry buttons to layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_return_to_menu, alignment=Qt.AlignLeft)
        button_layout.addWidget(self.button_retry, alignment=Qt.AlignRight)
        layout.addLayout(button_layout)

        # Add canvas to layout
        layout.addWidget(self.canvas_view)

    def return_to_menu(self):
        # Add functionality to return to the main menu
        pass

    def retry(self):
        # Add functionality to retry the game
        pass



