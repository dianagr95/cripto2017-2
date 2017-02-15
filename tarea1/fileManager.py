#!/usr/bin/python

class FileManager:

    def saveFile(self,file_name,file_data):
        F = open(file_name,"w")
        F.write(file_data)
        F.close()

    def saveFileBytes(self,file_name,file_data):
        F = open(file_name,"wb")
        F.write(file_data)
        F.close()

    def loadFile(self,file_name):
        F = open(file_name,"r")
        file_data = F.read()
        F.close()
        return file_data 

    def loadFileBytes(self,file_name):
        F = open(file_name,"rb")
        file_data = F.read()
        F.close()
        return file_data 
