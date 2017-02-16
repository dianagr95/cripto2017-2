#!/usr/bin/python

import numpy as np
import sys

class XOR:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.relleno = "beetlejuice"
        
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

    
    def xor_(self):
        A = bytearray(self.A)
        B = bytearray(self.B)
        A, B = self.emparejar(A,B)
        size = len(A)
        C = bytearray(size)
        for i in xrange(size):
            C[i] = A[i] ^ B[i]
        return C
        
            
    def getGrado(self, i):
        g = 0
        while i > 1:
            i >>= 1
            g += 1
        return g
    
    def mod(self, a):
        pol = int("100011011",2)
        g = self.getGrado(a)
        while g >= 8:
            aux = 0
            if a & (1 << g):
                aux = 1 << g - 8
            aux = self.mul(pol, aux)
            a ^= aux
            g = self.getGrado(a)
        return a
    
    def mul(self, pol, b):
        res = 0
        i = 1
        grado = self.getGrado(pol) + 1
        for x in xrange(grado):
            if pol & i:
                res ^= b << x
            i <<= 1
        return res
        
    def multiplicacion_(self):
        A = bytearray(self.A)
        pol = int("AA", 16)
        C = bytearray()
        for a in A:
            C.append(self.mod(self.mul(pol, a)))
        return C
    
