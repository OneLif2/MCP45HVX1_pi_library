""" ******************************************************

  This file is the MCP45HVX1 library.
  Copyright (c) 2022 OneLif2. All rights reserved.
  
  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.
  
  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.
  
  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

********************************************************** """

import smbus
import time


class MCP45HVX1(object):

    def __init__(self, addr):
        self.addr = addr
        self.i2c = smbus.SMBus(1)

        self.R0HW = True
        self.R0A = True
        self.R0B = True
        self.R0W = True

    # TCON configuration.................. #
        self.TCON_R0HW = 0x08  # Shutdown Resistor Force
        self.TCON_R0A = 0x04  # Terminal A Connection
        self.TCON_R0W = 0x02  # Wiper Connection
        self.TCON_R0B = 0x01  # Terminal B Connection

        self.GCALL_TCON = 0x60
        self.GCALL_WIPER = 0x40
        self.GCALL_WIPERUP = 0x42
        self.GCALL_WIPERDWN = 0x44
        self.GCALL_COM_WRITE = 0x02
        self.GCALL_COM_RWRITE = 0x03
        self.GCALL_COM_WIPERINC = 0x42
        self.GCALL_COM_WIPERDEC = 0x44

        self.MEM_WIPER = 0x00
        self.MEM_TCON = 0x40

        self.COM_WRITE = 0x00
        self.COM_READ = 0x0C
        self.COM_WIPERINC = 0x04
        self.COM_WIPERDEC = 0x08

    def writeWiper(self, wiperValue):
        try:
            self.i2c.write_byte_data(
                self.addr, (self.MEM_WIPER | self.COM_WRITE), wiperValue & 0xff)
            #self.i2c.write_i2c_block_data(self.addr, self.MEM_WIPER , [wiperValue & 0xff])

        except IOError:
            print("WriteError: wiper 0")
            return (0)

        else:
            #print("write",wiperValue," to wipter")
            return

    def readWiper(self):
        try:
            self.arr = self.i2c.read_i2c_block_data(
                self.addr, (self.MEM_WIPER | self.COM_READ), 2)
            # print(self.arr)

        except IOError:
            #print("ReadError: wiper 0")
            return (0)

        else:
            return (self.arr[0] << 8 | self.arr[1] & 0xff)

    def incrementWiper(self, incriments):
        try:
            arr = [None] * incriments
            for i in range(0, incriments, 1):
                arr[i] = (self.MEM_WIPER | self.COM_WIPERINC)
            # print(arr)
            self.i2c.write_i2c_block_data(self.addr, arr[0], arr[1:])

        except IOError:
            print("WriteError: incrementWiper")
            return (0)

        else:
            #print("write",wiperValue," to wipter")
            return

    def decrementWiper(self, decriments):
        try:
            arr = [None] * decriments
            for i in range(0, decriments, 1):
                arr[i] = (self.MEM_WIPER | self.COM_WIPERDEC)
            # print(arr)
            self.i2c.write_i2c_block_data(self.addr, arr[0], arr[1:])

        except IOError:
            print("WriteError: decrementWiper")
            return (0)

        else:
            #print("write",wiperValue," to wipter")
            return

    # TCON Register...........................................................#

    def readTCON(self):
        try:
            self.arr = self.i2c.read_i2c_block_data(
                self.addr, (self.MEM_TCON | self.COM_READ), 2)

        except IOError:
            #print("ReadError: wiper 0")
            return (0)

        else:
            return (self.arr[0] << 8 | self.arr[1] & 0xff)

    def defaultTCON(self):
        self.R0HW = True
        self.R0A = True
        self.R0B = True
        self.R0W = True
        self.write_TCON_Register()

    def writeTCON(self, inReg):
        #inReg is a 4-bits data to update the TCON status, e.g.: inReg = 0b0101 
        self.R0HW = inReg >> 3 & 0x1
        self.R0A = inReg >> 2 & 0x1
        self.R0B = inReg >> 1 & 0x1
        self.R0W = inReg >> 0 & 0x1
        self.write_TCON_Register()

    def write_TCON_R0HW(self, isOn):
        self.R0HW = isOn
        self.write_TCON_Register()

    def write_TCON_R0A(self, isOn):
        self.R0A = isOn
        self.write_TCON_Register()

    def write_TCON_R0W(self, isOn):
        self.R0W = isOn
        self.write_TCON_Register()

    def write_TCON_R0B(self, isOn):
        self.R0B = isOn
        self.write_TCON_Register()

    def write_TCON_Register(self):
        try:
            buff = 0xff
            buff = (buff | self.TCON_R0HW) if self.R0HW == True else (
                buff ^ self.TCON_R0HW)
            buff = (buff | self.TCON_R0A) if self.R0A == True else (
                buff ^ self.TCON_R0A)
            buff = (buff | self.TCON_R0B) if self.R0B == True else (
                buff ^ self.TCON_R0B)
            buff = (buff | self.TCON_R0W) if self.R0W == True else (
                buff ^ self.TCON_R0W)

            #print("Writing TCON: ", bin(buff))

            self.i2c.write_byte_data(self.addr, (self.MEM_TCON | self.COM_WRITE), buff)

        except IOError:
            print("WriteError: wiper 0")
            return (0)

        else:
            return

    def startup(self):
        self.write_TCON_R0HW(True)

    def shutdown(self):
        self.write_TCON_R0HW(False)

    def connectTerminalA(self):
        self.write_TCON_R0A(True)

    def disconnectTerminalA(self):
        self.write_TCON_R0A(False)

    def connectTerminalB(self):
        self.write_TCON_R0B(True)

    def disconnectTerminalB(self):
        self.write_TCON_R0B(False)

    def connectWiper(self):
        self.write_TCON_R0W(True)

    def disconnectWiper(self):
        self.write_TCON_R0W(False)

def main():
    while(True):
        for i in range(61, 256, 2):
            digiPot.writeWiper(i)
            print("readWiper: ", digiPot.readWiper(), "\n")
            time.sleep(0.05)  # minimum 0.05

if __name__ == "__main__":
    digiPot = MCP45HVX1(0x3c)
    main()
