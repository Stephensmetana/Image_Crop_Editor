from PyQt5.QtWidgets import QLabel, QGraphicsScene, QVBoxLayout, QGraphicsView, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QEvent, QFileInfo, QPointF
from event_handler import wheelEvent
from file_navigation import get_first_image_in_folder, get_next_image_in_folder, get_previous_image_in_folder
from file_operations import get_last_opened_directory, set_last_opened_directory


class ImageLoader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._folder_path = None
        self._image_path = None


        # Create a layout for the image loader
        layout = QVBoxLayout(self)

        # Create a scene for displaying images
        self.image_scene = QGraphicsScene()
        self.image_view = QGraphicsView(self)
        self.image_view.setScene(self.image_scene)

        layout.addWidget(self.image_view)

        # By default, shrink the image to fit the window
        self.image_view.setRenderHint(QPainter.Antialiasing, True)
        self.image_view.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.image_view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        
        # Disable the vertical and horizontal scroll bars
        self.image_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.image_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Connect mouse events
        self.setMouseTracking(True)

        # Install an event filter to capture key press events
        self.installEventFilter(self)
        self.image_view.wheelEvent = wheelEvent.__get__(self, QGraphicsView)

        # Connect the resize event to the custom method
        self.resizeEvent = self.custom_resize_event



    def load_image(self, image_path):
        # Load the image and display it in the scene
        pixmap = QPixmap(image_path)
        self.image_scene.clear()
        self.image_scene.addPixmap(pixmap)

        self.set_image_path(image_path)
        
        # Set the transformation to shrink the image to fit the window
        self.image_view.fitInView(self.image_scene.sceneRect(), Qt.KeepAspectRatio)
        self.image_view.setSceneRect(self.image_scene.itemsBoundingRect())

        # Automatically fit the image to the window
        self.fit_to_window()

    def show_full_size(self):
        # Show the image at full size
        self.image_view.resetTransform()

    def fit_to_window(self):        
        self.image_view.resetTransform()
        # Fit the image to the window
        self.image_view.fitInView(self.image_scene.sceneRect(), Qt.KeepAspectRatio)

    def eventFilter(self, source, event):
        # Handle key press events for right and left arrow keys
        if event.type() == QEvent.KeyRelease:
            if event.key() == Qt.Key_Right:
                self.load_next_image()
                return True
            elif event.key() == Qt.Key_Left:
                self.load_previous_image()
                return True
        return super().eventFilter(source, event)


    def load_next_image(self):
        current_image_path = self.get_image_path()
        folder_path = self.get_folder_path()
        next_image_path = get_next_image_in_folder(folder_path, current_image_path)
        if next_image_path:
            self.load_image(next_image_path)

    def load_previous_image(self):
        current_image_path = self.get_image_path()
        folder_path = self.get_folder_path()
        previous_image_path = get_previous_image_in_folder(folder_path, current_image_path)
        if previous_image_path:
            self.load_image(previous_image_path)

    def load_image_from_folder_dialog(self):
        # Open file dialog to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, 'Select a Folder')
        if folder_path:
            print(f"Selected folder path: {folder_path}")
            self.folder_path = folder_path  # Set the instance variable
            image_path = get_first_image_in_folder(folder_path)
            if image_path:
                self.load_image(image_path)

    
    def open_last_directory(self):
        # Open last opened directory
        last_opened_directory = get_last_opened_directory()
        if last_opened_directory:
            self.set_folder_path(last_opened_directory) 
            image_path = get_first_image_in_folder(last_opened_directory)
            if image_path:
                self.load_image(image_path)

    
    def custom_resize_event(self, event):
        # Handle custom logic when the window is resized
        if self.get_image_path():
            self.load_image(self.get_image_path())
        super().resizeEvent(event)
    
    # Getters and Setters
    def get_image_path(self):
        return self._image_path

    def set_image_path(self, image_path):
        self._image_path = image_path
    
    def get_folder_path(self):
        return self._folder_path

    def set_folder_path(self, folder_path):
        self._folder_path = folder_path