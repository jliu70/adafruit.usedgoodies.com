# Choosing a board

### [Back to Hardware Overview](index.md)

*Related* [Grove](../glossary/connectors.md#grove), [JST](../glossary/connectors.md#jst), [QWIIC](../glossary/connectors.md#qwiic), [Stemma](../glossary/connectors.md#stemma), [Stemma QT](../glossary/connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](../glossary/connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)


## Choosing a microcontroller for a project can be overwhelming.

Here are some great Adafruit guides on how to choose a microcontroller:

https://learn.adafruit.com/choose-your-circuitpython-board

https://learn.adafruit.com/how-to-choose-a-microcontroller

https://learn.adafruit.com/best-beginner-boards-for-teachers

### Considerations for Choosing a Board
##### Reference: CircuitPython School - Choosing a Board for CircuitPython - A Few Important Considerations-2dEBAN_bd9o.mp4

Ultimately there are many features to consider when choosing a board
- Wireless 
    - WiFi 
        and
    - Bluetooth
- STEMMA QT
- Expansion
- Size
- Battery and Pass-thru chargning
- Header pins
- Cabling
- Price 
- Power


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



# Connectors

Explore what is STEMMA or STEMMA QT

[Go to Connectors](../../glossary/connectors)

<div>
<a href="../../glossary/connectors/" class="btn btn-primary" role="button">Go to Connectors</a>
</div>



