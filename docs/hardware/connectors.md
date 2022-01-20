# Connectors


## STEMMA and STEMMA QT

- [ ] Explanation of STEMMA and STEMMA QT https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma  Also explains the differences to Grove and Qwiic  ```https://www.youtube.com/watch?v=_Cu7UOcGL14```  7/28/2019

https://learn.adafruit.com/introducing-adafruit-stemma-qt/what-is-stemma-qt
    What is STEMMA QT?
    We like the JST PH 2.0mm pitch cables because they are cross-compatible with Grove/Gravity. But they're a bit large for smaller breakout boards and wearables. So, for smaller I2C devices, we'll use the JST SH that SparkFun Qwiic uses, so that Qwiic & STEMMA QT sensors are cross-compatible!  
    https://www.youtube.com/watch?v=6GXRRuFuFy0


https://www.seeedstudio.com/Grove-Qwiic-Hub-p-4531.html
    Different from our Grove system, Qwiic is an I2C interface system initiated by Sparkfun around 2017, using a 4pin JST SH 1.0mm connector. STEMMA QT initiated by Adafruit is cross-compatible with Qwiic, as they use the same connector/cable. To better support different types of interface systems, we provide Grove - Qwiic Hub, which enables you easily connect the I2C devices with Grove/Qwiic/STEMMA QT interface, get the best use of your devices/controller of different interfaces.


### JST 

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

 
