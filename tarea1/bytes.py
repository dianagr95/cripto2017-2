#!/usr/bin/python

from fileManager import FileManager
from xor import XOR

import sys

file_name1 = "xor.out"
file_name2 = "multiplicacion.out"
file_name3 = "multiplicacion_poli.out"

def main(args):
    fileM = FileManager()
    
    data1 = fileM.loadFile(args[0])

    data2 = fileM.loadFile(args[1])
    
    xor = XOR(data1,data2)
    
    #Ejercicio 1-a
    
    dataR = xor.xor_()
    fileM.saveFile(file_name1,dataR)

    #Ejercicio 1-b
    
    dataR = xor.multiplicacion_()
    fileM.saveFile(file_name2,dataR)
    
    #Ejercicio 1-c
    
    dataR = xor.poli_()
    fileM.saveFile(file_name3,dataR)
    
if __name__ == "__main__":
    main(sys.argv[1:])
