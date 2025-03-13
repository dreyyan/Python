from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon # Icons
from PyQt5.QtGui import QFont # Fonts
from PyQt5.QtGui import QPixmap # Pixmap
from PyQt5.QtCore import Qt # Alignment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centered Scaled Pixmap")
        self.setGeometry(700, 300, 500, 500) # Dimensions
        self.setWindowIcon(QIcon("C:\\Users\\Drei\\Downloads\\.img\\python.png"))

        label = QLabel("PYTHON GUI", self) # Add Label
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Times New Roman", 40)) # Add Label Font
        label.setGeometry(0, 0, 500, 100) # Set Label Size
        label.setStyleSheet("color: #162a8c;" # Set Label Color
                            "background-color: #d9d92e;" # Set Label Background
                            "font-weight: bold;")

        label = QLabel(self) # Create Label
        pixmap = QPixmap(r"C:\Users\Drei\Downloads\.img\python.png") # Pixmap(Picture)

        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation) # Scaled Pixmap
        label.setPixmap(scaled_pixmap)

        label.setAlignment(Qt.AlignCenter) # Center Pixmap within Label

        layout = QVBoxLayout() # Create Layout
        layout.addWidget(label, alignment=Qt.AlignCenter) # Add Label

        central_widget = QWidget(self) # Set Center Widget
        central_widget.setLayout(layout) # Layout
        self.setCentralWidget(central_widget)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
