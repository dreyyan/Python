import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel # Widgets
from PyQt5.QtGui import QIcon # Icons
from PyQt5.QtGui import QFont # Fonts
from PyQt5.QtCore import Qt # Alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Python GUI") # Window Title
        self.setGeometry(700, 300, 500, 500) # Dimensions
        self.setWindowIcon(QIcon("C:\\Users\\Drei\\Downloads\\.img\\python.png"))

        label = QLabel("PYTHON GUI", self) # Add Label
        label.setFont(QFont("Times New Roman", 40)) # Add Label Font
        label.setGeometry(0, 0, 500, 100) # Set Label Size
        label.setStyleSheet("color: #162a8c;" # Set Label Color
                            "background-color: #dddddd;" # Set Label Background
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        # Alignments
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter)
        # SHORTCUT
        # label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

def main():
    app = QApplication(sys.argv) # Create Instance of QAppplication
    window = MainWindow() # Create Instance Main Window
    window.show() # Display Main Window
    sys.exit(app.exec()) # Waits for User Interaction

if __name__ == "__main__": # If Script is Run Directly
    main() # Call Main