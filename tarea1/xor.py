#!/usr/bin/python

import numpy as np

class XOR:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.relleno = "bettlejuice"
    
    def emparejar(self):
        A = self.A[:-1]
        B = self.B[:-1]
        diff = len(A) - len(B)
        s = len(self.relleno)
        index = 0
        while(diff != 0):
            if diff < 0:
                if diff + s < 0:
                    A = A + self.relleno
                else:
                    A = A + self.relleno[index]
                    index = index + 1
            else:
                if diff - s > 0:
                    B = B + self.relleno
                else:
                    B = B + self.relleno[index]
                    index = index + 1
            diff = len(A) - len(B)
        print(diff)
        return A+self.A[-1],B+self.B[-1]
    
    def toInt(self,string):
        A = []
        size = len(string)
        i = 0
        while i < size:
            A.append(ord(string[i]))
            i = i + 1
        A = np.array(A)
        return A
            
    def toString(self,array):
        s = ""
        size = array.shape[0]
        i = 0
        while i < (size):
            s = s + chr(array[i])
            i = i + 1
        return s
    
    def xor_(self):
        A, B = self.emparejar()
        A = self.toInt(A)
        B = self.toInt(B)
        C = A ^ B
        C = self.toString(C)
        return C
        
    def multiplicacion_(self):
        return "WUT"
        
    def poli_(self):
        return "WUT"
        
