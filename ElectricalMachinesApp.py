import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from ElectricalMachinesUI import *
import matplotlib.pyplot as plt
from pandas import *
from math import *

class ElectricalMachines(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.calculate.clicked.connect(self.IMCalculate)
        self.ui.reset.clicked.connect(self.IMReset)
        self.ui.exit.clicked.connect(self.exitapp)
        self.ui.opvsSpeed.clicked.connect(self.OPvsSpeed)
        self.ui.opvsslip.clicked.connect(self.OPvsSlip)
        self.ui.opvspf.clicked.connect(self.OPvsPowerFactor)
        self.ui.opvseff.clicked.connect(self.OPvsEfficiency)
        

        self.ui.SMCalculate.clicked.connect(self.SMcalc)
        self.ui.SMReset.clicked.connect(self.SMreset)
        self.ui.SMExit.clicked.connect(self.exitapp)
        self.ui.SMPLot.clicked.connect(self.smplot)

    def IMCalculate(self):
        Ns=1500
        Nr=float(self.ui.IMSpeed.text())
        slip=((Ns-Nr)/Ns)*100

        T=float(self.ui.IMTorque.text())
        Output_Power=(2*pi*Nr*T)/60

        Input_Power=float(self.ui.IMPower.text())
        Efficiency=(Output_Power/Input_Power)*100

        self.ui.label_3.setText(str('%.2f' %slip))
        self.ui.label_5.setText(str('%.2f' %Output_Power)+' Watts')
        self.ui.label_7.setText(str('%.2f' %Efficiency)+' %')
        
    def IMReset(self):
        self.ui.IMSpeed.clear()
        self.ui.IMTorque.clear()
        self.ui.IMPower.clear()
        self.ui.IMpf.clear()
        self.ui.label_3.clear()
        self.ui.label_5.clear()
        self.ui.label_7.clear()
         
    def exitapp(self):
        sys.exit()
        
    def OPvsSpeed(self):
        df=read_csv("E:\PYTHON\Python Projects\Induction Motor.csv")
        plt.plot(df['Output Power'], df['Speed'],label='Output Power vs Speed',color='#068CE9')
        plt.title('Characteristics of Induction Motor')
        plt.xlabel('Output in watts')
        plt.ylabel('Speed in RPM')
        plt.legend()
        plt.show()
    def OPvsSlip(self):
        df=read_csv("E:\PYTHON\Python Projects\Induction Motor.csv")
        plt.plot(df['Output Power'], df['Slip'],label='Slip vs Output Power',color='green')
        plt.title('Characteristics of Induction Motor')
        plt.xlabel('Output in watts')
        plt.ylabel('Slip')
        plt.legend()
        plt.show()

    def OPvsPowerFactor(self):
        df=read_csv("E:\PYTHON\Python Projects\Induction Motor.csv")
        plt.plot(df['Output Power'], df['Power Factor'],label='Power Factor vs Output Power',color='red')
        plt.title('Characteristics of Induction Motor')
        plt.xlabel('Output in watts')
        plt.ylabel('Power Factor')
        plt.legend()
        plt.show()
        
    def OPvsEfficiency(self):
        df=read_csv("E:\PYTHON\Python Projects\Induction Motor.csv")
        plt.plot(df['Output Power'], df['Efficiency'],label='Power Factor vs Output Power',color='orange')
        plt.title('Characteristics of Induction Motor')
        plt.xlabel('Output in watts')
        plt.ylabel('Efficiency in %')
        plt.legend()
        plt.show()

    def SMcalc(self):
        Torque=float(self.ui.SMTorque.text())
        Speed=float(self.ui.SMSpeed.text())
        Input_Power=float(self.ui.SMPower.text())
        LineCurrent=float(self.ui.SMLineCurrent.text())

        Output_Power=(2*pi*Speed*Torque)/60
        PowerFactor=Input_Power/(sqrt(3)*415*LineCurrent)
        Efficiency=(Output_Power/Input_Power)*100

        self.ui.label_27.setText(str('%.2f' %PowerFactor))
        self.ui.label_29.setText(str('%.2f' %Output_Power)+' Watts')
        self.ui.label_31.setText(str('%.2f' %Efficiency)+' %')
    def SMreset(self):
        self.ui.SMTorque.clear()
        self.ui.SMSpeed.clear()
        self.ui.SMLineCurrent.clear()
        self.ui.SMPower.clear()
    def smplot(self):
        df=read_csv("D:\Python\projects\Performance of Electrical Machines\Synchronous Motor.csv")
        plt.plot(df['Line Current'], df['Power Factor'],label='Line Current vs Power Factor',color='green')
        plt.title('Characteristics of Synchronous Motor')
        plt.xlabel('Line Current in Amps')
        plt.ylabel('Power Factor')
        plt.legend()
        plt.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = ElectricalMachines()
    w.show()
    sys.exit(app.exec_())
