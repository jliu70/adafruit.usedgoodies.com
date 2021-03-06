
# I2C

### [Back to Index](index.md)

*Related* [SPI](spi.md), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md#connector-comparison), [GPIO](gpio.md)

WIP

[I2C](https://en.wikipedia.org/wiki/I²C) (eye-squared-C) or *Inter-Integrated Circuit* is a synchronous, multi-master, multi-slave, packet-switched, single-ended, serial communication bus invented in 1982 by Philips Semiconductors.


I2C is a serial communication protocol commonly used for sensors and other simple devices that don’t need to send or receive data quickly.
I2C has become the standard for sensors - rarely see [SPI](spi.md) over sensors anymore.

I2C uses four wires

- power 
- ground
- clock (SCL)
- data (SDA)


I2C uses unique addresses for devices so it makes it possible to daisy chain multiple devices.  
NOTE: if you need to use the same type of component or sensor twice, some devices allow you to set a jumper to change the default address.  
Another option is to use [SparkFun STEMMA QT / Qwiic TCA9548A Mux Breakout - 8 Channel](https://www.adafruit.com/product/4704)


Addresses range from 0 to 128 
A seven bit wide address space theoretically allows 128 I2C addresses – however, some addresses are reserved for special purposes. Thus, only 112 addresses are available with the 7 bit address scheme. <sup>5</sup>


THe [QWIIC](connectors.md#qwiic) and [STEMMA QT](connectors.md#stemma-qt) devices exclusively communicate via I2C.  [STEMMA](connectors.md#stemma) 4-pin connectors can also use I2C. [Grove](connectors.md#grove) devices can also use I2C.  If you are unsure if a device uses I2C, if you see SCL and SDA pins then it is an I2C device.


I2C is ideal for short distances and low bandwidth communication.
I2C uses a client/server architecture. 

I2C limitiations:

- No hot plugging support
- No auto device discovery
- Addresses collisions may occur (if multiple devices use the same address)


[Working with Multiple Same Address I2C Devices](https://blog.adafruit.com/2022/05/04/new-guide-working-with-multiple-same-address-i2c-devices-circuitpython-adafruitlearningsystem-adafruit/)


[I2C Ecosystems](https://blog.adafruit.com/2022/05/05/i2c-ecosystems-the-connector-zoo-hackaday/)



https://blog.adafruit.com/2022/02/03/luxuriously-long-stemma-qt-cable-samples/

!!! quote
    I2C was never meant to go 200, 300 or 400mm but we laugh in the face of death thanks to these samples we got of some looooooooong stemma qt cables. each cable has two JST SH connectors on either end and a PVC sheathed center. we were inspired by this tweet https://twitter.com/lovyan03/status/1480867328783163396 about I2C wire interleaving with power in order to avoid cross-talk for long cables (I2C is not differential so you definitely do not want to use twisted wires!) if you look closely, the cable is flat and has the red power wire between SDA and SCL instead of having them next to each other. we’re just trying it out here with our fancy new ESP32 Feather V2 which has an onboard STEMMA QT connector 


[I2C over the network](https://blog.adafruit.com/2022/01/26/wifiwire-a-i2c-to-udb-bridge/)
WiFiWire is provides a Wire (i2c) protocol able to communicate over AsyncUDP.
You can have your program use a Wire (i2c) sensor/device, but it is communicating over a network rather than wiring. There are server and client software.



**Additional References**
1. [Adafruit Learn Guide: I2C devices](https://learn.adafruit.com/circuitpython-basics-i2c-and-spi/i2c-devices)
2. [CircuitPython Basics: I2C and SPI](https://learn.adafruit.com/circuitpython-basics-i2c-and-spi)
3. [CircuitPython Basics: Digital Inputs & Outputs](https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs)
4. [CircuitPython Basics: Analog Inputs & Outputs](https://learn.adafruit.com/circuitpython-basics-analog-inputs-and-outputs)
1. [Adafruit Learn Guide: Working with I2C devices](https://learn.adafruit.com/working-with-i2c-devices)
5. [I2C addressing](https://www.i2c-bus.org/addressing/)



<small>This page was last updated on 2022-05-05 16:55:07 -0500.</small>