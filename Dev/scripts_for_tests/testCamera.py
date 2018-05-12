"""from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(20)
camera.stop_preview()
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&Submit")

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """
    # import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainGUI(object):
    def setupUi(self, MainGUI):
        MainGUI.setObjectName("Photobooth")
        MainGUI.resize(824, 654)
        self.centralWidget = QtWidgets.QWidget(MainGUI)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_image = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_image.setObjectName("graphicsView_image")
        self.verticalLayout.addWidget(self.graphicsView_image)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.line_textPhoto = QtWidgets.QLineEdit(self.centralWidget)
        self.line_textPhoto.setObjectName("line_textPhoto")
        self.horizontalLayout_2.addWidget(self.line_textPhoto)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.line_sendEmail = QtWidgets.QLineEdit(self.centralWidget)
        self.line_sendEmail.setObjectName("line_sendEmail")
        self.horizontalLayout_3.addWidget(self.line_sendEmail)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_prev = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_prev.setObjectName("pushButton_prev")
        self.horizontalLayout.addWidget(self.pushButton_prev)
        self.pushButton_next = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_takephoto = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_takephoto.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_takephoto.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_takephoto.setObjectName("pushButton_takephoto")
        self.horizontalLayout_4.addWidget(self.pushButton_takephoto)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainGUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainGUI)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menuBar.setObjectName("menuBar")
        MainGUI.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainGUI)
        self.mainToolBar.setObjectName("mainToolBar")
        MainGUI.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainGUI)
        self.statusBar.setObjectName("statusBar")
        MainGUI.setStatusBar(self.statusBar)
        
        #initialize the camera and grab a reference to the raw camera capture
      camera = PiCamera()
       camera.resolution = (640,480)
        camera.framerate = 32
         rawCapture = PiRGBArray(camera, size=(640, 480)
                
    time.sleep(0.1)
    
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      # grab the raw NumPy array representing the image, then initialize the timestamp
      # and occupied/unoccupied text
        image = frame.array
      
           scene = QGraphicsScene(self)
        scene.addPixmap(QPixmap.fromImage(qimage2ndarray.array2qimage(frame)))
         self.graphicsView.setScene(scene)

        self.retranslateUi(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)
        
        
    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.pushButton_next.clicked.connect(self.handle_trigger)


    def handle_trigger(self):
        # Show that the slot has been called.

        print("trigger signal received")
  
  
    def retranslateUi(self, MainGUI):
        _translate = QtCore.QCoreApplication.translate
        MainGUI.setWindowTitle(_translate("MainGUI", "MainGUI"))
        self.label.setText(_translate("MainGUI", "Texte : "))
        self.pushButton_4.setText(_translate("MainGUI", "Envoyer par mail : "))
        self.pushButton_prev.setText(_translate("MainGUI", "<< Prev "))
        self.pushButton_next.setText(_translate("MainGUI", "Next >>"))
        self.pushButton_takephoto.setText(_translate("MainGUI", "Photo !!!"))
        
        self.connect_and_emit_trigger()
  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGUI = QtWidgets.QMainWindow()
    ui = Ui_MainGUI()
    ui.setupUi(MainGUI)
    
    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    darkPalette = QtGui.QPalette()
    darkPalette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    darkPalette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.Base, QtGui.QColor(25,25,25))
    darkPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    darkPalette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.Text, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    darkPalette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255,255,255))
    darkPalette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    darkPalette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0,0,0))
    app.setPalette(darkPalette)
    #MainGUI.showFullScreen()
    MainGUI.show()
    
    sys.exit(app.exec_())



"""
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  # grab the raw NumPy array representing the image, then initialize the timestamp
  # and occupied/unoccupied text
  image = frame.array
    #imageQt = QImage(cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB), frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
    #label.setPixmap(QPixmap.fromImage(imageQt)) 
 
  # show the frame
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF
 
  # clear the stream in preparation for the next frame
  rawCapture.truncate(0)
 
  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break"""
"""