#!/usr/bin/python

class FileManager:
    
    def __init__(self): 
        self.file_name = None
        self.file_data = None
        
    def saveFile(self,file_name = None,file_data = None):
        if(file_name != None):
            self.file_name = file_name
        if(file_data != None):
            self.file_data = file_data
        if self.file_name != None and self.file_data != None:
            F = open(self.file_name,"w")
            F.write(self.file_data)
            F.close()
        else:
            print("No hay informacion para guardar.")
            
    def loadFile(self,file_name = None):
        if(file_name != None):
            self.file_name = file_name
        if self.file_name != None:
            F = open(self.file_name,"r")
            self.file_data = F.read()
            F.close()
            return self.file_data    
        else:
            print("Nombre de archivo no valido.")
            return None
    
    def getFileData(self):
        return self.file_data
        
    def getFileName(self):
        return self.file_name
        
