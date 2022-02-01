from re import S
from typing import TextIO
import numpy as np
class Cabeza :
    def __init__(self,Posiscion,llave,nombre):
        self.posicion=Posiscion 
        self.llave=llave
        self.nombre=nombre
        self.siguiente=None

    def Agregar(self,clave,posicion,nombre):
        if self.siguiente==None:
            self.siguiente=Cabeza(posicion,clave,nombre)
        else:
            self.siguiente.Agregar(clave,posicion,nombre)    
        
    def Imprimir(self):
        if self.siguiente==None:
            return str(self.llave)
        else:
            return str(self.llave)+ '->' + self.siguiente.Imprimir()    

    def Get_llave(self):
        return self.llave

    def Set_siguiente(self,siguiente):
        self.siguiente=siguiente

    def Get_poscion(self):
        return self.posicion        
     
class cabeza_listas:
    def __init__(self,primo,diccionario):
       self.lista=[]
       self.diccionario=diccionario
       self.tamaño=primo
       self.crear()

    def crear(self):
        for i in range(self.tamaño):
            self.lista.append(-1)

    def LLenar (self,llaves):
        pos=0
        for i in llaves:
            if self.lista[i%self.tamaño] ==-1:
                pos+=1
                self.lista[i%self.tamaño]= Cabeza(pos,i,self.diccionario[i])     
            else:
                pos+=1
                self.lista[i%self.tamaño].Agregar(i,pos,self.diccionario[i])
        return pos
     
    def Eliminar(self,anterior,valor,numero):
        if valor.Get_llave()==numero:
            aux=None
            if anterior!=None:
                anterior.Set_siguiente(valor.siguiente)
                aux=anterior
            else:
                self.lista[self.lista.index(valor)]=valor.siguiente
            return valor.Get_poscion(),aux   
        else:
            return self.Eliminar(valor,valor.siguiente,numero)


    def imprimir(self):
        matriz=[]
        fila=0
        for i in self.lista:
            if i!=-1 and i!=None: 
                palabra=str(fila)+','+str(i.Get_poscion())+','+i.Imprimir()
                aux=palabra.split(',')
                matriz.append(aux)
            fila+=1
        return matriz
            
    def Get_Cabezalista(self):
        return self.lista

class Cursor:
    def __init__(self,cabeza_lista):
        self.cabezalista=cabeza_lista
        self.cursor=[]
        self.disponible=[]
        
    def llenar_cursor(self,tamaño):
        for i in range(4):
            aux=[]
            for j in range(tamaño):
                aux.append(0)
            self.cursor.append(aux)
        for i in self.cabezalista:
            if i!=-1 :
                self.recorer(i)
    
    def recorer(self,valor):
        if  valor!=None:
            if valor.siguiente!=None:
                self.cursor[0][valor.Get_poscion()-1]=valor.Get_poscion()
                self.cursor[1][valor.Get_poscion()-1]=valor.Get_llave()
                self.cursor[2][valor.Get_poscion()-1]=valor.nombre
                self.cursor[3][valor.Get_poscion()-1]=valor.siguiente.Get_poscion()          
            else:
                self.cursor[0][valor.Get_poscion()-1]=valor.Get_poscion()
                self.cursor[1][valor.Get_poscion()-1]=valor.Get_llave()
                self.cursor[2][valor.Get_poscion()-1]=valor.nombre
                self.cursor[3][valor.Get_poscion()-1]=0
            self.recorer(valor.siguiente) 

    def Eliminar(self,pos,anterior):
        self.disponible.append(pos)
        self.cursor[1][pos-1]='-'
        self.cursor[2][pos-1]='-'
        self.cursor[3][pos-1]='-'
        if anterior!=None:
            self.cursor[1][anterior.Get_poscion()-1]=anterior.Get_llave()
            self.cursor[2][anterior.Get_poscion()-1]=anterior.nombre
            if anterior.siguiente!=None:
                self.cursor[3][anterior.Get_poscion()-1]=anterior.siguiente.Get_poscion()
            else:    
                self.cursor[3][anterior.Get_poscion()-1]=0


    def Mostrar_cursor(self):
        for i in self.cursor:
            for j in  i:
                print(j,end=" ")
            print()     

    def Get_matriz(self):
        return self.cursor
        
    def Get_disponible(self):
        return self.disponible[len(self.disponible)-1]

if __name__ =="__main__":
    prueba=cabeza_listas(23)
    archivo=open('prueba.txt')
    entrada=archivo.readlines()
    entrada=entrada[3].split(',')
    valor_duplicado=[]
    llaves=[]
    for i in range(len(entrada)):
        if int(entrada[i]) in llaves:
          valor_duplicado.insert(0,i)
        else:
            llaves.append(int(entrada[i]))
    tamaño=prueba.LLenar(llaves)
    prueba.imprimir()
    cur=Cursor(prueba.Get_Cabezalista())
    cur.llenar_cursor(tamaño)
    numero=91
    pos=prueba.Eliminar(None,prueba.Get_Cabezalista()[numero%23],91)
    print("nslkdjcldskjckl",pos)
    prueba.imprimir()
    cur.Mostrar_cursor()




            





