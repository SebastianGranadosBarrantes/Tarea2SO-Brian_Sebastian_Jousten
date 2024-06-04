# Form implementation generated from reading ui file 'mainInterface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1353, 652)
        MainWindow.setStyleSheet("\n"
"QWidget {\n"
"    background-color: #000000;\n"
"}\n"
"\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"     background-color: rgb(128, 128, 128);\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #afff7e;  /* Color de fondo */\n"
"    color: #0000;  /* Color del texto */\n"
"    border: 2px solid #ffbc37;  /* Borde con grosor de 2px y color */\n"
"    border-radius: 10px;  /* Esquinas redondeadas */\n"
"    padding: 5px;  /* Espaciado interno */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;  /* Color de fondo al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1abc9c;  /* Color de fondo al hacer clic */\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #f0f0f0;  /* Color de fondo del QTableWidget */\n"
"    gridline-color: #d3d3d3;  /* Color de las líneas de la cuadrícula */\n"
"    border: 1px solid #d3d3d3;  /* Borde del QTableWidget */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #ffffff;  /* Color de fondo de los ítems (celdas) */\n"
"    color: #000000;  /* Color del texto de los ítems */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #3399ff;  /* Color de fondo de las celdas seleccionadas */\n"
"    color: #ffffff;  /* Color del texto de las celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: #cccccc;  /* Color de fondo de los encabezados */\n"
"    color: #000000;  /* Color del texto de los encabezados */\n"
"    padding: 4px;\n"
"    border: 1px solid #d3d3d3;  /* Borde de los encabezados */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    outline: none;  /* Eliminar el borde por defecto al enfocarse en una celda */\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 251, 226))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tfPrincipalMemorySize = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.tfPrincipalMemorySize.setObjectName("tfPrincipalMemorySize")
        self.verticalLayout.addWidget(self.tfPrincipalMemorySize)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tfSecondaryMemorySize = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.tfSecondaryMemorySize.setObjectName("tfSecondaryMemorySize")
        self.verticalLayout.addWidget(self.tfSecondaryMemorySize)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tfPagesSize = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.tfPagesSize.setObjectName("tfPagesSize")
        self.verticalLayout.addWidget(self.tfPagesSize)
        self.label_16 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.btnSetParameters = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnSetParameters.setObjectName("btnSetParameters")
        self.verticalLayout.addWidget(self.btnSetParameters)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 0, 251, 238))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.tfProcessName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.tfProcessName.setObjectName("tfProcessName")
        self.verticalLayout_3.addWidget(self.tfProcessName)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.tfProcessSize = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget_2)
        self.tfProcessSize.setObjectName("tfProcessSize")
        self.verticalLayout_3.addWidget(self.tfProcessSize)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.cmbType = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.cmbType.setObjectName("cmbType")
        self.cmbType.addItem("")
        self.cmbType.addItem("")
        self.verticalLayout_3.addWidget(self.cmbType)
        self.btnCreateProccess = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnCreateProccess.setObjectName("btnCreateProccess")
        self.verticalLayout_3.addWidget(self.btnCreateProccess)
        self.btnGenerateRandom = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnGenerateRandom.setObjectName("btnGenerateRandom")
        self.verticalLayout_3.addWidget(self.btnGenerateRandom)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 791, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.btnPause = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnPause.setObjectName("btnPause")
        self.verticalLayout_2.addWidget(self.btnPause)
        self.btnDone = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnDone.setObjectName("btnDone")
        self.verticalLayout_2.addWidget(self.btnDone)
        self.lblActualProcess = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.lblActualProcess.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblActualProcess.setObjectName("lblActualProcess")
        self.verticalLayout_2.addWidget(self.lblActualProcess)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.vboxProcessTable = QtWidgets.QVBoxLayout()
        self.vboxProcessTable.setObjectName("vboxProcessTable")
        self.label_8 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.vboxProcessTable.addWidget(self.label_8)
        self.tbwProcess = QtWidgets.QTableWidget(parent=self.horizontalLayoutWidget)
        self.tbwProcess.setObjectName("tbwProcess")
        self.tbwProcess.setColumnCount(8)
        self.tbwProcess.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwProcess.setHorizontalHeaderItem(7, item)
        self.vboxProcessTable.addWidget(self.tbwProcess)
        self.horizontalLayout.addLayout(self.vboxProcessTable)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 410, 501, 191))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.tbwPrimaryMemory = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_5)
        self.tbwPrimaryMemory.setObjectName("tbwPrimaryMemory")
        self.tbwPrimaryMemory.setColumnCount(5)
        self.tbwPrimaryMemory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbwPrimaryMemory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwPrimaryMemory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwPrimaryMemory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwPrimaryMemory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwPrimaryMemory.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.tbwPrimaryMemory)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(520, 410, 461, 191))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_6)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.tbwSecondaryMemory = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_6)
        self.tbwSecondaryMemory.setObjectName("tbwSecondaryMemory")
        self.tbwSecondaryMemory.setColumnCount(5)
        self.tbwSecondaryMemory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbwSecondaryMemory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwSecondaryMemory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwSecondaryMemory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwSecondaryMemory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwSecondaryMemory.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tbwSecondaryMemory)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(570, 0, 160, 80))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_7)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.cmbSelectAlgorithm = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_7)
        self.cmbSelectAlgorithm.setObjectName("cmbSelectAlgorithm")
        self.cmbSelectAlgorithm.addItem("")
        self.cmbSelectAlgorithm.addItem("")
        self.cmbSelectAlgorithm.addItem("")
        self.cmbSelectAlgorithm.addItem("")
        self.verticalLayout_6.addWidget(self.cmbSelectAlgorithm)
        self.btnLauch = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLauch.setGeometry(QtCore.QRect(570, 90, 151, 24))
        self.btnLauch.setObjectName("btnLauch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Process simulator"))
        self.label_4.setText(_translate("MainWindow", "Machine parameters:"))
        self.label.setText(_translate("MainWindow", "Principal Memory"))
        self.label_2.setText(_translate("MainWindow", "Secondary Memory"))
        self.label_3.setText(_translate("MainWindow", "Pages size"))
        self.label_16.setText(_translate("MainWindow", "Al values most be a power of 2 "))
        self.btnSetParameters.setText(_translate("MainWindow", "Set"))
        self.label_5.setText(_translate("MainWindow", "Create Process/Sevice:"))
        self.label_6.setText(_translate("MainWindow", "Process/Service Name"))
        self.label_7.setText(_translate("MainWindow", "Process/Service size:"))
        self.label_10.setText(_translate("MainWindow", "Type"))
        self.cmbType.setItemText(0, _translate("MainWindow", "Process"))
        self.cmbType.setItemText(1, _translate("MainWindow", "Service"))
        self.btnCreateProccess.setText(_translate("MainWindow", "Create"))
        self.btnGenerateRandom.setText(_translate("MainWindow", "Generate random"))
        self.label_9.setText(_translate("MainWindow", "Alter process: "))
        self.btnPause.setText(_translate("MainWindow", "Pause"))
        self.btnDone.setText(_translate("MainWindow", "Done"))
        self.lblActualProcess.setText(_translate("MainWindow", "Actual process:"))
        self.label_8.setText(_translate("MainWindow", "Process:"))
        item = self.tbwProcess.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process Id"))
        item = self.tbwProcess.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tbwProcess.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tbwProcess.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Size "))
        item = self.tbwProcess.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Pages"))
        item = self.tbwProcess.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "State"))
        item = self.tbwProcess.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Pg pr memo"))
        item = self.tbwProcess.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Pg seco memo"))
        self.label_11.setText(_translate("MainWindow", "Principal Memory:"))
        item = self.tbwPrimaryMemory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address-Range"))
        item = self.tbwPrimaryMemory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Page #"))
        item = self.tbwPrimaryMemory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Execution Page #"))
        item = self.tbwPrimaryMemory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Process Id"))
        item = self.tbwPrimaryMemory.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Process Name"))
        self.label_12.setText(_translate("MainWindow", "Secondary memory:"))
        item = self.tbwSecondaryMemory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address-Range"))
        item = self.tbwSecondaryMemory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Storage Number"))
        item = self.tbwSecondaryMemory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Id"))
        item = self.tbwSecondaryMemory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Process Name"))
        item = self.tbwSecondaryMemory.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "# Page"))
        self.label_13.setText(_translate("MainWindow", "Define Algorithm"))
        self.cmbSelectAlgorithm.setItemText(0, _translate("MainWindow", "FIFO"))
        self.cmbSelectAlgorithm.setItemText(1, _translate("MainWindow", "SJF"))
        self.cmbSelectAlgorithm.setItemText(2, _translate("MainWindow", "HRRN"))
        self.cmbSelectAlgorithm.setItemText(2, _translate("MainWindow", "PRIORITY"))
        self.btnLauch.setText(_translate("MainWindow", "Lauch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
