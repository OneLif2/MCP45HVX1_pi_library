# MCP45HVX1 Digital Potentiometer Driver for Raspberry Pi / Jetson Nano
#MCP45HVX1 #Ditgital variable resistor #Potentiometer #Raspberry Pi #Jetson Nano

## Wiring Diagram

|  Raspberry Pi  || MCP45HVX1     ||
| :---        |    :----:   |   ---: |      ---: |
| Header      | Title       | Here's this   |Here's this   |
| Header      | Title       | Here's this   |Here's this   |
| Paragraph   | Text        | And more      |And more      |

|               |          Grouping             ||         Grouping 2         || Not Grouped    |
| First Header  | Second Header | Third Header   | Forth Header | Fifth Header | Sixth Header    |
| ------------- | :-----------: | -------------: | :----------: | :----------: | --------------- |
| Tall Cell     |          *Long Cell*          ||         *Long Long Cell*                    |||
| ^^            |   **Bold**    | 1. first item  | *Italic*     | 3. third item | + first point  |
| ^^            |               | 1. second item |              | 1. forth item | + second point |
| New section   |     More      |         Data   | ... - -- --- |||
| And more      | With an escaped \|          || "Try 'quotes' in quotes "         |||
[Compicated table]


| :                   MathJax \|\| Image                 : |||
| :------------ | :-------- | :----------------------------- |
| Apple         | : Apple : | Apple                          \
| Banana        | Banana    | Banana                         \
| Orange        | Orange    | Orange                         |
| :     Rowspan is 4     : || :        How's it?           : |
| ^^     A. Peach          ||    1. ![example][cell-image]   |
| ^^     B. Orange         || ^^ 2. $I = \int \rho R^{2} dV$ |
| ^^     C. Banana         || **It's OK!**                   |

[cell-image]: https://jekyllrb.com/img/octojekyll.png "An exemplary image"


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