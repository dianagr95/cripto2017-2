#!/usr/bin/python

from fileManager import FileManager
import numpy as np

if __name__ == "__main__":

    fileM = FileManager()

    out = fileM.loadFile("xor.out")
    out1 = fileM.loadFile("xor1.out")
    if out == out1:
        print("yei")
    else:
        print("nain")

