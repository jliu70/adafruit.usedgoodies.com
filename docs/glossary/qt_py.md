
# QT Py

### [Back to Index](index.md)

*Related* [Feather](feather.md), [Itsy Bitsy](itsy_bitsy.md)

WIP

QT Py is tiny.

It is size and pin compatible with Seeed Studio XIAO.

Adafruit [sells](https://www.adafruit.com/product/5033) the [Seeduino XIAO expansion board](https://blog.adafruit.com/2021/04/26/testing-out-qt-py-rp2040-with-xiao-extension-board/) which works with the Adafruit QT Py.


### Three versions of QT Py

| Device                                                  | Microcontroller        | Code                                | RAM / Storage                          | Cost   |
| ------------------------------------------------------- | ---------------------- | ----------------------------------- | -------------------------------------- | ------ |
| [QT Py SAMD21](https://www.adafruit.com/product/4600)   | ATSAMD21 ARM Cortex M0 | Arduino, CircuitPython, or MakeCode | 32KB RAM / 256 KB of SPI Flash storage | $7.50  |
| [QT Py ESP32-S2](https://www.adafruit.com/product/5325) | ESP32-S2               | Arduino, CircuitPython, or MakeCode | 2MB PSRSM / 4 MB of SPI Flash storage  | $12.50 |
| [QT Py RP2040](https://www.adafruit.com/product/4900)   | [RP2040](rp2040.md)    | Arduino, CircuitPython, or MakeCode | 264KB RAM / 8MB of SPI Flash           | $9.95  |


#### Additional versions of the QT Py on the way

| Device                                                                                                                                 | Microcontroller | Code                                | RAM /Storage                   |
| -------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------------------------- | ------------------------------ |
| [QT Py nRF52840](https://blog.adafruit.com/2022/01/06/qt-py-bluefruit-routin-party/) <sup>1</sup>                                      | nRF52840        | Arduino, CircuitPython, or MakeCode | 256KB RAM / ? storage          |
| [QT Py ESP32-S3](https://blog.adafruit.com/2022/01/07/qt-py-with-esp32-s3/) <sup>2, 3</sup>                                            | ESP32-S3        | Arduino, CircuitPython, or MakeCode | ? RAM / ? storage              |
| [QT Py ESP32-C3](https://blog.adafruit.com/2022/03/09/coming-soon-adafruit-qt-py-esp32-c3-wifi-dev-board-with-stemma-qt/) <sup>4</sup> | ESP32-C3        | Arduino, CircuitPython, or MakeCode | 400KB SRAM / 4MB Flash storage |


1. [Adafruit blog post about QT Py nRF52840 1/6/2022](https://blog.adafruit.com/2022/01/06/qt-py-bluefruit-routin-party/)
    Now we’ve got the QT Py SAMD21, RP2040 and ESP32-S2 designed and fabricated, we’re going to follow up with an NRF52840 version! We’ve been using the Nordict nRF series for a loooooong time (anyone else remember the nRF8001? it was like the AT90S2313 of bluetooth le for us). nRF52840 is the first one with native USB – and its plenty fast as a Cortex M4 at 64MHz and 256K of RAM. we already did a module-less route of this chip on the Circuit Playground Bluefruit so we know the schem capture is right.

2. [Adaafruit blog post about QT Py ESP32-S3 1/7/2022](https://blog.adafruit.com/2022/01/07/qt-py-with-esp32-s3/)
    This is a swap-out of the ESP32-S2 QT Py for the new ESP32-S3 chip. The S3 is really a nice piece of kit – dual core is back and it also re-adds BLE. It’s basically an ESP32 with native USB, we’re looking forward to it! note that the S3 chip looks a lot like the S2 but the chip pinout is NOT the same, the reset, and some power pins have moved. and some gpio shifted down one. also, looks like the dual DAC was removed. anyways, just watch out don’t think you can use the exact same layout. we had to shift a few parts but it all still looks like it fits! top part is identical to the S2 QT Py, and the bottom only shifted a few passives around. we’ll get some 4 layer prototypes on order.

3. [Desk of Lady Ada youtube video 1/9/2022](https://www.youtube.com/watch?v=xC7oodxTWgE)  
    This weekend we cranked through 3.5 QT Py designs (we didnt finish routing one, its a toughie!) - we already make SAMD21, RP2040 and ESP32-S2 and we wanted to add some more chips to the mix: ESP32-S3 (dual core version of the S2), ESP32 Pico (OG ESP with built in flash/psram), ESP32-C3 (Risc-V wifi!) and nRF52840 (BLE wonder-chip from Nordic). the last one is what we didn't get to finish routing because its a particularly tough one. The other 3 worked out fine with a 4 layer PCB. We also designed a few 'BFF' boards - that fit onto a QT Py like a shield. 

4. [Adafruit blog post about QT Ot ESP32-C3 3/9/2022](https://blog.adafruit.com/2022/03/09/coming-soon-adafruit-qt-py-esp32-c3-wifi-dev-board-with-stemma-qt/)
     ESP32-C3 is a low-cost microcontroller from Espressif that supports 2.4 GHz Wi-Fi and Bluetooth® Low Energy (Bluetooth LE). It has built-in USB-to-Serial, but not native USB – it cannot act as a keyboard or disk drive. The chip used here has 4MB of Flash memory, 400 KB of SRAM and can easily handle TLS connections.


## BFF 
As of January 2022, BFF is the placeholder name for Adafruit expansion boards for QT Py boards that fit onto a QT Py like a shield.
https://blog.adafruit.com/2022/01/11/qt-py-bff-with-lipoly-charging-and-switch/
https://blog.adafruit.com/2022/01/11/gamer-bff-qt-py-mini-gaming-add-on/

[Adafruit LiIon or LiPoly Charger BFF Add-On for QT Py](https://www.adafruit.com/product/5397)

[Adafruit Learn Guide: Adafruit LiIon or LiPoly Charger BFF Add-On for QT Py](https://blog.adafruit.com/2022/04/20/new-guide-adafruit-liion-or-lipoly-charger-bff-add-on-for-qt-py-adafruitlearningsystem-adafruit-adafruit/)


## Additional References
- [Hackster.io QT Py Review](https://www.hackster.io/news/this-little-qt-py-has-certainly-caught-our-eye-dfc2e322775f)


<small>This page was last updated on 2022-03-18 08:46:07 -0500.</small>
