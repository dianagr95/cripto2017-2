#!/usr/bin/python

import numpy as np
import sys

class XOR:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.relleno = "beetlejuice"
        self.xAA = 170
        self.x03010102 = "??"
    
    def emparejar(self,auxA,auxB):
        A = bytearray()
        B = bytearray()
        for a in auxA:
            A.append(a)
        for b in auxB:
            B.append(b)
        relleno = bytearray(self.relleno,"utf-8") 
        diff = len(A) - len(B)
        s = len(relleno)
        index = 0
        while(diff != 0):
            if diff < 0:
                if diff + s < 0:
                    A = A + relleno
                else:
                    A = A + relleno[:diff%s]
            else:
                if diff - s > 0:
                    B = B + relleno
                else:
                    B = B + relleno[:diff%s]
            diff = len(A) - len(B)
        print(diff)
        return A,B

    def xor_test(self):
        A = bytearray(self.A)
        size = len(A)
        C = bytearray(size)
        for i in xrange(size):
            C[i] = A[i] ^ 0
        return C
    
    def xor_(self):
        A = bytearray(self.A)
        B = bytearray(self.B)
        A, B = self.emparejar(A,B)
        size = len(A)
        C = bytearray(size)
        for i in xrange(size):
            C[i] = A[i] ^ B[i]
        return C
    
    def multiplicacion_(self):
        A = bytearray(self.A)
        size = len(A)
        print(type(A[0]))
        C = bytearray(size)
        for i in xrange(size):
            C[i] = A[i]
        return "WUt"
        
    def poli_(self):
        return "WUT"
        
        def get_grado(self, i):
        g = 0
        while i > 1:
            i >>= 1
            g += 1
        return g
    
    def redu(self, a):
        k = 0
        g = self.get_grado(a)
        while g >= 8:
            aux = 0
            if a & (1 << g):
                aux = 1 << g - 8
            aux = self.mult_aux(self.pol, aux)
            a ^= aux
            g = self.get_grado(a)
        return a
    
    def mult_aux(self, bmult, b):
        res = 0
        i = 1
        for x in range(self.get_grado(bmult) + 1):
            if bmult & i:
                res ^= b << x
            i <<= 1
        return res
    
    def mult(self):
        bmult = int("AA", 16)
        res = bytearray()
        i  = 0
        for b in self.bytesA:
            print(str(i) + " Byte origen: " + bin(self.bytesA[i]) + " Byte a muliplicar: " + bin(bmult))
            res.append(self.redu(self.mult_aux(bmult, b)))
            i += 1
        self.escribe_archivo("multiplicacion.out", res)
