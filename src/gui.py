from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGraphicsView, QGraphicsScene, \
    QHBoxLayout, QMessageBox
from PySide6.QtGui import QScreen, QFont, QIcon
import os
from constants import (WINDOW_HEIGHT, WINDOW_WIDTH, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_STYLE, BACKGROUND_COLOR,
                       FONT_SIZE, ICON_PATH)


# Used in MainMenu and SubMenu to reduce redundancy
class BaseUtilityClass(QWidget):
    # used to center a Widget, in this case MainMenu and SubMenu
    def center_window(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        center_position = screen.center()
        self.setGeometry(center_position.x() - WINDOW_WIDTH // 2, center_position.y() - WINDOW_HEIGHT // 2,
                         WINDOW_WIDTH, WINDOW_HEIGHT)

    # styling buttons teh same using the global constants
    @staticmethod
    def style_button(button):
        button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        button.setStyleSheet(BUTTON_STYLE)
        return button

    # fonts will now all be the same size, when added in a Widget
    @staticmethod
    def init_font():
        font = QFont()
        font.setPointSize(FONT_SIZE)
        return font

    # sets the icon for the widget, and handles exception for missing icon_path
    @staticmethod
    def set_window_icon(widget, icon_path):
        if os.path.isfile(icon_path):
            widget.setWindowIcon(QIcon(icon_path))
        else:
            QMessageBox.warning(widget, "Icon Load Error", f"Icon file not found: {icon_path}")
            print(f"Icon file not found: {icon_path}")


class MainMenu(BaseUtilityClass):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Snake Game")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")
        self.setContentsMargins(10, 10, 10, 10)

        # Create widgets
        self.label_welcome = QLabel("Welcome to Snake Game")
        self.label_welcome.setFont(self.init_font())
        self.button_start = self.style_button(QPushButton("Start Game", clicked=self.show_sub_menu))
        self.button_options = self.style_button(QPushButton("Options", clicked=self.show_options))

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

        self.set_window_icon(self, ICON_PATH)

        self.play_screen = SubMenu(self)

    def show_sub_menu(self):
        print("Starting game")
        self.hide()
        self.play_screen.show()

    def show_options(self):
        print("Options button clicked!")
        pass


class SubMenu(BaseUtilityClass):
    def __init__(self, main_menu):
        super().__init__()

        self.main_menu = main_menu

        self.setWindowTitle("Play Screen")
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR};")

        # Create widgets
        self.label_score = QLabel("Score: 0")
        self.label_score.setFont(self.init_font())

        self.button_return_to_menu = self.style_button(QPushButton("Return to Menu", clicked=self.show_main_menu))
        self.button_retry = self.style_button(QPushButton("Retry", clicked=self.retry))
        self.canvas_view = QGraphicsView()
        self.canvas_scene = QGraphicsScene()
        self.canvas_view.setScene(self.canvas_scene)

        # Set up the layout
        layout = QVBoxLayout(self)

        # Add score label to layout
        score_layout = QHBoxLayout()
        score_layout.addWidget(self.label_score, alignment=Qt.AlignCenter)
        layout.addLayout(score_layout)

        # Add return to menu and retry buttons to layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_return_to_menu, alignment=Qt.AlignLeft)
        button_layout.addWidget(self.button_retry, alignment=Qt.AlignRight)
        layout.addLayout(button_layout)

        # Add canvas to layout
        layout.addWidget(self.canvas_view)

        # Center the window on the screen
        self.center_window()
        # Set fixed size to make the window not resizable
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        self.set_window_icon(self, ICON_PATH)

    def show_main_menu(self):
        # Add functionality to return to the main menu
        self.hide()
        self.main_menu.show()

    def retry(self):
        # Add functionality to retry the game
        pass
