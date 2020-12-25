from PyQt5 import QtWidgets, uic
import sys
import photo_rc
import pickle
import numpy as np
from PyQt5.QtWidgets import QMessageBox



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(lambda: self.Handel_buttons())
        self.show()

     
    def Handel_buttons (self):
        age=float(self.lineEdit_1.text())
        
        Gender= self.lineEdit_2.text().lower()
        if Gender == "male" :
            Gender = 1
        elif Gender == "female"  :
            Gender = 0

        Total_Bilirubin = float(self.lineEdit_3.text())
        Direct_Bilirubin = float(self.lineEdit_4.text())
        Alkaline_Phosphotase = float(self.lineEdit_5.text())
        Alamine_Aminotransferase = float(self.lineEdit_6.text())
        Aspartate_Aminotransferase = float(self.lineEdit_7.text())
        Total_Protiens = float(self.lineEdit_8.text())
        Albumin = float(self.lineEdit_9.text())
        Albumin_and_Globulin_Ratio = float(self.lineEdit_10.text())


        clf = pickle.load(open(r"F:\python ml\projects\Liver Disease\liversavemo.pkl","rb"))
        test = np.array([[age,   Gender ,Total_Bilirubin,    Direct_Bilirubin ,   Alkaline_Phosphotase ,   Alamine_Aminotransferase,    Aspartate_Aminotransferase,   Total_Protiens, Albumin,Albumin_and_Globulin_Ratio ]])
        predicition = clf.predict(test)



        if predicition == 1:
            QMessageBox.about(self, "The result", "you are diganosed with liver deise")
           
        elif predicition==2:
            QMessageBox.about(self, "The result", "you are fine")
        
            

        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()