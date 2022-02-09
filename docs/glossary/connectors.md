
# Connectors

### [Back to Index](index.md)

*Related* [I2C](i2c.md), [SPI](spi.md)


It used to be that in order to connect sensors or components you had to use a breadboard or do soldering.
However, in the past decade companies have begun to offer *connectors* which let you easily connect / disconnect components to your project without the need to use a breadboard or do soldering.

The benefit is that it makes it much more accessible for beginners.  And even for experienced people it is much easier and quicker to prototype and build interesting projects.  

Here we describe some of the more popular connectors that are in use today.

## Grove

https://www.seeedstudio.com/Grove-QWIIC-Hub-p-4531.html
    Different from our Grove system, QWIIC is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with QWIIC, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - QWIIC Hub, which enables you easily connect the I2C devices with Grove/QWIIC/STEMMA QT interface, get the best use of your devices/controller of different interfaces.

*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)




## JST

https://en.wikipedia.org/wiki/JST_connector
    JST Series  "SH" 1.00 mm pin-to-pin pitch     "PH"  2.00mm pin-to-pin pitch
https://www.linkedin.com/company/jst-sales-america-inc  
    J.S.T. = Japanese Solderless Terminals As our company name implies, Solderless Terminal, has real significance. When JST was established in 1957, we were Japan's first manufacturer and distributor of Solderless Terminals.
The Great Search: JST Connectors SH and PH  https://www.youtube.com/watch?v=s5XYd0Z0HFw  1/5/2021
    1:14 JST PH great for power - Sparkfun originally started LiPo Battery connectors and it became a Maker standard. 
    2:25 STEMMA QT - JST SH  - Sparkfun also originated QWIIC for breakout boards
    Also a brief intro to i2c (i2c has become the standard for sensors - rarely see SPI over sensors anymore) https://youtu.be/s5XYd0Z0HFw?t=169
Grove 10th Anniversary Documentary 12/31/2020  https://www.youtube.com/watch?v=r-W0XYhVdTk
NOTE: so STEMMA QT is different to STEMMA (see CircuitPython School video) -   STEMMA QT is equivalent to Sparkfun QWIIC.    


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)


## QWIIC


https://www.seeedstudio.com/Grove-QWIIC-Hub-p-4531.html
    Different from our Grove system, QWIIC is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with QWIIC, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - QWIIC Hub, which enables you easily connect the I2C devices with Grove/QWIIC/STEMMA QT interface, get the best use of your devices/controller of different interfaces.
    


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)

## STEMMA

https://www.adafruit.com/category/1005

STEMMA is a plug-and-play board and sensor system that lets you quickly plug together various devices and accessories, without any soldering! STEMMA uses 3-pin cables for simple analog and digital devices, like relays and buttons. For more complex sensors and displays, we use a 4-wire I2C connection. For larger boards and devices we use a Grove-compatible connector, for smaller ones we use a QWIIC-compatible connector called STEMMA QT.

As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.


As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.

*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)


## STEMMA QT

https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt
    What is STEMMA QT?
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun QWIIC uses, so that QWIIC & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


CircuitPython School - Choosing a Board for CircuitPython - A Few Important Considerations-2dEBAN_bd9o.mp4
Minute 6:15 STEMMA-QT is discussed
Minute 8:49 STEMMA standard is discussed - not plug-compatible with STEMMA-QT

 STEMMA - JST PH 3 and 4 pin connectors (2.0mm pitch connectors)
 4 pins - I2C
 3 pins - PWM/Analog/Digital
 Cross-compatible with Grove/Gravity

 STEMMA-QT - JST SH (1.0mm pitch connectors)
 4 pins - I2C (when the larger JST PH connectors won't fit on a small sensor board)
 Cross-compatible with SparkFun QWIIC

From the video description ```https://www.youtube.com/watch?v=_Cu7UOcGL14```
 STEMMA started in 2014, intended to be compatible with Grove (cause Grove is all that existed at the time - since 2010)
 QWIIC started in 2017, STEMMA-QT added so that could use the smaller connectors.
 In addition - on the comparison page it states that Grove is a proprietary 4 pin 2.0mm pitch connector.
 STEMMA attempts to be as cross-compatible as possible with both Grove and Gravity (compatible connectors & 3-5V power/logic). STEMMA QT is cross-compatible with QWIIC - STEMMA QT connector/cable is same as QWIIC. You can use STEMMA QT devices with QWIIC devices/controllers.
 There is also a table which outlines the compatability matrix.  https://learn.adafruit.com/introducing-adafruit-stemma-qt/stemma-qt-comparison

Minute 4:00 - Arduino Nano RP2040 Connect Pros and Cons listed
Minute 10:30 - Feather RP2040 Pros and Cons listed
Minute 11:19 - QT Py RP2040 Pros and Cons listed
Minute 12:19 Microcontrollers vs "Computers"



CircuitPython School - Adding STEMMA QT_QWIIC to an Arduino RP2040 + Using a Temperature Sensor-IX3VvSU3bCY.mp4
Minute 0:57  STEMMA QT recap
Minute 1:42 shows some boards which have STEMMA-QT ports


- [ ] Awesome list for STEMMA QT:  https://github.com/adafruit/awesome-stemma


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)


## STEMMA and STEMMA QT

- [ ] Explanation of STEMMA and STEMMA QT https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma  Also explains the differences to Grove and QWIIC  ```https://www.youtube.com/watch?v=_Cu7UOcGL14```  7/28/2019

https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt
    What is STEMMA QT?
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun QWIIC uses, so that QWIIC & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


