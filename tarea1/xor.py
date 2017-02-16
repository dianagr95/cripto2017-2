#!/usr/bin/python

import numpy as np
import sys

class XOR:
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.relleno = "beetlejuice"
        
    def emparejar(self,resA,resB):
        A = bytearray()
        B = bytearray()
        for a in resA:
            A.append(a)
        for b in resB:
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
        
            
    def getGrado(self, pol):
        grado = 0
        while pol > 1:
            pol = pol >> 1
            grado = grado + 1
        return grado
    
    def mod(self, mod):
        pol = int("100011011",2)
        grado = self.getGrado(mod)
        while g > 7:
            res = 0
            if mod & (1 << grado):
                res = 1 << grado - 8
            res = self.mul(pol, res)
            mod ^= res
            grado = self.getGrado(mod)
        return mod
    
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
    
