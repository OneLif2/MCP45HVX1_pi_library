# MCP45HVX1 Digital Potentiometer Driver for Raspberry Pi / Jetson Nano
#MCP45HVX1 #Ditgital variable resistor #Potentiometer #Raspberry Pi #Jetson Nano

## Wiring Diagram
<table>
<thead>
  <tr>
    <th colspan="2">Raspberry Pi</th>
    <th colspan="2">MCP41HVX1</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Pin</td>
    <td>Description</td>
    <td>Pin</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>+3.3v</td>
    <td>5v is also supported</td>
    <td>1</td>
    <td>Power 1.8v to 5.5v<br></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>2</td>
    <td>SCL</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>3</td>
    <td>A1</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>4</td>
    <td>SDA</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>5</td>
    <td>A0</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>6</td>
    <td>WLAT</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>7</td>
    <td>NC</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>8</td>
    <td>SHDN</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>9</td>
    <td>DGND</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>10</td>
    <td>V-    (Connect to external power supply max 36 volts. Common ground with Raspberry Pi)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>11</td>
    <td>POB   (This is the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>12</td>
    <td>POW   (This is the wiper of the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>13</td>
    <td>POA   (This is the potentiometer)</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>14</td>
    <td>V+    (Connect to external power supply max 36 volts)</td>
  </tr>
</tbody>
</table>


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

---

<table>
  <tr>
    <th colspan="3">second</th>
  </tr>
  <tr>
    <td rowspan="2">1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
  <td> 4</rd>
  </tr>

</table>

