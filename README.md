# Snake
Snake is a classic arcade game where players control a growing snake, navigating through a confined space to consume food and extend its length. The challenge lies in avoiding collisions with the snake's own body and the game boundaries.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/paullab321/Snake.git
    ```

2. Install the required dependencies:
  - Qt for Python:
    ### Creating and activating an environment You can do this by running the following on a terminal: 
    - Create environment (Your Python executable might be called python3):
    ```bash
    python -m venv env 
    ```
    - Activate the environment (Linux and macOS):
    ```bash
    source env/bin/activate
    ```
    - Activate the environment (Windows):
    ```bash
    env\Scripts\activate.bat 
    ```
  - Installing PySide6
    - For the latest version: 
    ```bash
    pip install pyside6 
    ```
  - Test your installation
    ```bash
    import PySide6.QtCore

    # Prints PySide6 version
    print(PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print(PySide6.QtCore.__version__) 
    ```

    
