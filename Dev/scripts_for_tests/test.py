import cv2
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

class Capture():
  def __init__(self):
      self.capturing = False
      #initialize the camera and grab a reference to the raw camera capture
      
      self.camera = PiCamera()
      self.camera.resolution = (640,480)
      self.camera.framerate = 15
      self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
  
  def endCapture(self):
      print("pressed End")
      self.capturing = False
  
  def quitCapture(self):
      print("pressed Quit")
      cv2.destroyAllWindows()
      QtCore.QCoreApplication.quit()
  
  def startCapture(self):
      self.capturing = True
      for frame in self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True):
            """ grab the raw NumPy array representing the image, then initialize the timestamp
            and occupied/unoccupied text """
            image = frame.array
            cv2.imshow("Capture", image)
            cv2.waitKey(5)
  
      cv2.destroyAllWindows()


class Window(QWidget):
    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Control Panel')

        self.capture = Capture()
        self.start_button = QPushButton('Start',self)
        self.start_button.clicked.connect(self.capture.startCapture)

        self.end_button = QPushButton('End',self)
        self.end_button.clicked.connect(self.capture.endCapture)

        self.quit_button = QPushButton('Quit',self)
        self.quit_button.clicked.connect(self.capture.quitCapture)

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.end_button)
        vbox.addWidget(self.quit_button)

        self.setLayout(vbox)
        self.setGeometry(100,100,200,200)
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())