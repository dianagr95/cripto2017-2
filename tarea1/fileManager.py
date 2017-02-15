#!/usr/bin/python

class FileManager:
    
        
    def saveFile(self,file_name = None,file_data = None):
		F = open(self.file_name,"w")
        F.write(self.file_data)
        F.close()
            

            
    def loadFile(self,file_name = None):
		F = open(self.file_name,"r")
        self.file_data = F.read()
        F.close()
        return self.file_data 
