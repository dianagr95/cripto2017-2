#!/usr/bin/python

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
        return A,B
    
    def xor_(self):
        A, B = self.emparejar()
        print("A")
        print(A)
        print("B")
        print(B)
        
        return "WUT"
        
    def multiplicacion_(self):
        return "WUT"
        
    def poli_(self):
        return "WUT"
