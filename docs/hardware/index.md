# Hardware

The Adafruit lingo for their hardware is quite extensive and can be confusing to someone new to the Adafruit ecosystem.  One of the primary goals of this website is to help newcomers sort through this cornicopia of terminology.


## First Adafruit Hardware for Beginners

!!! note
    *A Beginner's Recommendation*.

    **CircuitPlayground Bluefruit**

Among the many Adafruit devices, the [CircuitPlayground Bluefruit](https://learn.adafruit.com/adafruit-circuit-playground-bluefruit) is a more accesible to beginners:

- Runs [CircuitPython](https://circuitpython.org)
- Alligator clips instead of soldering
- Loaded with features: tons of sensors, accelerometers, neopixels, speaker, etc
- About the size of a Ritz cracker a
- Supported by many Adafruit learn guides as well as online tutorials such as [CircuitPython School](https://bit.ly/circuit-python-school)





## Microcontrollers

The following should be in a sub-section:

## Comprehensive list of boards supported by CircuitPython
As this website focuses on CircuitPython, all the boards currently supported by CircuitPython (Adafruit and other vendors) is available at [CircuitPython.org](https://circuitpython.org/downloads)

There are over 270 boards currently supported by CircuitPython and that list grows everyday.
The boards are listed in order of number of downloads, and it is interesting to note that the most popular board, as of Jan 2022 -- the Raspberry Pi Pico, is not even manufactured by Adafruit.


Choosing a microcontroller for a project can be overwhelming.

Here are some great Adafruit guides on how to choose a microcontroller:

https://learn.adafruit.com/choose-your-circuitpython-board

https://learn.adafruit.com/how-to-choose-a-microcontroller

https://learn.adafruit.com/best-beginner-boards-for-teachers

## Considerations for Choosing a Board
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


## Chipsets

The microcontrollers are "mini-computers".
The chips that they use are 
    SAMD21
    ESP32-S2
    ESP32-S3
    NRF52840
    RP2040



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




!!! warning
    Using absolute paths with links is not officially supported. Relative paths
    are adjusted by MkDocs to ensure they are always relative to the page. Absolute
    paths are not modified at all. This means that your links using absolute paths
    might work fine in your local environment but they might break once you deploy
    them to your production server.

## GPIO
General Purpose Input/Output 
#raspberrypi #STEM  Website reference guide to the GPIO pins:
https://pinout.xyz


# Connectors

[Go to Connectors](connectors)

<div>
<a href="connectors/" class="btn btn-primary" role="button">Go to Connectors</a>
</div>


JST 

Shields, FeatherWings, HATs, Capes… 

Shields
Example: Adafruit 16-Channel 12-bit PWM/Servo Shield - I2C interface  https://www.adafruit.com/product/1411


FeatherWings
Example:  NeoPixel FeatherWing for all Feather Boards https://www.adafruit.com/product/2945
Plugin add-on boards that provide additional features.  E.g., running motors, adding sensors, include displays, add bluetooth or WiFi capabliities.

Feather Format is an Adafruit standard format for microcontrollers (Large, comparatively for microcontrollers.  It's still pretty small compared to a Raspberry Pi or other types of SBCs) 
Alot of feather boards.  All the same size and mostly use the same standards for pins and connections.  NOTE: not all feathers run CircuitPython.

ItsyBitsy (Small)

QT Py (Tiny)



HATs
Example:  Raspberry Pi Build HAT for Lego
https://blog.adafruit.com/2021/11/12/the-raspberry-pi-build-hat-and-lego-components-at-raspberry_pis-coderdojo-piday-raspberrypi/


Capes
Example: 4.3" LCD Capacitive Touchscreen Display Cape for BeagleBone  https://www.adafruit.com/product/3396


BFF 
BFF is the placeholder name for Adafruit expansion boards for QT Py boards
https://blog.adafruit.com/2022/01/11/qt-py-bff-with-lipoly-charging-and-switch/
https://blog.adafruit.com/2022/01/11/gamer-bff-qt-py-mini-gaming-add-on/


Stemma 
Stemma QT 
