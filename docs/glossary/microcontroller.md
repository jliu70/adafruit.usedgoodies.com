
# Microcontroller

### [Back to Index](index.md)

*Related* [Feather](feather.md), [Itsy Bitsy](itsy_bitsy.md), [QT Py](qt_py.md), [RP2040](rp2040.md)


Microcontrollers are single purpose computers 

- small embedded development boards
- limited storage and memory
- limited processing power


## Microcontrollers vs General Purpose Computer

- Use of microcontrollers is fine for most cases
- When you need more computational power, you may want to use a [Raspberry Pi](raspberry_pi.md)
    - For example, if you wish to have a web dashboard to interface with


## Comparison of Raspberry Pi to Arduino

### Features

| Raspberry Pi                        | Arduino                       |
|:------------------------------------|:------------------------------|
| Raspberry Pi is a Microcomputer     | Arduino is a Microcontroller  |
| Operating System on MicroSD card    | Bootloader on chip            |
| USB, Video, Camera, Display & Audio | USB                           |
| I2C &SPI Busses                     | I2C & SPI Buses               |
| Digital I/O                         | Digital I/O and Analog Inputs |
| 5v USB power                        | 5v USB & 8-20v DC power       |
| Commercial patented product         | Open source design            |



The Raspberry Pi's schematics are released, but the board itself is not open hardware. The Raspberry Pi Foundation relies on income from the sale of Raspberry Pis to do its charitable work.
Reference: [https://opensource.com/resources/raspberry-pi](https://opensource.com/resources/raspberry-pi)

### Specs

| Raspberry Pi                       | Arduino                      |
| :--------------------------------- | :--------------------------- |
| Up to 1.5 GHz 64-bit quad-core CPU | 16 MHz 8-bit single-core MCU |
| 512 MB to 8 GB RAM                 | 2 Kb - 8 Kb SRAM             |
| 26 Digital I/O pins                | 14 - 54 Digital I/O pins     |
| No Analog inputs                   | 6 - 16 Anallog inputs        |
| Bluetooth & WiFi (some models)     | No Bluetooth or WiFi         |
| Ethernet (some models)             | No Ethernet                  |
| Expand with HATs                   | Expand with Shields          |



### Extras

| Raspberry Pi                | Arduino   |
| :-------------------------- | :-------- |
| MicroSD card                | USB Cable |
| USB (or USB-C) power supply | Computer  |
| Keyboard                    |           |
| Mouse                       |           |
| HDMI monitor                |           |
| Adapter cables as required  |           |


NOTE: as the Raspberry Pi is a SBC (Single Board Computer) - you will need all the peripherals for Input and Output, as well as an OS.

NOTE: the Arduino is a microcontroller so that it requires a separate computer to push code/instructions to it

**Recap** 

- Arduino - precision timing, measure pulse widths to a high degree of accuracy
- Raspberry Pi - add more intelligence  
