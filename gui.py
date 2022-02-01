import sys
from PyQt5.QtGui import QTextOption 
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaDI import *
from logica import *;
#-------------------------------------
#------------- Interfaz---------------

class Ventana_principal(QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        #----------------------------
        self.setWindowTitle("DISPERSION")
        #--------------------------------
        self.ui.tabWidget.setTabText(0,"GRAFICA CURSOR")
        self.ui.tabWidget.setTabText(1,"CURSOR")
        #--------------------------------------------
        self.ui.text_crear.setAlignment(Qt.AlignHCenter)
        self.ui.text_ingresar_3.setAlignment(Qt.AlignHCenter)
        self.ui.text_crear.setClearButtonEnabled(True)
        self.ui.text_ingresar.setClearButtonEnabled(True)
        self.ui.text_ingresar_2.setClearButtonEnabled(True)
        self.ui.text_ingresar_3.setClearButtonEnabled(True)
        self.ui.boton_dispersar.setEnabled(False)
        self.ui.boton_eliminar.setEnabled(False)
        self.ui.text_ingresar.setEnabled(False)
        self.ui.text_ingresar_2.setEnabled(False)
        self.ui.text_ingresar_3.setEnabled(False)
        
        #-------------------------------------------
        self.ui.boton_dispersar.setStyleSheet("background:#9b9b9b;\n")
        self.ui.boton_eliminar.setStyleSheet("background:#9b9b9b;\n")
        self.ui.text_ingresar.setStyleSheet("background:#9b9b9b;\n")
        self.ui.text_ingresar_2.setStyleSheet("background:#9b9b9b;\n")
        self.ui.text_ingresar_3.setStyleSheet("background:#9b9b9b;\n")
        #-------------------------------------------
        self.ui.TablaGcursor.setColumnCount(3)
        self.ui.TablaCursor.setVisible(False)
        self.ui.TablaCursor.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.TablaGcursor.setVisible(False)
        self.ui.TablaGcursor.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def Get_modelo(self):
        return self.modelo

#--------------------------------------
#------------controlador---------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_crear.clicked.connect(lambda:self.ventana.Get_modelo().Crear())        
        self.ventana.ui.boton_dispersar.clicked.connect(lambda: self.ventana.Get_modelo().Dispersar())
        self.ventana.ui.boton_eliminar.clicked.connect(lambda: self.ventana.Get_modelo().Eliminar())
        
#---------------------------------------
#---------------Modelo-----------------
class Modelo ():
    def __init__(self) :
        self.ventana = Ventana_principal(self)
        self.matriz =None
        self.valores_in={}
        self.cabezalista=None
        self.cursor=None

    def Crear(self):
        self.primo=self.ventana.ui.text_crear.text()
        if  self.primo.isnumeric():
            self.primo=int(self.primo)
            self.ventana.ui.boton_dispersar.setEnabled(True)
            self.ventana.ui.boton_eliminar.setEnabled(True)
            self.ventana.ui.text_ingresar.setEnabled(True)
            self.ventana.ui.text_ingresar_2.setEnabled(True)
            self.ventana.ui.text_ingresar_3.setEnabled(True)
            self.ventana.ui.boton_dispersar.setStyleSheet("background:#2d89ef;\n")
            self.ventana.ui.boton_eliminar.setStyleSheet("background:#2d89ef;\n")
            self.ventana.ui.text_ingresar.setStyleSheet("background:white;\n")
            self.ventana.ui.text_ingresar_2.setStyleSheet("background:white;\n")
            self.ventana.ui.text_ingresar_3.setStyleSheet("background: white;\n")
        else:
            QMessageBox.warning(self.ventana,"     Advertencia    ","      El valor ingresado debe ser un numero       ")
        self.ventana.ui.text_crear.clear()
    

    def Dispersar(self):
        claves=self.ventana.ui.text_ingresar.text()
        nombres=self.ventana.ui.text_ingresar_2.text()
        if claves!='' and nombres !='':
            lista_claves = claves.split(',')
            lista_nombres = nombres.split(',')
            lista_claves =[int(i) for i in lista_claves]
            llaves=[]
            for i in range(len(lista_claves)):
                if  lista_claves[i] not in  llaves:
                    self.valores_in[lista_claves[i]]=lista_nombres[i]
                    llaves.append(lista_claves[i])
            self.cabezalista=cabeza_listas(self.primo,self.valores_in)
            tamaño=self.cabezalista.LLenar(llaves)
            self.cursor=Cursor(self.cabezalista.Get_Cabezalista())
            self.cursor.llenar_cursor(tamaño)
            self.Mostrar_tabla()
            self.Mostrar_simbolos()
            self.cursor.Mostrar_cursor()
            self.ventana.ui.label.setText('DISPONIBLE: '+str(self.cursor.Get_disponible()))


    def Eliminar (self):
        numero =self.ventana.ui.text_ingresar_3.text()
        if numero !='' and numero.isnumeric():
                numero=int(numero)
                if numero in list(self.valores_in.keys()):
                    pos,anteriorpos=self.cabezalista.Eliminar(None,self.cabezalista.Get_Cabezalista()[numero%self.primo],numero)
                    self.cursor.Eliminar(pos,anteriorpos)
                    self.Mostrar_tabla()
                    self.Mostrar_simbolos()
                    self.valores_in.pop(numero)
                else:
                    QMessageBox.warning(self.ventana,"     Advertencia    ","      El valor ingresado no se encuentra en la lista       ")
                          
        else:
            QMessageBox.warning(self.ventana,"     Advertencia    ","      El valor ingresado debe ser un numero       ")
        self.ventana.ui.text_ingresar_3.clear()    

    def Mostrar_simbolos(self):
        labels_en_y=[]
        if self.ventana.ui.TablaGcursor.rowCount()!=0:
            self.ventana.ui.TablaGcursor.clearContents()
            self.ventana.ui.TablaGcursor.setRowCount(0)
        self.ventana.ui.TablaGcursor.setHorizontalHeaderLabels(["   DISPERCION    ","     CABEZA     ","      LISTA      "])
        fila=0
        for i in self.cabezalista.imprimir():
            columna=0
            self.ventana.ui.TablaGcursor.insertRow(fila)
            for j in i :
                celda= QTableWidgetItem(str(j))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.TablaGcursor.setItem(fila,columna,celda)
                columna+=1
            fila+=1 
        for i in range(len(self.cabezalista.imprimir())+1):
            labels_en_y.append(str(i))
        self.ventana.ui.TablaGcursor.setVerticalHeaderLabels(labels_en_y)  
        self.ventana.ui.TablaGcursor.setVisible(True) 
        
 
    def Mostrar_tabla(self): 
        labels_en_x=[]
        if self.ventana.ui.TablaCursor.rowCount()!=0:
            self.ventana.ui.TablaCursor.clearContents()
            self.ventana.ui.TablaCursor.setRowCount(0)
            self.ventana.ui.TablaCursor.setColumnCount(0)
        for i in range(len(self.cursor.Get_matriz()[0])+4):
            self.ventana.ui.TablaCursor.insertColumn(i)
            self.ventana.ui.TablaCursor.setColumnWidth(i,48)
        if self.ventana.ui.TablaCursor.columnCount()>20:
             self.ventana.ui.TablaCursor.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
             self.ventana.ui.TablaCursor.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(self.cursor.Get_matriz())):
            self.ventana.ui.TablaCursor.insertRow(i)
            self.ventana.ui.TablaCursor.setRowHeight(i,48)    
        for i in range(len(self.cursor.Get_matriz())):
            for j in range(len(self.cursor.Get_matriz()[i])) :
                celda= QTableWidgetItem(str(self.cursor.Get_matriz()[i][j]))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.TablaCursor.setItem(i,j,celda)
        self.ventana.ui.TablaCursor.setVerticalHeaderLabels(["POSICION","LLAVE","NOMBRE","SIGUIENTE"])
        self.ventana.ui.TablaCursor.setVisible(True) 
        
 
    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
