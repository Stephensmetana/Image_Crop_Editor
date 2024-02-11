import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from image_loader import ImageLoader
from side_menu import SideMenu

class ImageCropEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize UI components
        self.init_ui()

    def init_ui(self):
        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create layouts for the main window
        main_layout = QHBoxLayout(central_widget)

        # Create an image loader and side menu
        self.image_loader = ImageLoader()
        self.side_menu = SideMenu(self.image_loader)

        # Add image loader and side menu to the main layout
        main_layout.addWidget(self.side_menu)
        main_layout.addWidget(self.image_loader)

        # Set window properties
        self.setWindowTitle('ICE: Image Crop Editor')
        self.setGeometry(100, 100, 800, 600)


def main():
    app = QApplication(sys.argv)
    editor = ImageCropEditor()
    editor.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
