
# Connectors

### [Back to Index](index.md)

*Related* [I2C](i2c.md), [SPI](spi.md)



Connectors


## Grove

https://www.seeedstudio.com/Grove-Qwiic-Hub-p-4531.html
    Different from our Grove system, Qwiic is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with Qwiic, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - Qwiic Hub, which enables you easily connect the I2C devices with Grove/Qwiic/STEMMA QT interface, get the best use of your devices/controller of different interfaces.

*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [Stemma](connectors.md#stemma), [Stemma QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md)




## JST

https://en.wikipedia.org/wiki/JST_connector
    JST Series  "SH" 1.00 mm pin-to-pin pitch     "PH"  2.00mm pin-to-pin pitch
https://www.linkedin.com/company/jst-sales-america-inc  
    J.S.T. = Japanese Solderless Terminals As our company name implies, Solderless Terminal, has real significance. When JST was established in 1957, we were Japan's first manufacturer and distributor of Solderless Terminals.
The Great Search: JST Connectors SH and PH  https://www.youtube.com/watch?v=s5XYd0Z0HFw  1/5/2021
    1:14 JST PH great for power - Sparkfun originally started LiPo Battery connectors and it became a Maker standard. 
    2:25 Stemma QT - JST SH  - Sparkfun also originated Qwiic for breakout boards
    Also a brief intro to i2c (i2c has become the standard for sensors - rarely see SPI over sensors anymore) https://youtu.be/s5XYd0Z0HFw?t=169
Grove 10th Anniversary Documentary 12/31/2020  https://www.youtube.com/watch?v=r-W0XYhVdTk
NOTE: so STEMMA QT is different to STEMMA (see CircuitPython School video) -   STEMMA QT is equivalent to Sparkfun Qwiic.    


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [Stemma](connectors.md#stemma), [Stemma QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md)


## QWIIC


https://www.seeedstudio.com/Grove-Qwiic-Hub-p-4531.html
    Different from our Grove system, Qwiic is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with Qwiic, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - Qwiic Hub, which enables you easily connect the I2C devices with Grove/Qwiic/STEMMA QT interface, get the best use of your devices/controller of different interfaces.
    


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [Stemma](connectors.md#stemma), [Stemma QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md)

## STEMMA

https://www.adafruit.com/category/1005

STEMMA is a plug-and-play board and sensor system that lets you quickly plug together various devices and accessories, without any soldering! STEMMA uses 3-pin cables for simple analog and digital devices, like relays and buttons. For more complex sensors and displays, we use a 4-wire I2C connection. For larger boards and devices we use a Grove-compatible connector, for smaller ones we use a Qwiic-compatible connector called STEMMA QT.

As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.


As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.

*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [Stemma](connectors.md#stemma), [Stemma QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md)


## STEMMA QT

https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt
    What is STEMMA QT?
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun Qwiic uses, so that Qwiic & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


CircuitPython School - Choosing a Board for CircuitPython - A Few Important Considerations-2dEBAN_bd9o.mp4
Minute 6:15 Stemma-QT is discussed
Minute 8:49 Stemma standard is discussed - not plug-compatible with Stemma-QT

 STEMMA - JST PH 3 and 4 pin connectors (2.0mm pitch connectors)
 4 pins - I2C
 3 pins - PWM/Analog/Digital
 Cross-compatible with Grove/Gravity

 STEMMA-QT - JST SH (1.0mm pitch connectors)
 4 pins - I2C (when the larger JST PH connectors won't fit on a small sensor board)
 Cross-compatible with SparkFun Qwiic

From the video description ```https://www.youtube.com/watch?v=_Cu7UOcGL14```
 STEMMA started in 2014, intended to be compatible with Grove (cause Grove is all that existed at the time - since 2010)
 QWIIC started in 2017, STEMMA-QT added so that could use the smaller connectors.
 In addition - on the comparison page it states that Grove is a proprietary 4 pin 2.0mm pitch connector.
 STEMMA attempts to be as cross-compatible as possible with both Grove and Gravity (compatible connectors & 3-5V power/logic). STEMMA QT is cross-compatible with Qwiic - STEMMA QT connector/cable is same as Qwiic. You can use STEMMA QT devices with Qwiic devices/controllers.
 There is also a table which outlines the compatability matrix.  https://learn.adafruit.com/introducing-adafruit-stemma-qt/stemma-qt-comparison

Minute 4:00 - Arduino Nano RP2040 Connect Pros and Cons listed
Minute 10:30 - Feather RP2040 Pros and Cons listed
Minute 11:19 - QT Py RP2040 Pros and Cons listed
Minute 12:19 Microcontrollers vs "Computers"



CircuitPython School - Adding STEMMA QT_Qwiic to an Arduino RP2040 + Using a Temperature Sensor-IX3VvSU3bCY.mp4
Minute 0:57  Stemma QT recap
Minute 1:42 shows some boards which have STEMMA-QT ports


- [ ] Awesome list for Stemma QT:  https://github.com/adafruit/awesome-stemma


*Related* [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [Stemma](connectors.md#stemma), [Stemma QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md)


## STEMMA and STEMMA QT

- [ ] Explanation of STEMMA and STEMMA QT https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma  Also explains the differences to Grove and Qwiic  ```https://www.youtube.com/watch?v=_Cu7UOcGL14```  7/28/2019

https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt
    What is STEMMA QT?
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun Qwiic uses, so that Qwiic & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


https://www.seeedstudio.com/Grove-Qwiic-Hub-p-4531.html
    Different from our Grove system, Qwiic is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with Qwiic, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - Qwiic Hub, which enables you easily connect the I2C devices with Grove/Qwiic/STEMMA QT interface, get the best use of your devices/controller of different interfaces.


# What is the difference between Stemma and Stemma QT


Stemma, Qwiic and Grove Connectors: Which is Right for You?
https://www.tomshardware.com/features/stemma-vs-qwiic-vs-grove-connectors  4/24/2021
What are Stemma and Stemma QT?
Adafruit’s Stemma connector arrived in 2018 and essentially it is three or four pin JST PH with 2.00 mm pitch, a connector which is keyed so that it cannot be inserted incorrectly. Stemma is seen on larger boards such as PyPortal which has plenty of space for multiple three and four pin connectors.
There are two forms of Stemma connectors, a three or four pin connector. The three pin connector is used for Pulse Width Modulation, Analog and Digital IO. Using this connector we can control Neopixels, read analog sensors and use digital IO devices such as LEDs and buttons. The four-pin connector is for I2C (Inter-Integrated Circuit) components, enabling the use of multiple sensors / devices on a single bus thanks to devices having an address which can be read from / written to.
Stemma is a great connector, but for smaller boards, such as Adafruit’s QT Py RP2040 we need something smaller and that is where Stemma QT (‘cutie’) comes in. Stemma QT is a smaller version of the four pin Stemma format, roughly half the size of Stemma, with a 1.0 mm pitch. Stemma QT is only for use with I2C components. Analog, PWM and digital IO connections are made via the traditional GPIO.
The pin order for QT is designed to match the pin order for SparkFun’s Qwiic enabling the use of Qwiic add-ons with Stemma QT boards and for the reverse to also be true.
Examples of Stemma QT boards are Adafruit’s MPR121 capacitive touch sensor, SGP40 air quality sensor, aBME680 temperature / humidity / pressure sensor and AMG8833 IR thermal camera.

What is Qwiic?
SparkFun’s Qwiic Connect System was released in 2017 and is for use with I2C components. It is compatible with Adafruit’s Stemma and Stemma QT as Qwiic uses the same pin ordering. Qwicc, like Stemma, uses the I2C protocol and enables components to be daisy chained together.
Qwiic connectors can be found on many of SparkFun’s boards such as the MicroMod ATP carrier board which uses an M.2 slot, the MicroMod standard, for interchangeable processor boards such as the ESP32, Artemis and the new RP2040. There are also adapters for using Qwiic components on the Raspberry Pi via a HAT and pHAT and for the Arduino range of boards.
With SparkFun’s Qwiic connector we can easily connect sensors such as the HC-SR04 ultrasonic sensor, soil moisture sensor and even a NEO-M9N GPS breakout.

What is Seeed Studio’s Grove Connector?
Seeed Studio’s Grove connector is a proprietary connector for its range of boards and boards made in partnership with Arduino. The Grove connector is a 4-pin cable which can be used with analog, PWM, digital IO and I2C.

Grove is compatible with Stemma components, but only for I2C devices as analog, PWM and digital IO are not compatible. If you are unsure, just take a look at the component. If it has SDA / SCL pins, then it is an I2C device.

If you have never used Grove connections before, then the Grove Beginner Kit is worth your investment. In the kit we get an OLED screen, DHT11 temperature sensor, microphone, light sensor and a bonus Arduino compatible board.

## Connector Comparison

| Device    | Connector                                                          | Voltage / Logic | Protocols                                 |
| --------- | ------------------------------------------------------------------ | --------------- | ----------------------------------------- |
| Stemma    | JST PH 3 / 4 Pin 2.0mm pin pitch                                   | 3-5V DC         | 4 Pin I2C or 3 Pin Analog / Digital / PWM |
| Stemma QT | JST SH 4 pin 1.0mm pin pitch                                       | 3-5V DC         | I2C                                       |
| Qwiic     | JST SH 4 pin 1.0mm pin pitch                                       | 3V DC           | I2C                                       |
| Grove     | Proprietary 4 pin 2.0mm pin pitch, Compatible with Stemma I2C only | 3-5V DC         | 4 Pin I2C / Analog / Digital / PWM        |

Which Connector is Right For You?
The answer is based on what boards you already have and what you want to achieve. If you have Adafruit’s boards, then you will most likely have some form of Stemma / Stemma QT connector and so the entire range of add-ons is available to you. You will also have access to SparkFun’s Qwiic range of add ons which opens up a plethora of options for your projects. This is also true if you have any of SparkFun’s boards with Qwiic connectors. 

Seeed’s Grove connectors work with Arduino, Raspberry Pi and now the Raspberry Pi Pico. So buying one set of Grove components is good value for those that wish to use them across multiple platforms.

Ultimately the choice is yours. What projects you wish to build will dictate the choices that you make. But no matter what choice you make, all of these connectors make electronics a breeze and give you the confidence to learn new skills without worrying about your wiring.

