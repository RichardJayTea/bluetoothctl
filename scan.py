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

#This program scans for all MAC addresses currently available and shuffles them through the tempMac file.  If a scanned address is desired to be saved onto a save file then push the push button that represents numbered saved file.

#Scan for new device
    kb = bash()
    kb.killblue()
    kb.initpulse()
    bl = Bluetoothctl()
    scanCheck.open("checkscan.txt", "w")
    scanCheck.write("1")
    bl.start_scan()
    availDev = bl.get_available_devices()
    for i in availDev:
        dicti = i
        mac_add = dicti['mac_address']
        writetoTemp = open("tempMAC.txt", "w")
        writetoTemp.write(mac_add)
        print("Attempting to connect to address: " + mac_add)
        bl.connect(mac_add)
        time.sleep(5)
        bl.disconnect(mac_add)

    scanCheck.write("0")
    scanCheck.close()
    writetoTemp.close()
