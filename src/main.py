from PySide6.QtWidgets import QApplication, QWidget

import sys

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()

    app.exec()

main()
