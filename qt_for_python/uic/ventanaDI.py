# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\ciencias 2.2\dispersionES\ventanaDI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qt_for_python.rcc.source import*


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 449)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
                                 "\n"
                                 "     background-image: url(:/image/imagenes/456.jpg);\n"
                                 "     font-family:     Comic Sans MS;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "   background:#2d89ef;\n"
                                 "   color: white;\n"
                                 "   border: 2px solid;\n"
                                 "   border-radius:15px;\n"
                                 "   font-size:15px;        \n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "  background:white;\n"
                                 "  color:black;    \n"
                                 "  border: 2px solid;\n"
                                 "  border-radius:15px;    \n"
                                 "  font-size:13px;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#contenedor{\n"
                                 "    border:transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView {\n"
                                 "    color: white;\n"
                                 "    font-size:15px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView{\n"
                                 "  qproperty-defaultAlignment: AlignHCenter;\n"
                                 "  background: rgb(59, 89, 213);\n"
                                 " font-weight: bold;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.boton_dispersar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dispersar.setGeometry(QtCore.QRect(640, 60, 91, 31))
        self.boton_dispersar.setObjectName("boton_dispersar")
        self.text_ingresar = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar.setGeometry(QtCore.QRect(320, 40, 311, 31))
        self.text_ingresar.setObjectName("text_ingresar")
        self.contenedor = QtWidgets.QWidget(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(30, 210, 681, 231))
        self.contenedor.setObjectName("contenedor")
        self.tabWidget = QtWidgets.QTabWidget(self.contenedor)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 681, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.TablaGcursor = QtWidgets.QTableWidget(self.tab)
        self.TablaGcursor.setGeometry(QtCore.QRect(40, 0, 601, 201))
        self.TablaGcursor.setObjectName("TablaGcursor")
        self.TablaGcursor.setColumnCount(0)
        self.TablaGcursor.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TablaCursor = QtWidgets.QTableWidget(self.tab_2)
        self.TablaCursor.setGeometry(QtCore.QRect(0, 0, 681, 201))
        self.TablaCursor.setObjectName("TablaCursor")
        self.TablaCursor.setColumnCount(0)
        self.TablaCursor.setRowCount(0)
        self.TablaCursor.horizontalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.boton_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_eliminar.setGeometry(QtCore.QRect(170, 80, 121, 31))
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.text_ingresar_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar_2.setGeometry(QtCore.QRect(320, 80, 311, 31))
        self.text_ingresar_2.setObjectName("text_ingresar_2")
        self.text_ingresar_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar_3.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.text_ingresar_3.setObjectName("text_ingresar_3")
        self.text_crear = QtWidgets.QLineEdit(self.centralwidget)
        self.text_crear.setGeometry(QtCore.QRect(40, 40, 111, 31))
        self.text_crear.setObjectName("text_crear")
        self.boton_crear = QtWidgets.QPushButton(self.centralwidget)
        self.boton_crear.setGeometry(QtCore.QRect(170, 40, 121, 31))
        self.boton_crear.setObjectName("boton_crear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_dispersar.setText(_translate("MainWindow", "Dispersar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("MainWindow", "Tab 2"))
        self.boton_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.boton_crear.setText(_translate("MainWindow", "Crear"))
        self.label.setText(_translate("MainWindow", "Disponible:"))
