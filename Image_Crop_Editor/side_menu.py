from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from image_loader import ImageLoader
from file_operations import open_file_explorer

class SideMenu(QWidget):
    def __init__(self, image_loader, parent=None):
        super().__init__(parent)

        self.image_loader = image_loader

        # Create a layout for the side menu
        layout = QVBoxLayout(self)

        # Create a button to open file explorer
        self.open_button = QPushButton('Open File Explorer', self)
        self.open_button.clicked.connect(self.open_file_explorer)
        layout.addWidget(self.open_button)

        # Create a button to display the image at full size
        self.full_size_button = QPushButton('Full Size', self)
        self.full_size_button.clicked.connect(self.show_full_size)
        layout.addWidget(self.full_size_button)

        # Create a button to fit the image to the window
        self.fit_to_window_button = QPushButton('Fit Image to Window', self)
        self.fit_to_window_button.clicked.connect(self.fit_to_window)
        layout.addWidget(self.fit_to_window_button)

        # Create a button to open the last directory
        self.open_last_directory_button = QPushButton("Open Last Directory", self)
        self.open_last_directory_button.clicked.connect(self.open_last_directory)
        layout.addWidget(self.open_last_directory_button)

        # Create a button to save image
        self.save_image_overwrite_button = QPushButton("Save (Overwrite)", self)
        self.save_image_overwrite_button.clicked.connect(self.save_image_overwrite)
        layout.addWidget(self.save_image_overwrite_button)

        # Create a button to save image as a new file
        self.save_image_as_new_button = QPushButton("Save as New", self)
        self.save_image_as_new_button.clicked.connect(self.save_image_as_new)
        layout.addWidget(self.save_image_as_new_button)


    def open_file_explorer(self):
        open_file_explorer(self, self.image_loader)

    def show_full_size(self):
        # Show the image at full size
        self.image_loader.show_full_size()

    def fit_to_window(self):
        # Fit the image to the window
        self.image_loader.fit_to_window()

    def open_last_directory(self):
        # Open file dialog to select the last opened directory
        self.image_loader.open_last_directory()
        
    def save_image_overwrite(self):
        # Overwrite existing file with this changed file
        print("Placeholder Button")
        
    def save_image_as_new(self):
        # Open file dialog to save the file as a new file
        print("Placeholder Button")

