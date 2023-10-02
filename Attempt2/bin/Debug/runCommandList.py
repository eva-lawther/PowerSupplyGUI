
from pydoc import Doc
from re import S
from tkinter import Variable
import pyvisa
from time import sleep
from commandClass import channelInstrument 
import sed_json as fm #file manager ### C# Interaction



def devices():
    rm = pyvisa.ResourceManager()
    print("Resources detected\n{}\n".format(rm.list_resources()))
    dmm = rm.open_resource('ASRL6::INSTR')    # resource id for digital multi meter
    supply = rm.open_resource('ASRL13::INSTR') # resource id for power supply   
    
    # set digital multimeter to dc voltage mode
    #dmm.write('VDC')
    return (supply,  rm)

def runCommandList(supply):
    file = open("runningFile.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        if (line[0:5] == "sleep" ):
            time = line.split(" ")[1]
            sleep(time)
        else:
            runLine(supply, line)

def runLine(supply, line):
    supply.write(line)    




         
        

def main():
    supply,  rm = devices()  
    runCommandList(supply)
    
    
    
    rm.close()

 