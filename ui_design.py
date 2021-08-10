import pdb
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget
from image_download import download_image


output_Dir=None
class Ui_ImageDataSetCreator(QWidget):
    def setupUi(self, ImageDataSetCreator):
        ImageDataSetCreator.setObjectName("ImageDataSetCreator")
        ImageDataSetCreator.resize(638, 555)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageDataSetCreator.setWindowIcon(icon)
        ImageDataSetCreator.setWindowOpacity(1)
        self.label_seacrchQuery = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_seacrchQuery.setGeometry(QtCore.QRect(40, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_seacrchQuery.setFont(font)
        self.label_seacrchQuery.setObjectName("label_seacrchQuery")
        self.lineEdit_searchQuery = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_searchQuery.setGeometry(QtCore.QRect(140, 10, 271, 28))
        self.lineEdit_searchQuery.setAutoFillBackground(True)
        self.lineEdit_searchQuery.setObjectName("lineEdit_searchQuery")
        self.label_output_dir = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_output_dir.setGeometry(QtCore.QRect(40, 60, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_output_dir.setFont(font)
        self.label_output_dir.setObjectName("label_output_dir")
        self.pushButton_output_dir = QtWidgets.QPushButton(ImageDataSetCreator)
        self.pushButton_output_dir.setGeometry(QtCore.QRect(170, 60, 90, 28))
        self.pushButton_output_dir.setObjectName("pushButton_output_dir")
        self.pushButton_output_dir.clicked.connect(self.select_Dir)
        self.label_output_loc = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_output_loc.setGeometry(QtCore.QRect(280, 60, 291, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_output_loc.setFont(font)
        self.label_output_loc.setObjectName("label_output_loc")
        self.label_images_downloaded = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_images_downloaded.setGeometry(QtCore.QRect(40, 120, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_images_downloaded.setFont(font)
        self.label_images_downloaded.setObjectName("label_images_downloaded")
        self.spinBox_images_range = QtWidgets.QSpinBox(ImageDataSetCreator)
        self.spinBox_images_range.setGeometry(QtCore.QRect(230, 120, 71, 26))
        self.spinBox_images_range.setMinimum(100)
        self.spinBox_images_range.setMaximum(600)
        self.spinBox_images_range.setSingleStep(100)
        self.spinBox_images_range.setObjectName("spinBox_images_range")
        self.label_arrangemen_function = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_arrangemen_function.setGeometry(QtCore.QRect(190, 166, 181, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_arrangemen_function.setFont(font)
        self.label_arrangemen_function.setObjectName("label_arrangemen_function")
        self.checkBox_duplicate_images = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_duplicate_images.setGeometry(QtCore.QRect(50, 200, 181, 21))
        self.checkBox_duplicate_images.setObjectName("checkBox_duplicate_images")
        self.checkBox_rename_files = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_rename_files.setGeometry(QtCore.QRect(240, 200, 111, 21))
        self.checkBox_rename_files.setObjectName("checkBox_rename_files")
        self.checkBox_rename_files.stateChanged.connect(lambda:self.checkbox_rename(self.checkBox_frontal_face))
        self.label_data_extraction = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_data_extraction.setGeometry(QtCore.QRect(190, 240, 221, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_data_extraction.setFont(font)
        self.label_data_extraction.setObjectName("label_data_extraction")
        self.checkBox_frontal_face = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_frontal_face.setGeometry(QtCore.QRect(50, 260, 121, 21))
        self.checkBox_frontal_face.setObjectName("checkBox_frontal_face")
        self.checkBox_frontal_face.stateChanged.connect(lambda:self.checkbox_frontalFace(self.checkBox_frontal_face))
        self.label_data_Augmentation = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_data_Augmentation.setGeometry(QtCore.QRect(180, 330, 251, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_data_Augmentation.setFont(font)
        self.label_data_Augmentation.setObjectName("label_data_Augmentation")
        self.checkBox_resize = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_resize.setGeometry(QtCore.QRect(60, 490, 87, 21))
        self.checkBox_resize.setObjectName("checkBox_resize")
        self.checkBox_resize.stateChanged.connect(lambda:self.checkbox_resize(self.checkBox_resize))
        self.lineEdit_width = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_width.setEnabled(True)
        self.lineEdit_width.setGeometry(QtCore.QRect(210, 490, 81, 28))
        self.lineEdit_width.setAutoFillBackground(True)
        self.lineEdit_width.setObjectName("lineEdit_width")
        self.lineEdit_width.setEnabled(False)
        self.lineEdit_width.setMaxLength(3)
        self.lineEdit_height = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_height.setGeometry(QtCore.QRect(370, 490, 91, 28))
        self.lineEdit_height.setAutoFillBackground(True)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.lineEdit_height.setEnabled(False)
        self.lineEdit_height.setMaxLength(3)
        self.label_width = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_width.setGeometry(QtCore.QRect(160, 490, 41, 21))
        self.label_width.setObjectName("label_width")
        self.label_height = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_height.setGeometry(QtCore.QRect(320, 490, 41, 21))
        self.label_height.setObjectName("label_height")
        self.checkBox_grayscale = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_grayscale.setGeometry(QtCore.QRect(60, 460, 87, 21))
        self.checkBox_grayscale.setObjectName("checkBox_grayscale")
        self.checkBox_brightness = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_brightness.setGeometry(QtCore.QRect(210, 370, 87, 21))
        self.checkBox_brightness.setObjectName("checkBox_brightness")
        self.checkBox_channel_Shift = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_channel_Shift.setGeometry(QtCore.QRect(310, 370, 121, 21))
        self.checkBox_channel_Shift.setObjectName("checkBox_channel_Shift")
        self.checkBox_horizontal_Flip = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_horizontal_Flip.setGeometry(QtCore.QRect(440, 370, 131, 21))
        self.checkBox_horizontal_Flip.setObjectName("checkBox_horizontal_Flip")
        self.checkBox_height_width_Shift = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_height_width_Shift.setGeometry(QtCore.QRect(60, 400, 141, 21))
        self.checkBox_height_width_Shift.setObjectName("checkBox_height_width_Shift")
        self.checkBox_rotation = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_rotation.setGeometry(QtCore.QRect(60, 370, 87, 21))
        self.checkBox_rotation.setObjectName("checkBox_rotation")
        self.checkBox_laplace = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_laplace.setGeometry(QtCore.QRect(200, 460, 87, 21))
        self.checkBox_laplace.setObjectName("checkBox_laplace")
        self.checkBox_shear = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_shear.setGeometry(QtCore.QRect(210, 400, 87, 21))
        self.checkBox_shear.setObjectName("checkBox_shear")
        self.checkBox_zoom = QtWidgets.QCheckBox(ImageDataSetCreator)
        self.checkBox_zoom.setGeometry(QtCore.QRect(310, 400, 87, 21))
        self.checkBox_zoom.setObjectName("checkBox_zoom")
        self.label_note1 = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_note1.setGeometry(QtCore.QRect(10, 350, 581, 16))
        self.label_note1.setObjectName("label_note1")
        self.label_note2 = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_note2.setGeometry(QtCore.QRect(10, 430, 541, 20))
        self.label_note2.setObjectName("label_note2")
        self.label_scale_Factor = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_scale_Factor.setGeometry(QtCore.QRect(180, 260, 71, 21))
        self.label_scale_Factor.setObjectName("label_scale_Factor")
        self.label_min_Neighbors = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_min_Neighbors.setGeometry(QtCore.QRect(380, 260, 91, 20))
        self.label_min_Neighbors.setObjectName("label_min_Neighbors")
        self.label_min_Size = QtWidgets.QLabel(ImageDataSetCreator)
        self.label_min_Size.setGeometry(QtCore.QRect(180, 300, 71, 20))
        self.label_min_Size.setObjectName("label_min_Size")
        self.lineEdit_scale_Factor = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_scale_Factor.setGeometry(QtCore.QRect(260, 260, 81, 28))
        self.lineEdit_scale_Factor.setAutoFillBackground(True)
        self.lineEdit_scale_Factor.setObjectName("lineEdit_scale_Factor")
        self.lineEdit_scale_Factor.setEnabled(False)
        self.lineEdit_min_Neighbors = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_min_Neighbors.setGeometry(QtCore.QRect(480, 260, 81, 28))
        self.lineEdit_min_Neighbors.setAutoFillBackground(True)
        self.lineEdit_min_Neighbors.setObjectName("lineEdit_min_Neighbors")
        self.lineEdit_min_Neighbors.setEnabled(False)
        self.lineEdit_min_Size = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_min_Size.setGeometry(QtCore.QRect(260, 300, 81, 28))
        self.lineEdit_min_Size.setAutoFillBackground(True)
        self.lineEdit_min_Size.setObjectName("lineEdit_min_Size")
        self.lineEdit_min_Size.setEnabled(False)
        self.pushButton_submit = QtWidgets.QPushButton(ImageDataSetCreator)
        self.pushButton_submit.setGeometry(QtCore.QRect(530, 520, 90, 28))
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.pushButton_submit.clicked.connect(self.get_inputs)
        self.progressBar = QtWidgets.QProgressBar(ImageDataSetCreator)
        self.progressBar.setGeometry(QtCore.QRect(220, 530, 151, 21))
        self.progressBar.setMinimum(0)
        self.progressBar.setRange(0, 100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit_rename = QtWidgets.QLineEdit(ImageDataSetCreator)
        self.lineEdit_rename.setGeometry(QtCore.QRect(360, 200, 171, 21))
        self.lineEdit_rename.setAutoFillBackground(True)
        self.lineEdit_rename.setObjectName("lineEdit_rename")
        self.lineEdit_rename.setEnabled(False)
        self.retranslateUi(ImageDataSetCreator)
        QtCore.QMetaObject.connectSlotsByName(ImageDataSetCreator)

    def retranslateUi(self, ImageDataSetCreator):
        _translate = QtCore.QCoreApplication.translate
        ImageDataSetCreator.setWindowTitle(_translate("ImageDataSetCreator", "Image Data Set Creator"))
        self.label_seacrchQuery.setText(_translate("ImageDataSetCreator", "Search query"))
        self.label_output_dir.setText(_translate("ImageDataSetCreator", "Ouput Directory"))
        self.pushButton_output_dir.setText(_translate("ImageDataSetCreator", "Select"))
        self.label_output_loc.setText(_translate("ImageDataSetCreator", "ouput location"))
        self.label_images_downloaded.setText(_translate("ImageDataSetCreator", "Images to be downloaded"))
        self.label_arrangemen_function.setText(_translate("ImageDataSetCreator", "Data Arrangement functions"))
        self.checkBox_duplicate_images.setText(_translate("ImageDataSetCreator", "Delete Duplicate Images"))
        self.checkBox_rename_files.setText(_translate("ImageDataSetCreator", "Rename Files"))
        self.label_data_extraction.setText(_translate("ImageDataSetCreator", "Frontal Face Extraction Functions"))
        self.checkBox_frontal_face.setText(_translate("ImageDataSetCreator", "Frontal Face "))
        self.label_data_Augmentation.setText(_translate("ImageDataSetCreator", "Data Preprocessing  and Augmentation"))
        self.checkBox_resize.setText(_translate("ImageDataSetCreator", "Resize"))
        self.label_width.setText(_translate("ImageDataSetCreator", "Width"))
        self.label_height.setText(_translate("ImageDataSetCreator", "Height"))
        self.checkBox_grayscale.setText(_translate("ImageDataSetCreator", "Grayscale"))
        self.checkBox_brightness.setText(_translate("ImageDataSetCreator", "Brightness"))
        self.checkBox_channel_Shift.setText(_translate("ImageDataSetCreator", "Channel Shift"))
        self.checkBox_horizontal_Flip.setText(_translate("ImageDataSetCreator", "Horizontal Flip"))
        self.checkBox_height_width_Shift.setText(_translate("ImageDataSetCreator", "Height Width Shift"))
        self.checkBox_rotation.setText(_translate("ImageDataSetCreator", "Rotation"))
        self.checkBox_laplace.setText(_translate("ImageDataSetCreator", "Laplace"))
        self.checkBox_shear.setText(_translate("ImageDataSetCreator", "Shear"))
        self.checkBox_zoom.setText(_translate("ImageDataSetCreator", "Zoom"))
        self.label_note1.setText(_translate("ImageDataSetCreator", "* These function applies to random images and create new images in the same directory"))
        self.label_note2.setText(_translate("ImageDataSetCreator", "* These function applies to entire images and replaces the original image from directory"))
        self.label_scale_Factor.setText(_translate("ImageDataSetCreator", "scale_Factor"))
        self.label_min_Neighbors.setText(_translate("ImageDataSetCreator", "min_Neighbors"))
        self.label_min_Size.setText(_translate("ImageDataSetCreator", "min_Size"))
        self.pushButton_submit.setText(_translate("ImageDataSetCreator", "Submit"))
        
    def checkbox_frontalFace(self,b):
        if self.checkBox_frontal_face.isChecked()==True:
            self.lineEdit_min_Neighbors.setEnabled(True)
            self.lineEdit_scale_Factor.setEnabled(True)
            self.lineEdit_min_Size.setEnabled(True)
            self.lineEdit_min_Neighbors.setText('5')
            self.lineEdit_scale_Factor.setText('1.3')
            self.lineEdit_min_Size.setText('30')
        elif self.checkBox_frontal_face.isChecked()==False:
            self.lineEdit_min_Neighbors.setEnabled(False)
            self.lineEdit_scale_Factor.setEnabled(False)
            self.lineEdit_min_Size.setEnabled(False)
            frontalFace = True
            
    def checkbox_resize(self,b):
        if self.checkBox_resize.isChecked() == True:
            self.lineEdit_height.setEnabled(True)
            self.lineEdit_width.setEnabled(True)
            self.lineEdit_height.setText('200')
            self.lineEdit_width.setText('200')
        elif self.checkBox_resize.isChecked() == False:
            self.lineEdit_height.setEnabled(False)
            self.lineEdit_width.setEnabled(False)
    def checkbox_rename(self,b):
        if self.checkBox_rename_files.isChecked() == True:
            self.lineEdit_rename.setEnabled(True)
        elif self.checkBox_rename_files.isChecked() == False:
            self.lineEdit_rename.setEnabled(False)
    def select_Dir(self):
        while(True):
            global output_Dir
            output_Dir = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
            if(os.path.isdir(output_Dir) == False):
                QMessageBox.about(self, "Input Error", "Please select valid directory")
            else:
                break
        self.label_output_loc.setText(output_Dir)
        
    def get_inputs(self):
        global output_Dir
        search_query = self.lineEdit_searchQuery.text()
        scroll_Value = int(self.spinBox_images_range.value())//100
        if(output_Dir == None):
            QMessageBox.about(self, "Input Error", "Please select valid directory")
            self.progressBar.setFormat('Error-restart')
            pdb.set_trace()
        if(search_query == ''):
            QMessageBox.about(self, "Input Error", "Search query missing")
            self.progressBar.setFormat('Error-restart')
            pdb.set_trace()
        output_Dir = output_Dir + '/'
        self.progressBar.setValue(10)
        download_image(search_query,output_Dir,scroll_Value)
        self.progressBar.setValue(70)
        if self.checkBox_duplicate_images.isChecked() == True:
            from duplicate import remove_duplicates
            remove_duplicates(output_Dir)
        if self.checkBox_frontal_face.isChecked()==True:
            from face_extraction import face_extract
            minNieghbors = int(self.lineEdit_min_Neighbors.text())
            scaleFactor = float(self.lineEdit_scale_Factor.text())
            minSize = int(self.lineEdit_min_Size.text())
            face_extract(output_Dir,scaleFactor,minNieghbors,minSize)
        if self.checkBox_grayscale.isChecked() == True:
            from black_white import gray_scale
            gray_scale(output_Dir)
        if self.checkBox_laplace.isChecked() == True:
            from laplace import transform
            transform(output_Dir)            
        files = os.listdir(output_Dir)
        self.progressBar.setValue(75)
        if self.checkBox_brightness.isChecked() == True:
            from brightness import brightness_level
            brightness_level(files,output_Dir)
        if self.checkBox_channel_Shift.isChecked() == True:
            from channel_shift import ch_shift
            ch_shift(files,output_Dir)
        if self.checkBox_horizontal_Flip.isChecked() == True:
            from flip_horizontal import flip
            flip(files,output_Dir)
        if self.checkBox_rotation.isChecked() == True:
            from rotation import rotate
            rotate(files,output_Dir)
        if self.checkBox_shear.isChecked() == True:
            from  shear import shear_intensity
            shear_intensity(files,output_Dir)
        self.progressBar.setValue(80)
        if self.checkBox_zoom.isChecked() == True:
            from zoom import zoom_in
            zoom_in(files,output_Dir)
        self.progressBar.setValue(85)
        if self.checkBox_height_width_Shift.isChecked() == True:
            from height_width_shift import shift
            shift(files,output_Dir)
        self.progressBar.setValue(90)
        if self.checkBox_resize.isChecked() == True:
            from resize import image_resize
            height = int(self.lineEdit_height.text())
            width = int(self.lineEdit_width.text())
            image_resize(output_Dir,width,height)
        self.progressBar.setValue(95)
        if self.checkBox_rename_files.isChecked() == True:
            from rename_files import rename_file
            fname = self.lineEdit_rename.text()
            rename_file(output_Dir,fname,search_query)
        self.progressBar.setValue(100)
        self.progressBar.setFormat('Completed')
         
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ImageDataSetCreator = QtWidgets.QDialog()
    ui = Ui_ImageDataSetCreator()
    ui.setupUi(ImageDataSetCreator)
    ImageDataSetCreator.show()
    sys.exit(app.exec_())