https://www.seeedstudio.com/Grove-QWIIC-Hub-p-4531.html
    Different from our Grove system, QWIIC is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with QWIIC, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - QWIIC Hub, which enables you easily connect the I2C devices with Grove/QWIIC/STEMMA QT interface, get the best use of your devices/controller of different interfaces.


# What is the difference between STEMMA and STEMMA QT


STEMMA, QWIIC and Grove Connectors: Which is Right for You?
https://www.tomshardware.com/features/stemma-vs-qwiic-vs-grove-connectors  4/24/2021
What are STEMMA and STEMMA QT?
Adafruit’s STEMMA connector arrived in 2018 and essentially it is three or four pin JST PH with 2.00 mm pitch, a connector which is keyed so that it cannot be inserted incorrectly. STEMMA is seen on larger boards such as PyPortal which has plenty of space for multiple three and four pin connectors.
There are two forms of STEMMA connectors, a three or four pin connector. The three pin connector is used for Pulse Width Modulation, Analog and Digital IO. Using this connector we can control Neopixels, read analog sensors and use digital IO devices such as LEDs and buttons. The four-pin connector is for I2C (Inter-Integrated Circuit) components, enabling the use of multiple sensors / devices on a single bus thanks to devices having an address which can be read from / written to.
STEMMA is a great connector, but for smaller boards, such as Adafruit’s QT Py RP2040 we need something smaller and that is where STEMMA QT (‘cutie’) comes in. STEMMA QT is a smaller version of the four pin STEMMA format, roughly half the size of STEMMA, with a 1.0 mm pitch. STEMMA QT is only for use with I2C components. Analog, PWM and digital IO connections are made via the traditional GPIO.
The pin order for QT is designed to match the pin order for SparkFun’s QWIIC enabling the use of QWIIC add-ons with STEMMA QT boards and for the reverse to also be true.
Examples of STEMMA QT boards are Adafruit’s MPR121 capacitive touch sensor, SGP40 air quality sensor, aBME680 temperature / humidity / pressure sensor and AMG8833 IR thermal camera.

What is QWIIC?
SparkFun’s QWIIC Connect System was released in 2017 and is for use with I2C components. It is compatible with Adafruit’s STEMMA and STEMMA QT as QWIIC uses the same pin ordering. Qwicc, like STEMMA, uses the I2C protocol and enables components to be daisy chained together.
QWIIC connectors can be found on many of SparkFun’s boards such as the MicroMod ATP carrier board which uses an M.2 slot, the MicroMod standard, for interchangeable processor boards such as the ESP32, Artemis and the new RP2040. There are also adapters for using QWIIC components on the Raspberry Pi via a HAT and pHAT and for the Arduino range of boards.
With SparkFun’s QWIIC connector we can easily connect sensors such as the HC-SR04 ultrasonic sensor, soil moisture sensor and even a NEO-M9N GPS breakout.

What is Seeed Studio’s Grove Connector?
Seeed Studio’s Grove connector is a proprietary connector for its range of boards and boards made in partnership with Arduino. The Grove connector is a 4-pin cable which can be used with analog, PWM, digital IO and I2C.

Grove is compatible with STEMMA components, but only for I2C devices as analog, PWM and digital IO are not compatible. If you are unsure, just take a look at the component. If it has SDA / SCL pins, then it is an I2C device.

If you have never used Grove connections before, then the Grove Beginner Kit is worth your investment. In the kit we get an OLED screen, DHT11 temperature sensor, microphone, light sensor and a bonus Arduino compatible board.

## Connector Comparison

| Device    | Manufacturer                                | Connector                                                                    | Voltage / Logic                                         | Protocols                                                         | Year Introduced | Compatible                           |
| --------- | ------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------- | --------------- | ------------------------------------ |
| Grove     | [Seeed Studio](https://www.seeedstudio.com) | Proprietary 4 pin 2.0mm pin pitch, Compatible with STEMMA [I2C](i2c.md) only | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current) | 4 Pin [I2C](i2c.md) / Analog / Digital / [PWM](pwm.md)            | 2010            | N/A                                  |
| QWIIC     | [Sparkfun](https://www.sparkfun.com)        | [JST SH](connectors.md#jst) 4 pin 1.0mm pin pitch                            | 3V [DC](https://en.wikipedia.org/wiki/Direct_current)   | [I2C](i2c.md)                                                     | 2017            | N/A                                  |
| STEMMA    | [Adafruit](https://www.adafruit.com)        | [JST PH](connectors.md#jst) 3 / 4 Pin 2.0mm pin pitch                        | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current) | 4 Pin [I2C](i2c.md) **or** 3 Pin Analog / Digital / [PWM](pwm.md) | 2014            | intended to be compatible with Grove |
| STEMMA QT | [Adafruit](https://www.adafruit.com)        | [JST SH](connector.smd#jst) 4 pin 1.0mm pin pitch                            | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current) | [I2C](i2c.md)                                                     | 2018            | intended to be compatible with QWIIC |

Which Connector is Right For You?
The answer is based on what boards you already have and what you want to achieve. If you have Adafruit’s boards, then you will most likely have some form of STEMMA / STEMMA QT connector and so the entire range of add-ons is available to you. You will also have access to SparkFun’s QWIIC range of add ons which opens up a plethora of options for your projects. This is also true if you have any of SparkFun’s boards with QWIIC connectors. 

Seeed’s Grove connectors work with Arduino, Raspberry Pi and now the Raspberry Pi Pico. So buying one set of Grove components is good value for those that wish to use them across multiple platforms.

Ultimately the choice is yours. What projects you wish to build will dictate the choices that you make. But no matter what choice you make, all of these connectors make electronics a breeze and give you the confidence to learn new skills without worrying about your wiring.

