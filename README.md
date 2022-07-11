# MCP45HVX1 Digital Potentiometer Driver for Raspberry Pi / Jetson Nano
#MCP45HVX1 #Ditgital variable resistor #Potentiometer #Raspberry Pi #Jetson Nano

## Wiring Diagram

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |


```
+-----------------------------+---------------------------------
|   Raspberry Pi               |   MCP41HVX1
| Pin | Description            | Pin | Description
+-----+-----------------------+-----+---------------------------
|+3.3v| 5v is also supported   |  1  | Power 1.8v to 5.5v 
|   5 | SCL1 I2C Bus 1         |  2  | SCL
|GPIO | Any GPIO Pin or GND    |  3  | A1
|   3 | SDA1 I2C Bus 1         |  4  | SDA
|GPIO | Any GPIO Pin or GND    |  5  | A0
| GND | (Not supported yet)    |  6  | WLAT
| GND |                        |  7  | NC
|+3.3v| (Not supported yet)    |  8  | SHDN
| GND |                        |  9  | DGND
| GND |                        | 10  | V-    (Connect to external power supply max 36 volts. Common ground with Arduino
|     | (e.g. GND)             | 11  | POB   (This is the potentiometer)
|     | (e.g. 330 Ohm + LED)   | 12  | POW   (This is the wiper of the potentiometer)
|     | (e.g. +5v)             | 13  | POA   (This is the potentiometer)
|     |                        | 14  | V+    (Connect to external power supply max 36 volts)

```