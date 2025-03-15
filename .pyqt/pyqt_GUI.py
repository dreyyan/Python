import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Python GUI") # Window Title
        self.setGeometry(700, 300, 500, 500) # Dimensions

def main():
    app = QApplication(sys.argv) # Create Instance of QAppplication
    window = MainWindow() # Create Instance Main Window
    window.show() # Display Main Window
    sys.exit(app.exec()) # Waits for User Interaction

if __name__ == "__main__": # If Script is Run Directly
    main() # Call Main
