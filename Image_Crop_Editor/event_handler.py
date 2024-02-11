from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QPointF


def wheelEvent(self, event):
    # Zoom in or out with the scroll wheel
    factor = 1.2  # Adjust the zoom factor as needed
    if event.angleDelta().y() > 0:
        self.image_view.scale(factor, factor)
    else:
        self.image_view.scale(1.0 / factor, 1.0 / factor)
    event.accept()


def mousePressEvent(self, event):
    # Store the initial position when the mouse button is pressed
    if event.button() == Qt.LeftButton:
        self.last_pos = event.pos()
        print("Mouse Pressed at:", self.last_pos)

def mouseMoveEvent(self, event):
    # Pan the image when the mouse is moved with the left button pressed
    if hasattr(self, 'last_pos') and event.buttons() & Qt.LeftButton:
        delta = event.pos() - self.last_pos
        self.last_pos = event.pos()

        # Map the delta to the scene coordinates
        mapped_delta = self.mapToScene(delta) - self.mapToScene(QPointF(0, 0))
        self.translate(mapped_delta.x(), mapped_delta.y())
        print("Mouse Moved, Delta:", delta, "Mapped Delta:", mapped_delta)

def mouseReleaseEvent(self, event):
    # Clear the stored position when the mouse button is released
    if hasattr(self, 'last_pos') and event.button() == Qt.LeftButton:
        del self.last_pos
        print("Mouse Released")