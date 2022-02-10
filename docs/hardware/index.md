# Hardware

The Adafruit lingo for their hardware is quite extensive and can be confusing to someone new to the Adafruit ecosystem.  One of the primary goals of this website is to help newcomers sort through this cornicopia of terminology.


## Microcontrollers

Adafruit designs and sells their own custom microcontrollers. 

Microcontrollers are single purpose computers 

- small embedded development boards
- limited storage and memory
- limited processing power


Microcontrollers vs General Purpose Computer

- Use of Microcontrollers is fine for many cases
- When you need more computational power, you may want to use a [Raspberry Pi](https://www.raspberrypi.com)
    - For example, if you wish to have a web dashboard to interface with, then you will need to use a Raspberry Pi


For more info, see the **Glossary** page for [Microcontroller](../glossary/microcontroller.md)


## Recommended: First Adafruit Hardware for Beginners

!!! note
    *A Beginner's Recommendation*.

    **[Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit)**

Among the many Adafruit devices, the [Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit) is more accesible to beginners.  It is a great piece of hardware to start with.

For more info, see the **Glossary** page for [Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit)



## Comprehensive list of hardware supported by CircuitPython
List of all the hardware currently supported by CircuitPython (Adafruit and other manufacturers) is available at the [CircuitPython Downloads Page](https://circuitpython.org/downloads).

As of Feb 2022 

- There are over 270 boards supported by CircuitPython and that list grows everyday.
- The list is sorted by number of downloads.  
    - The most popular board -- the Raspberry Pi Pico -- is not manufactured by Adafruit.

## Adafruit Hardware

Adafruit offers over 60 different microcontrollers.

Within the Adafruit ecosystem, there are a few general categories:

- Adafruit Feather (Regular)

- ItsyBitsy (Small)

- QT Py (Tiny)

- Metro (Arduino form factor)

- Trinkey (USB dongles)

There are also custom form factors such as 

- [Circuit Playground](../../glossary/circuit_playground)
- Gemma M0
- Trinket M0
- FunHouse
- PyBadge/EdgeBadge
- [CLUE](../glossary/clue.md)


## Chipsets

Most Adafruit devices use one of the following chipsets: 

- SAMD21
- SAMD51
- ESP32-S2
- ESP32-S3
- NRF52840
- RP2040


You will often see multiple versions of a particular Adafruit form factor based upon different chipsets.

For example:

[Circuit Playground Versions](../glossary/circuit_playground/#circuit-playground)
[QT Py Versions](../glossary/qt_py/#qt-py)


https://blog.adafruit.com/2022/01/06/qt-py-bluefruit-routin-party/

Now we’ve got the QT Py SAMD21, RP2040 and ESP32-S2 designed and fabricated, we’re going to follow up with an NRF52840 version! We’ve been using the Nordict nRF series for a loooooong time (anyone else remember the nRF8001? it was like the AT90S2313 of bluetooth le for us). nRF52840 is the first one with native USB – and its plenty fast as a Cortex M4 at 64MHz and 256K of RAM. we already did a module-less route of this chip on the Circuit Playground Bluefruit so we know the schem capture is right.



QT Py ESP32-S3 is also next https://blog.adafruit.com/2022/01/07/qt-py-with-esp32-s3/
this is a swap-out of the ESP32-S2 QT Py for the new ESP32-S3 chip. The S3 is really a nice piece of kit – dual core is back and it also re-adds BLE. It’s basically an ESP32 with native USB, we’re looking forward to it! note that the S3 chip looks a lot like the S2 but the chip pinout is NOT the same, the reset, and some power pins have moved. and some gpio shifted down one. also, looks like the dual DAC was removed. anyways, just watch out don’t think you can use the exact same layout. we had to shift a few parts but it all still looks like it fits! top part is identical to the S2 QT Py, and the bottom only shifted a few passives around. we’ll get some 4 layer prototypes on order. 


Desk of Lady Ada https://www.youtube.com/watch?v=xC7oodxTWgE  1/9/2022 
This weekend we cranked through 3.5 QT Py designs (we didnt finish routing one, its a toughie!) - we already make SAMD21, RP2040 and ESP32-S2 and we wanted to add some more chips to the mix: ESP32-S3 (dual core version of the S2), ESP32 Pico (OG ESP with built in flash/psram), ESP32-C3 (Risc-V wifi!) and nRF52840 (BLE wonder-chip from Nordic). the last one is what we didn't get to finish routing because its a particularly tough one. The other 3 worked out fine with a 4 layer PCB. We also designed a few 'BFF' boards - that fit onto a QT Py like a shield. 


https://blog.adafruit.com/2022/01/15/feather-huzzah-esp32-v2/
The Feather ESP32 is a classic Adafruit board, used in thousands and thousands of projects. And we love it so…but with the CP2104 going EOL and requiring us to do a light re-spin for the CP2102N revision, we thought maybe we’d do a gut renovation. With the new ESP32 PICO module, we save a ton of space AND have 8 MB Flash / 2MB PSRAM instead of the WROOM’s 4 MB Flash & no PSRAM. the PICO is also much smaller, so we have room to upgrade the USB micro B to Type C, add a NeoPixel, STEMMA QT with separate LDO, and even a user button on the very last unused input pin. However, we did have to shuffle a few pins around. the named pins got some changes, so for example, RX and TX used to be 16 and 17 respectively – but those pins are used internally on the PICO module so they’re no longer available. on the V2 feather they’re now 8 and 9. all of the analog pins and the numbered pins are the same, just SPI/I2C/UART named pins are different. that should make code be ‘drop in replacement’ as long as the named pins/ports are used instead of the underlying io pad names. since code needs to be recompiled for the variant, this would be a fully new product ID. however, i think for the bump in capabilities and capacity it is worth an upgrade! Coming soon!


## RP2040 
https://www.cytron.io/index.php?route=product/product&product_id=44150&r=1
https://store-usa.arduino.cc/products/arduino-nano-rp2040-connect-with-headers



https://github.com/adafruit/PrettyPins
CSV files for Adafruit pin out diagrams - only needed to be done once per chip



# Choosing a Board

[Go to Choosing a Board](choosing_a_board.md)

<div>
<a href="./choosing_a_board/" class="btn btn-primary" role="button">Go to Choosing a Board</a>
</div>

