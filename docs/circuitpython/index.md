# CircuitPython

The majority of [Adafruit hardware](../hardware/index.md) can run either

- [Arduino](https://arduino.cc) 

    or 

- [CircuitPython](https://circuitpython.org)  

- Some [Adafruit hardware](../hardware/index.md) is also compatible with [MakeCode](https://makecode.org).

!!! note
    *A Beginner's Recommendation*.

    **CircuitPython**

## What is CircuitPython?

This website focuses on CircuitPython which is a version of python for microcontrollers.  [Adafruit](https://www.adafruit.com) is the principle backer for [CircuitPython](https://circuitpython.org).  


I recommend [CircuitPython](https://circuitpython.org) over Arduino for beginners because:

- Python is a more accesible programming language than `C++` (which is what Arduino uses). 
    - Python syntax is more similar to plain language
- Python gives beginners an easier and quicker feedback loop 
    - Python code does not need to be compiled in the way that C++ (Arduino) code requirees.
        - With CircuitPython, the code is stored and run directly on the microcontroller, aka "click save and your code starts running" 
    - Arduino code requires the traditional method of:
        - Compiling code on an external device (e.g., your laptop)
        - Downloading the compiled binary to the microcontroller through the Arduino IDE
        - Debugging the code
        - Watching the output

Because of these and other reasons, Python continues to be increasingly used for microcontroller projects.


## MakeCode 

!!! note
    Great for younger students, [MakeCode](https://makecode.org) is a blocked-based programming language which is similar to [Scratch](https://scratch.mit.edu).  

Block-based programming, such as [MakeCode](https://makecode.org) or [Scratch](https://scratch.mit.edu), is great for younger beginners.  Using drag-and-drop blocks avoids common syntax errors like typos or formatting issues, which can be source of frustration for new programmers.   However, the power and flexiblity of block-based programs is limited.  

Hence for older students, or those students already experienced with [Scratch](https://scratch.mit.edu) or [MakeCode](https://makecode.org), I recommend jumping straight into python.

For those looking to ease the transition from block-based programming to python, [EduBlocks](https://edublocks.org) is an interesting hybrid which offers python in a block-based format.


## What about Micropython?

[MicroPython](https://micropython.org) is an open source Python programming language interpretor that runs on small embedded development boards, aka [microcontrollers](../glossary/microcontroller.md).

- Lean and efficient implementation of Python 3 
    - Includes a small subset of Python standard library
- Optimized to run on microcontrollers

CircuitPython is a fork of Micropython.  While CircuitPython looks somewhat like MicroPython there are some [differences](https://github.com/adafruit/circuitpython#differences-from-micropython).

While I’d generally point folks towards MicroPython if they need advanced features like interrupts and threading — or complete access to the RP2040’s Programmable I/O (PIO) in Python — for library support for sensors and other breakouts I would point you to CircuitPython. It’s well supported by our friends at Adafruit.


## CircuitPython Documentation 

We are now sponsoring Read the Docs, where all of our documentation is hosted, which comes with a couple of perks. All of our docs are now ad-free. As well, I worked with our web devs to get the new docs.circuitpython.org URL set up. We’re now working to get all the libraries updated to use the new URL. 

http://docs.circuitpython.org/

Community
https://learn.adafruit.com/welcome-to-the-community


[What is CircuitPython?](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/what-is-circuitpython)

https://learn.adafruit.com/adafruit-circuit-playground-bluefruit

Adafruit has a great walkthrough on how to [get started with CircuitPython with Raspberry Pi Pico](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/micropython-or-circuitpython)


## Additional References

- [Arduino](https://arduino.cc) 
- [CircuitPython](https://circuitpython.org)
- [MakeCode](https://makecode.org) 
- [Scratch](https://scratch.mit.edu)
