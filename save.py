import time
import pexpect
import subprocess
import sys
import bluetoothctl #Package written by Egor Fedorov from ReachView.

class bash:
        def killblue(self):
                pid = pexpect.run('pidof bluetoothctl')
                pexpect.run('sudo kill ' + pid)
        def initpulse(self):
                pexpect.run('/usr/bin/pulseaudio --start')

if __name__ == "__main__":

#Code finished and is ready to implement with Pi, but has not been yet.  Pseudocode below.
#This program should be executed as an interrupt on the Pi while scan.py is executing.
#IF PUSH BUTTON 2 IS PRESSED AND SCAN IS IN PROGRESS, SAVE CURRENT SCANNED MAC ADDRESS TO SAVE1 FILE.
#ELSE CONNECT BLUETOOTH TO CURRENT SAVED MAC ON SAVE1 FILE.

    rwtempMAC = open("tempMAC.txt", "r")
    tempMAC = rwtempMAC.read()
    checkScan = open("checkscan.txt", "r")
    scan = checkScan.read()
    saveRW = open("Save1.txt", "r+")
    if scan==1:
        print("Writing tempMAC into Save file")
        saveRW.write(tempMAC)
    else:
        kb = bash()
        kb.killblue()
        kb.initpulse()
        bl = Bluetoothctl()
        MAC = saveRW.read()
        print("Attempting to connect to Save file MAC: " + MAC)
        bl.connect(MAC)

    saveRW.close()
    rwtempMAC.close()

#IF PUSH BUTTON 3 IS PRESSED AND SCAN IS IN PROGRESS, SAVE CURRENT SCANNED MAC ADDRESS TO SAVE2 FILE.
#ELSE CONNECT BLUETOOTH TO CURRENT SAVED MAC ON SAVE2 FILE.
    rwtempMAC = open("tempMAC.txt", "r")
    tempMAC = rwtempMAC.read()
    checkScan = open("checkscan.txt", "r")
    scan = checkScan.read()
    saveRW = open("Save2.txt", "r+")
    if scan==1:
        print("Writing tempMAC into Save file")
        saveRW.write(tempMAC)
    else:
        kb = bash()
        kb.killblue()
        kb.initpulse()
        bl = Bluetoothctl()
        MAC = saveRW.read()
        print("Attempting to connect to Save file MAC: " + MAC)
        bl.connect(MAC)

    saveRW.close()
    rwtempMAC.close()

#IF PUSH BUTTON 4 IS PRESSED AND SCAN IS IN PROGRESS, SAVE CURRENT SCANNED MAC ADDRESS TO SAVE3 FILE.
#ELSE CONNECT BLUETOOTH TO CURRENT SAVED MAC ON SAVE3 FILE.
    rwtempMAC = open("tempMAC.txt", "r")
    tempMAC = rwtempMAC.read()
    checkScan = open("checkscan.txt", "r")
    scan = checkScan.read()
    saveRW = open("Save3.txt", "r+")
    if scan==1:
        print("Writing tempMAC into Save file")
        saveRW.write(tempMAC)
    else:
        kb = bash()
        kb.killblue()
        kb.initpulse()
        bl = Bluetoothctl()
        MAC = saveRW.read()
        print("Attempting to connect to Save file MAC: " + MAC)
        bl.connect(MAC)

    saveRW.close()
    rwtempMAC.close()

#IF MORE SAVES NEEDED ADD MORE OF THE ABOVE CODE.


