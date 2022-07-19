# Hardware

The Adafruit lingo for their hardware is quite extensive and can be confusing to someone new to the Adafruit ecosystem.  One of the primary goals of this website is to help newcomers sort through this cornicopia of terminology.

Adafruit designs and sells their own custom microcontrollers, components, sensors, and more. 

## What are Microcontrollers?

Microcontrollers are single purpose computers 

- small embedded development boards
- limited storage and memory
- limited processing power


Microcontrollers vs General Purpose Computer

- Use of microcontrollers is fine for many cases
- When you need more computational power, you may want to use a [Raspberry Pi](../glossary/raspberry_pi.md)
    - For example, if you wish to have a web dashboard to interface with, then you will need to use a Raspberry Pi


For more info, see the **Glossary** page for [Microcontroller](../glossary/microcontroller.md)


## Recommended: First Adafruit Hardware for Beginners

!!! note
    *A Beginner's Recommendation*.

    **[Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit)**

Among the many Adafruit devices, the [Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit) is more accesible to beginners.  It is a great piece of hardware to start with.

For more info, see the **Glossary** page for [Circuit Playground Bluefruit](../glossary/circuit_playground#circuit-playground-bluefruit)



## List of hardware supported by CircuitPython
List of all the hardware currently supported by CircuitPython (Adafruit and other manufacturers) is available at the [CircuitPython Downloads Page](https://circuitpython.org/downloads).

As of May 2022 

- There are over 300 boards supported by CircuitPython and that list grows everyday.
- The list is sorted by number of downloads.  
    - The most popular board -- the Raspberry Pi Pico -- is not manufactured by Adafruit.

### Adafruit Hardware

Adafruit offers over 70 different microcontrollers which run CircuitPython.

#### Within the Adafruit ecosystem, the primary microcontroller form factors are:

- [Circuit Playground](../../glossary/circuit_playground) 
- [Adafruit Feather](../glossary/feather.md) (Regular)
    - Supported by an extensive array of expansion options called [FeatherWings](../glossary/feather.md#featherwing)
- [ItsyBitsy](../glossary/itsy_bitsy.md) (Small)
- [QT Py](../glossary/qt_py.md) (Tiny)
- [Metro](../glossary/metro.md) (Arduino form factor)
- Trinkey (USB dongles)

#### Other form factors: 

- [CLUE](../glossary/clue.md)
- Gemma M0 (tiny - great for wearble projects)
- FunHouse (home automation)
- KB2040 (custom keyboards)
- MacroPad (custom macrokeypad)
- MagTag (e-ink display with WiFi)
- MatrixPortal (power LED Matrix displays - has WiFi)
- PyBadge/EdgeBadge/PyGamer 
- PyPortal/PyPortal Titano (an [IoT](../glossary/iot.md) display)
- Trellis 
- Trinket M0
- [Teensy](../glossary/teensy.md)


## Chipsets

Most Adafruit devices use one of the following chipsets: 

- SAMD21
- SAMD51
- [ESP32-S2](../glossary/esp32.md)
- [ESP32-S3](../glossary/esp32.md)
- [ESP32-C3](../glossary/esp32.md)
- NRF52840
- [RP2040](../glossary/rp2040.md)

There are features and advantages to each chipset, so there are often multiple versions of a particular Adafruit form factor based upon different chipsets.

For example:

- [Circuit Playground Versions](../glossary/circuit_playground/#circuit-playground)
- [QT Py Versions](../glossary/qt_py/#qt-py)

- [In general would recommend new users to avoid SAMD21 microcontrollers](https://forums.adafruit.com/viewtopic.php?f=60&t=189584)
```
The SAMD21 has limited flash space for including new features in CircuitPython. The non-Express versions are extra crunched because 64k of the flash is used for the file system.
```


## Expansion Options

Most microcontroller form factors have expansion boards which can extend functionality.

These expansion boards are often given "codenames" such as "[FeatherWing](../glossary/feather.md#featherwing)" or "[HAT](../glossary/hat.md)"

There are a wide variety of names for add-on boards.

- [Feather boards](../glossary/feather.md) use [FeatherWings](../glossary/feather.md#featherwing)
- [Arduinos](../glossary/arduino.md) use [Shields](../glossary/shield.md)
- [Raspberry Pi SBCs](../glossary/raspberry_pi.md) use [HATs](../glossary/hat.md)
- [QT Py](../glossary/qt_py.md) use [BFFs](../glossary/qt_py.md#bff)
- [BeagleBone boards](https://beagleboard.org) use [Capes](../glossary/cape.md)
- [Circuit Playground Express](../glossary/circuit_playground.md) use Gizmos
- Raspberry Pi Pico use [Bells](../glossary/bell.md)


Pretty Pins - pin out diagrams for Adafruit hardware

[CSV files for Adafruit pin out diagrams](https://github.com/adafruit/PrettyPins) - only needed to be done once per chip



# Choosing a Board

[Go to Choosing a Board](choosing_a_board.md)

<div>
<a href="./choosing_a_board/" class="btn btn-primary" role="button">Go to Choosing a Board</a>
</div>


<small>This page was last updated on 2022-07-19 13:03:07 -0500.</small>
