
# Connectors

### [Back to Index](index.md)

*Related* [I2C](i2c.md), [SPI](spi.md), [GPIO](gpio.md)


It used to be that in order to add sensors or components to your project you had to use a breadboard or do soldering.
However in the past decade companies have begun to offer *connectors* which let you easily connect / disconnect components to your project without a breadboard or soldering.

A major benefit of these connectors is that it makes it much more accessible for beginners.  And experienced people can also benefit since it becomes much easier and quicker to prototype and build interesting projects.  

On this page we describe some of the more popular connectors in use today.

## Grove

Introduced by [Seeed Studio](https://www.seeedstudio.com/) in 2010, Grove uses a proprietary 4-pin 2.0mm pin pitch connector for its range of boards and boards made in partnership with Arduino.  The Grove connector can be used with analog, [PWM](pwm.md), digital IO and [I2C](i2c.md).

While almost the same as a [JST PH](connectors.md#jst) connector, Grove unfortunately is not compatible - they are physically too different for JST PH and Grove to be inter-changeable.


**Additional References on comparision of Grove to JST PH**

1. [Grove compared to JST PH](https://arduino.stackexchange.com/questions/9030/what-type-of-connector-does-the-grove-system-use)
2. [Grove compatability to JST PH](https://www.omzlo.com/articles/is-the-seeed-studio-grove-connector-compatible-with-the-jst-ph-connector)


As Grove has been around the longest, there are a [large number of components](https://www.seeedstudio.com/category/Grove-c-1003.html?cat=890) available.  

Many Grove components can be used with Adafruit hardware.

- Grove is is only compatible with STEMMA I2C components.  
- Analog, PWM and digital IO are not compatible.  
- If a component has SDA / SCL pins, then it is an I2C device.


Seeed Studio makes a [Grove - QWIIC Hub](https://www.seeedstudio.com/Grove-QWIIC-Hub-p-4531.html) to support interoperability with [Sparkfun QWIIC](connectors.md#qwiic) and [Adafruit STEMMA QT](connectors.md#stemma-qt).

!!! Description 
    Different from our Grove system, QWIIC is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with QWIIC, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - QWIIC Hub, which enables you easily connect the I2C devices with Grove/QWIIC/STEMMA QT interface, get the best use of your devices/controller of different interfaces.


**Additional References**

1. [Youtube: Grove 10th Anniversary Documentary 12/31/2020](https://www.youtube.com/watch?v=r-W0XYhVdTk)


*Related* [Connector Comparison](connectors.md#connector-comparison), [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#connector-comparison)




## JST

JST is an acronym for the company [Japanese Solderless Terminals](https://web.archive.org/web/20161127093915/http://www.jst-mfg.com/company/info_e.php).  They pioneered the first solderless connectors.

!!! From_the_Archive   
    J.S.T. = Japanese Solderless Terminals As our company name implies, Solderless Terminal, has real significance. When JST was established in 1957, we were Japan's first manufacturer and distributor of Solderless Terminals.

There are [many types of JST connectors](https://en.wikipedia.org/wiki/JST_connector), but the two most commonly used by Adafruit are:

- JST Series  "PH"  2.00mm pin-to-pin pitch
    - Used with [STEMMA](connectors.md#stemma)
- JST Series  "SH" 1.00 mm pin-to-pin pitch  
    - Used with [QWIIC](connectors.md#qwiic) and [STEMMA QT](connectors.md#stemma-qt)   


Here's a great video from Jan 5, 2021 where Lady Ada talks about JST SH and PH Connectors:

- [The Great Search: JST Connectors SH and PH](https://www.youtube.com/watch?v=s5XYd0Z0HFw) 
    - [0:57](https://youtu.be/s5XYd0Z0HFw?t=57) JST PH great for power - Sparkfun originally started LiPo Battery JST PH connectors and it became a Maker standard. 
    - [2:34](https://youtu.be/s5XYd0Z0HFw?t=154) JST SH  - Sparkfun also originated QWIIC for breakout boards (STEMMA QT compatible with QWIIC) 
        - Used for I2C (I2C has become the standard for sensors - rarely see sensors over SPI anymore) 



*Related* [Connector Comparison](connectors.md#connector-comparison), [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#connector-comparison)


## QWIIC

QWIIC is an I2C interface system introduced by Sparkfun in 2017, using a 4pin JST SH 1.0mm connector. 

STEMMA QT was introduced by Adafruit in 2018.  STEMMA QT is cross-compatible with QWIIC because they use the same connector/cable. 

The I2C protocol enables components to be daisy chained together.


>> QWIIC connectors can be found on many of SparkFun’s boards such as the MicroMod ATP carrier board which uses an M.2 slot, the MicroMod standard, for interchangeable processor boards such as the ESP32, Artemis and the new RP2040. There are also adapters for using QWIIC components on the Raspberry Pi via a HAT and pHAT and for the Arduino range of boards.
With SparkFun’s QWIIC connector we can easily connect sensors such as the HC-SR04 ultrasonic sensor, soil moisture sensor and even a NEO-M9N GPS breakout.



*Related* [Connector Comparison](connectors.md#connector-comparison), [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#connector-comparison)

## STEMMA


STEMMA standard is not plug-compatible with STEMMA-QT

STEMMA 

- JST PH 3 and 4 pin connectors (2.0mm pitch connectors)
    - 4 pins - I2C
        - Enable the use of multiple sensors / devices on a single bus thanks to devices having an address
    - 3 pins - PWM/Analog/Digital
        - Control Neopixels
        - Read analog sensors 
        - Use digital IO devices such as LEDs and buttons
- Connector is keyed so that it cannot be inserted incorrectly
- STEMMA is seen on larger boards such as PyPortal
- Aims to be compatible with Grove/Gravity


** Additional References **

1. [Adafruit STEMMA info page](https://www.adafruit.com/category/1005)

    STEMMA is a plug-and-play board and sensor system that lets you quickly plug together various devices and accessories, without any soldering! STEMMA uses 3-pin cables for simple analog and digital devices, like relays and buttons. For more complex sensors and displays, we use a 4-wire I2C connection. For larger boards and devices we use a Grove-compatible connector, for smaller ones we use a QWIIC-compatible connector called STEMMA QT.

    As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.

2. [Adafruit Learn Guide: What is STEMMA?](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma)

3. [Awesome list for STEMMA and STEMMA QT](https://github.com/adafruit/awesome-stemma)

*Related* [Connector Comparison](connectors.md#connector-comparison), [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#connector-comparison)



## STEMMA QT

STEMMA is not plug-compatible with STEMMA-QT

STEMMA QT (‘cutie’) 

- JST SH (1.0mm pitch connectors)
- 4 pins - I2C only 
- About half the size of STEMMA
    - great for smaller boards such as [Adafruit QT Py](qt_py.md)
- Cross-compatible with SparkFun QWIIC

Examples of STEMMA QT boards

- [Adafruit MPR121 capacitive touch sensor](https://www.adafruit.com/product/4830)
- [Adafruit SGP40 air quality sensor](https://www.adafruit.com/product/4829)
- [Adafruit BME680 temperature / humidity / pressure sensor](https://www.adafruit.com/product/3660)
- [Adafruit AHT20 temperature sensor](https://www.adafruit.com/product/4566)
- [Adafruit VL53L1X Time of Flight Distance Sensor](https://www.adafruit.com/product/3967)
- [Adafruit AMG8833 IR thermal camera](https://www.adafruit.com/product/3538)


**Additional References**

1. [Adafruit STEMMA info page](https://www.adafruit.com/category/1005)

    STEMMA is a plug-and-play board and sensor system that lets you quickly plug together various devices and accessories, without any soldering! STEMMA uses 3-pin cables for simple analog and digital devices, like relays and buttons. For more complex sensors and displays, we use a 4-wire I2C connection. For larger boards and devices we use a Grove-compatible connector, for smaller ones we use a QWIIC-compatible connector called STEMMA QT.

    As all STEMMA sensors have level shifting and voltage regulation, you can use them safely with any 3 to 5V power and logic device - from microcontrollers like Arduino-compatibles, to full Linux single board computers like the Raspberry Pi. We even have USB to I2C adapters that let you connect STEMMA devices directly to a computer without any microcontroller programming required! Then, use our Arduino or CircuitPython/Python libraries and examples to easily get your electronics project working on any platform with STEMMA and STEMMA QT.

2. [Adafruit Learn Guide: What is STEMMA QT?](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt)
    
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun QWIIC uses, so that QWIIC & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


3. From the [Adafruit STEMMA & STEMMA QT Plug & play connectivity - STEMMA Sunday video 7/28/2019](https://www.youtube.com/watch?v=_Cu7UOcGL14) description

    STEMMA started in 2014, intended to be compatible with Grove (cause Grove is all that existed at the time - since 2010)
    QWIIC started in 2017, STEMMA-QT added so that could use the smaller connectors.
    In addition - on the comparison page it states that Grove is a proprietary 4 pin 2.0mm pitch connector.
    STEMMA attempts to be as cross-compatible as possible with both Grove and Gravity (compatible connectors & 3-5V power/logic). STEMMA QT is cross-compatible with QWIIC - STEMMA QT connector/cable is same as QWIIC. You can use STEMMA QT devices with QWIIC devices/controllers.
    There is also a table which outlines the [compatability matrix](https://learn.adafruit.com/introducing-adafruit-stemma-qt/stemma-qt-comparison).

    Also explains the differences to Grove and QWIIC

4. [Adafruit Learn Guide: What is STEMMA QT?](https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt)


5. [Awesome list for STEMMA and STEMMA QT](https://github.com/adafruit/awesome-stemma)


*Related* [Connector Comparison](connectors.md#connector-comparison), [Grove](connectors.md#grove), [JST](connectors.md#jst), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between STEMMA and STEMMA QT](connectors.md#connector-comparison)





## STEMMA, QWIIC and Grove Connectors: Which is Right for You?

Reference: [Toms Hardware STEMMA vs QWIIC vs Grove Connectors](https://www.tomshardware.com/features/stemma-vs-qwiic-vs-grove-connectors)  4/24/2021

Depends on what boards you already have

- Adafruit boards usualy have some form of STEMMA / STEMMA QT connector
    - STEMMA QT is completely cross-compatible with Sparkfun QWIIC
    - STEMMA is different from STEMMA QT/QWIIC, aims to be compatible with Grove I2C 
- Seeed Grove connectors work with multiple platforms
    - Arduino
    - Raspberry Pi
    - Raspberry Pi Pico


## Connector Comparison

| Device    | Manufacturer                                | Connector                                             | Voltage / Logic                                           | Protocols                                                           | Year Introduced | Compatible                            |
| --------- | ------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------- | --------------- | ------------------------------------- |
| Grove     | [Seeed Studio](https://www.seeedstudio.com) | Proprietary 4 pin 2.0mm pin pitch                     | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current)   | 4 Pin [I2C](i2c.md) / Analog / Digital / [PWM](pwm.md)              | 2010            | Compatible with STEMMA I2C only       |
| QWIIC     | [Sparkfun](https://www.sparkfun.com)        | [JST SH](connectors.md#jst) 4 pin 1.0mm pin pitch     | **3V** [DC](https://en.wikipedia.org/wiki/Direct_current) | [I2C](i2c.md)                                                       | 2017            | N/A                                   |
| STEMMA    | [Adafruit](https://www.adafruit.com)        | [JST PH](connectors.md#jst) 3 / 4 Pin 2.0mm pin pitch | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current)   | 4 Pin [I2C](i2c.md)  **or**  3 Pin Analog / Digital / [PWM](pwm.md) | 2014            | Only STEMMA I2C compatible with Grove |
| STEMMA QT | [Adafruit](https://www.adafruit.com)        | [JST SH](connectors.md#jst) 4 pin 1.0mm pin pitch     | 3-5V [DC](https://en.wikipedia.org/wiki/Direct_current)   | [I2C](i2c.md)                                                       | 2018            | intended to be compatible with QWIIC  |


!!! note
    An Adafruit Learn Guide has a table which outlines the [cross-compatability matrix](https://learn.adafruit.com/introducing-adafruit-stemma-qt/stemma-qt-comparison).
