# program for testing grippper status
import os
import sys
# Append parent directory to import path, import file from parent directory
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#print(__file__) #./file.py
#print(os.path.abspath(__file__)) #./file.py
#print(os.path.dirname(os.path.abspath(__file__))) #./
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #../

from mcp45hvx1 import MCP45HVX1
import time

def main():
    while(True):
        for i in range(61, 256, 2):
            digiPot.writeWiper(i)
            print("readWiper: ", digiPot.readWiper(), "\n")
            time.sleep(0.05)  # minimum 0.05

def function_test():

    digiPot = MCP45HVX1(0x3c)

    print("....... Functionality Test Begin ..........")
    # Wiper ........................... #
    digiPot.writeWiper(127)

    print("\n----- Wiper Register ----")
    print("readWiper: ", end=" ")
    print(digiPot.readWiper())

    print("writeWiper: ", end=" ")
    digiPot.writeWiper(0)
    print(digiPot.readWiper())

    print("incrementWiper by 1: ", end=" ")
    digiPot.incrementWiper(1)
    print(digiPot.readWiper())

    print("incrementWiper by 2: ", end=" ")
    digiPot.incrementWiper(2)
    print(digiPot.readWiper())

    print("incrementWiper by 3: ", end=" ")
    digiPot.incrementWiper(3)
    print(digiPot.readWiper())

    print("incrementWiper by 4: ", end=" ")
    digiPot.incrementWiper(4)
    print(digiPot.readWiper())

    print("decrementWiper by 1: ", end=" ")
    digiPot.decrementWiper(1)
    print(digiPot.readWiper())

    print("decrementWiper by 2: ", end=" ")
    digiPot.decrementWiper(2)
    print(digiPot.readWiper())

    print("decrementWiper by 3: ", end=" ")
    digiPot.decrementWiper(3)
    print(digiPot.readWiper())

    print("decrementWiper by 4: ", end=" ")
    digiPot.decrementWiper(4)
    print(digiPot.readWiper())

    print("writeWiper: ", end=" ")
    digiPot.writeWiper(255)
    print(digiPot.readWiper())

  # TCON ..........................#
    print("readTCON :", bin(digiPot.readTCON()))
    digiPot.shutdown()
    print("shutdown :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.startup()
    print("startup :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.shutdown()
    print("shutdown :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.startup()
    print("startup :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.disconnectTerminalA()
    print("disconnectTerminalA :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.connectTerminalA()
    print("connectTerminalA :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.disconnectTerminalA()
    print("disconnectTerminalA :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.connectTerminalA()
    print("connectTerminalA :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.disconnectWiper()
    print("disconnectWiper :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.connectWiper()
    print("connectWiper :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.disconnectWiper()
    print("disconnectWiper :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.connectWiper()
    print("connectWiper :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.disconnectTerminalB()
    print("disconnectTerminalB :", bin(digiPot.readTCON()))
    time.sleep(2)
    digiPot.connectTerminalB()
    print("connectTerminalB :", bin(digiPot.readTCON()))
    time.sleep(2)

if __name__ == "__main__":
    digiPot = MCP45HVX1(0x3c)
    function_test()
    print("RUN main function")
    time.sleep(5)
    main()