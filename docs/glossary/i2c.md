
# I2C

### [Back to Index](index.md)

*Related* [SPI](spi.md), [QWIIC](connectors.md#qwiic), [STEMMA](connectors.md#stemma), [STEMMA QT](connectors.md#stemma-qt), [What is the difference between Stemma and Stemma QT](connectors.md#what-is-the-difference-between-stemma-and-stemma-qt)


I2C


https://blog.adafruit.com/2022/02/03/luxuriously-long-stemma-qt-cable-samples/


!!! quote
    I2C was never meant to go 200, 300 or 400mm but we laugh in the face of death thanks to these samples we got of some looooooooong stemma qt cables. each cable has two JST SH connectors on either end and a PVC sheathed center. we were inspired by this tweet https://twitter.com/lovyan03/status/1480867328783163396 about I2C wire interleaving with power in order to avoid cross-talk for long cables (I2C is not differential so you definitely do not want to use twisted wires!) if you look closely, the cable is flat and has the red power wire between SDA and SCL instead of having them next to each other. we’re just trying it out here with our fancy new ESP32 Feather V2 which has an onboard STEMMA QT connector 

