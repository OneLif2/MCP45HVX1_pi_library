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

  # TCON ..........................#
    print("readTCON :", digiPot.readTCON())

if __name__ == "__main__":
    digiPot = MCP45HVX1(0x3c)
    function_test()
    main()