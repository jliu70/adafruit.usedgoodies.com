# CircuitPython

Python continues to be increasingly used for microcontroller projects.

The majority of [Adafruit hardware](../hardware/index.md) can run either

- [Arduino](https://arduino.cc) 

    or 

- [CircuitPython](https://circuitpython.org)  

Some [Adafruit hardware](../hardware/index.md) is also compatible with [MakeCode](https://makecode.org).


This website will focus on CircuitPython which is a version of python for microcontrollers recommended for beginners who are just getting started.  [Adafruit](https://www.adafruit.com) is the principle backer for [CircuitPython](https://circuitpython.org).  

!!! note
    *A Beginner's Recommendation*.

    **CircuitPython**


I recommend [CircuitPython](https://circuitpython.org) over Arduino for beginners because `python` is a more accesible programming language than `C++` (which is what Arduino uses).  Python syntax is more similar to plain language, and Python gives beginners an easier feedback loop as Python code does not need to be compiled in the way that C++ (Arduino) code requires.

[What is CircuitPython?](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/what-is-circuitpython)



https://learn.adafruit.com/adafruit-circuit-playground-bluefruit

Adafruit has a great walkthrough on how to [get started with CircuitPython with Raspberry Pi Pico](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/micropython-or-circuitpython)

## What about Micropython?
CircuitPython is a fork of Micropython.
while CircuitPython looks somewhat like MicroPython there are some differences.
https://github.com/adafruit/circuitpython#differences-from-micropython

While I’d generally point folks towards MicroPython if they need advanced features like interrupts and threading — or complete access to the RP2040’s Programmable I/O (PIO) in Python — for library support for sensors and other breakouts I would point you to CircuitPython. It’s well supported by our friends at Adafruit.


## CircuitPython Documentation 
We are now sponsoring Read the Docs, where all of our documentation is hosted, which comes with a couple of perks. All of our docs are now ad-free. As well, I worked with our web devs to get the new docs.circuitpython.org URL set up. We’re now working to get all the libraries updated to use the new URL. 

http://docs.circuitpython.org/
