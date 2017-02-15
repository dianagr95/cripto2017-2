#!/usr/bin/python

class FileManager:
        
    def saveFile(self,file_name,file_data):
		F = open(self.file_name,"w")
        F.write(self.file_data)
        F.close()
        
    def saveFileBytes(self,file_name,file_data):
		F = open(self.file_name,"wb")
        F.write(self.file_data)
        F.close()
            
    
    def loadFile(self,file_name):
		F = open(self.file_name,"r")
        self.file_data = F.read()
        F.close()
        return self.file_data 
            
    def loadFileBytes(self,file_name):
		F = open(self.file_name,"rb")
        self.file_data = F.read()
        F.close()
        return self.file_data 
