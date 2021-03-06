
# Blinka

### [Back to Index](index.md)

*Related* [microcontroller](microcontroller.md), [CircuitPython](../circuitpython/index.md)

WIP 

Blinka, our CircuitPython library compatibility layer for Single Board Computers, or SBCs. 


More techincal guides on how to add SBC to Blinka:

First step
https://learn.adafruit.com/adding-a-single-board-computer-to-platformdetect-for-blinka

Second step
https://learn.adafruit.com/adding-a-single-board-computer-to-blinka




Ordered 1/20/2021 - Delivered 1/23/2021
NOTE: there's a related article https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico
- [ ] MCP2221A USB I2C/GPIO Breakout Breakout board to use Stemma  QT or Grove Sensors on your computer directly via usb  
Delivered 1/23/2021
Adafruit MCP2221A breakout board  https://www.adafruit.com/product/4471  $6.50 
    - [ ] NOTE: before you install Blinka libraries - use venv  Mac: `python3 -m venv .virtualenvs/mcp2221` or on Windows: `python -m venv .virtualenvs/mcp2221`
        Blinka brings CircuitPython APIs and CircuitPython libraries to single board computers (SBCs). It is a pip installable Python library that runs in normal “desktop” Python. One can port their microcontroller code to an SBC or visa versa!
    CircuitPython Libraries on any Computer with MCP2221  https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221
    Update Blinka/Platform Libraries  -  Most issues can be solved by forcing Python to upgrade to the latest`blinka`/`platform-detect`libraries.   On Raspberry Pi, try running: `sudo python3 -m pip install --upgrade --force-reinstall adafruit-blinka`.   On my Mac just run `pip install --upgrade --force-reinstall adafruit-blinka`
    CircuitPython Libraries and Jupyter Notebook on any Computer with MCP2221  https://learn.adafruit.com/jupyter-on-any-computer-with-circuitpython-libraries-and-mcp2221
    Learn: Google Docs Sensor Logging From Your PC  https://learn.adafruit.com/gdocs-sensor-logging-from-your-pc
    JPs Product Pick of the Week 1/12/21 MCP2221A USB I2C/GPIO Breakout https://youtu.be/_nNe-YM7MCU?t=261
- [ ] Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic  https://www.adafruit.com/product/938  $19.95  (two)
https://learn.adafruit.com/monochrome-oled-breakouts
 
Learn: CircuitPython BLE Libraries on Any Computer  https://learn.adafruit.com/circuitpython-ble-libraries-on-any-computer
The Adafruit[Blinka bleio library](https://github.com/adafruit/Adafruit_Blinka_bleio)makes this possible. It is a regular Python library that runs on desktop Python, not on CircuitPython boards. It re-implements the`_bleio`module that is part of CircuitPython: all our BLE libraries are ultimately based on`_bleio`.
**The Blinka bleio library only supports acting in a BLE central role.**You can connect to peripheral devices, such as heart rate monitors, pulse oximeters, bicycle sensors, etc., but you cannot act as a peripheral yourself with this code.

For Mac
NOTE: pre-requisite is command line tools for python3 
```python
python3 -m venv .virtualenvs/mcp2221
. .virtualenvs/mcp2221/bin/activate
pip install hidapi
pip install --upgrade --force-reinstall adafruit-blinka
(mcp2221) jliu@JEFFREYs-MBP ~ % pip install adafruit-circuitpython-ahtx0
export BLINKA_MCP2221="1"

(mcp2221) jliu@JEFFREYs-MBP ~  % python
Python 3.7.3 (default, Apr 24 2020, 18:51:23) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import board
>>> dir(board)
['G0', 'G1', 'G2', 'G3', 'I2C', 'SCL', 'SDA', 'SPI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ap_board', 'board_id', 'detector', 'pin', 'sys']
>>> exit()
```

For Windows
```python
PS C:\Users\jeffrey.liu> python --verison
Python 3.9.2

python -m venv .virtualenvs/mcp2221

# NOTE: recall that git bash python cli repl just hangs and does not load - so open Powershell window instead
PS C:\Users\jeffrey.liu> .virtualenvs\mcp2221\Scripts\activate.ps1
pip install hidapi
pip install --upgrade --force-reinstall adafruit-blinka
pip install adafruit-circuitpython-ahtx0
$env:BLINKA_MCP2221="1"
    
python
Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import board
>>> dir(board)
['G0', 'G1', 'G2', 'G3', 'I2C', 'SCL', 'SDA', 'SPI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'ap_board', 'board_id', 'detector', 'pin', 'sys']
>>> exit()
```

For Windows upgrade adafruit-blinka output:
```
PS C:\Users\jeffrey.liu> .virtualenvs\mcp2221\Scripts\activate.ps1

(mcp2221) PS C:\Users\jeffrey.liu> pip list

Package                 Version
----------------------- -------
Adafruit-Blinka         6.2.2
Adafruit-PlatformDetect 3.1.1
Adafruit-PureIO         1.1.8
hidapi                  0.10.1
pip                     20.2.3
pyftdi                  0.52.9
pyserial                3.5
pyusb                   1.1.1
setuptools              49.2.1

WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\jeffrey.liu\.virtualenvs\mcp2221\scripts\python.exe -m pip install --upgrade pip' command.


(mcp2221) PS C:\Users\jeffrey.liu> pip install --upgrade --force-reinstall adafruit-blinka

Collecting adafruit-blinka
  Downloading Adafruit-Blinka-6.3.0.tar.gz (118 kB)
Collecting Adafruit-PlatformDetect>=3.1.0
  Downloading Adafruit-PlatformDetect-3.2.0.tar.gz (29 kB)
Collecting Adafruit-PureIO>=1.1.7
  Using cached Adafruit_PureIO-1.1.8.tar.gz (26 kB)
Collecting pyftdi>=0.40.0
  Using cached pyftdi-0.52.9-py3-none-any.whl (139 kB)
Collecting pyserial>=3.0
  Using cached pyserial-3.5-py2.py3-none-any.whl (90 kB)
Collecting pyusb>=1.0.0
  Using cached pyusb-1.1.1-py3-none-any.whl (58 kB)
...
...
...
  Attempting uninstall: adafruit-blinka
    Found existing installation: Adafruit-Blinka 6.2.2
    Uninstalling Adafruit-Blinka-6.2.2:
      Successfully uninstalled Adafruit-Blinka-6.2.2
    Running setup.py install for adafruit-blinka ... done
Successfully installed Adafruit-PlatformDetect-3.2.0 Adafruit-PureIO-1.1.8 adafruit-blinka-6.3.0 pyftdi-0.52.9 pyserial-3.5 pyusb-1.1.1

WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\jeffrey.liu\.virtualenvs\mcp2221\scripts\python.exe -m pip install --upgrade pip' command.

(mcp2221) PS C:\Users\jeffrey.liu> pip list

Package                 Version
----------------------- -------
Adafruit-Blinka         6.3.0
Adafruit-PlatformDetect 3.2.0
Adafruit-PureIO         1.1.8
hidapi                  0.10.1
pip                     20.2.3
pyftdi                  0.52.9
pyserial                3.5
pyusb                   1.1.1
setuptools              49.2.1

WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.

You should consider upgrading via the 'c:\users\jeffrey.liu\.virtualenvs\mcp2221\scripts\python.exe -m pip install --upgrade pip' command.
```




   
- [ ] A brief history of microcontrollers and a Great demo by Ladyada for using CircuitPython and Blinka to connect to a temperature sensor three ways (Raspberry Pi Pico, Raspberry Pi 4, and MCP2221A) https://www.youtube.com/watch?v=jZnDCs80b_A&t=3405s  1/31/2021
Reference:  Page 48 of  RPi_Pi Pico_Digital Edition.pdf
NOTE: UTIME VS TIME
If you’ve programmed in Python before, you’ll be used to using the ‘time’ library.  The utime library is a version designed for microcontrollers like the Pico – the ‘u’ standing for ‘μ’, the Greek letter ‘mu’, which is used as a shorthand for ‘micro’.  If you forget and use import time, don’t worry: MicroPython will automatically use the utime library instead.

Raspberry Pi Pico code
```python
import time
import board
import busio
import adafruit_ahtx0

i2c_bus = busio.I2C(board.GP1, board.GP0)

sensor = adafruit_ahtx0.AHTx0(i2c_bus)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Temperature: %0.1f F" % ((sensor.temperature * 1.8)+32))
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
```
Raspberry Pi 4 code
```python
import time
import board
# note import busio not needed for Raspberry Pi
import adafruit_ahtx0

# create the sensor object using I2C
sensor = adafruit_ahtx0.AHTx0(board.I2C())

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Temperature: %0.1f F" % ((sensor.temperature * 1.8)+32))
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
```
MCP2221 code
```python
import time
import board
import busio
import adafruit_ahtx0

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Temperature: %0.1f F" % ((sensor.temperature * 1.8)+32))
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
```
MCP2221 code without busio
```python
import time
import board
import adafruit_ahtx0

# Create library object using our Bus I2C port
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Temperature: %0.1f F" % ((sensor.temperature * 1.8)+32))
    print("\nHumidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
```
Ordered 2/6/2021 - Delivered 2/17/2021
- [ ] AHT20 Temperature & Humidity Sensor breakout https://www.adafruit.com/product/4566  $4.50
Learn:  Adafruit AHT20 Temperature & Humidity Sensor   https://learn.adafruit.com/adafruit-aht20

Sample output:
```
(mcp2221) jliu@JEFFREYs-MBP ~ % python test.py

Temperature: 24.2 C
Humidity: 29.6 %


Temperature: 24.1 C
Humidity: 29.7 %


Temperature: 24.1 C
Humidity: 29.8 %


Temperature: 24.0 C
Humidity: 29.9 %

^CTraceback (most recent call last):
 File "test.py", line 13, in &lt;module&gt;
 time.sleep(2)
KeyboardInterrupt
```




NOTE: there's a related article https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-raspberry-pi-pico
- [ ] FT232H General Purpose USB to I2C,  SPI, GPIO Breakout board to use Stemma  QT or Grove Sensors on your computer directly via usb  https://www.adafruit.com/product/2264  $15
Delivered 10/27/2021
    CircuitPython Libraries on any Computer with FT232H https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h
    The support for the FT232H in Blinka utilizes the[pyftdi library](https://pypi.org/project/pyftdi/)by[eblot](https://pypi.org/user/eblot/). This in turn relies on a few other things, like libusb. So before we can actually use the FT232H, we need to get everything setup. See the OS specific sections for what we went through to get things working for each.
NOTE: 10/28/2021  useless on Mac OS unless you use homebrew python.  Bleh!

Mac OS:
```python
pip install --upgrade pip

pip install libusb pyftdi adafruit-blinka

pip install --upgrade --force-reinstall adafruit-blinka
        
(ft232h) jliu@JEFFREYs-MBP ~ % pip list
Package  Version
Adafruit-Blinka  6.15.0
Adafruit-PlatformDetect 3.17.1
Adafruit-PureIO  1.1.9
libusb 1.0.23b7
pip  21.3.1
pyftdi 0.53.3
pyserial 3.5
pyusb  1.2.1
setuptools 58.3.0
        
        
export BLINKA_FT232H=1

import board




>>> import board

Traceback (most recent call last):

 File "&lt;stdin&gt;", line 1, in &lt;module&gt;

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/board.py", line 40, in &lt;module&gt;

 from adafruit_blinka.agnostic import board_id, detector

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/adafruit_blinka/agnostic/__init__.py", line 18, in &lt;module&gt;

 chip_id = detector.chip.id

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/adafruit_platformdetect/chip.py", line 79, in id

 count = len(UsbTools.find_all([(0x0403, 0x6014)]))

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/pyftdi/usbtools.py", line 95, in find_all

 devs.update(UsbTools._find_devices(vid, pid, nocache))

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/pyftdi/usbtools.py", line 597, in _find_devices

 backend = cls._load_backend()

 File "/Users/jliu/.virtualenvs/ft232h/lib/python3.8/site-packages/pyftdi/usbtools.py", line 663, in _load_backend

 raise ValueError('No backend available')

ValueError: No backend available

>>> exit()

```    
https://forums.adafruit.com/viewtopic.php?f=8&t=182556&p=887762&hilit=ft232h+ValueError%3A+No+backend+available#p887762
    https://github.com/pyusb/pyusb/issues/355
https://forums.adafruit.com/viewtopic.php?f=19&t=182685
```
"No backend available" error while testing the install, be sure you have installed your version of Python3 via Homebrew, otherwise the pyftdi and adafruit-blinka libraries will not be able to find the libusb package that you installed with Homebrew.
```
So the conclusion is that the FT232H is useless on the Mac unless you use Homebrew.  Bleh!  






Forum question I posted regarding busio:  https://forums.adafruit.com/viewtopic.php?f=60&t=175971&p=857191#p857191
Very thorough responses there on how "import board" automagically sets to the default board.SCL and board.SDA for both Blinka and for firmware.
Blinka:  https://github.com/adafruit/Adafruit_Blinka/blob/813d634f2ca50a93fa6dfb53e18aa09403be2440/src/board.py#L213
C code (firmware):  https://github.com/adafruit/circuitpython/blob/b69cb0144ca0d54011be540213d1e25e673a63de/shared-module/board/__init__.c#L57

In a nutshell:
```python
i2c = board.I2C()
```
is always a shortcut for 
```python
import busio

i2c = busio.I2C(board.SCL, board.SDA)
```

Verifies that if one wanted to be lazy, one could just rely on the board library to define the default SCL and SDA.  
  
It seems that if you want to define different I2C buses, you would use the busio library to define that (if the hardware could support it).
Hypothetical code:
```python
import board  
import busio  
  
i2c = busio.I2C(board.SCL, board.SDA)  
i2c1 = busio.I2C(board.SCL1, board.SDA1)  
  
i2c.try_lock()  
i2c.scan()  
  
i2c1.try_lock()  
i2c1.scan()
```
References
https://forums.adafruit.com/viewtopic.php?f=8&t=167829&start=15
https://www.raspberrypi.org/forums/viewtopic.php?t=33092
https://www.raspberrypi.org/forums/viewtopic.php?t=271200
https://randomnerdtutorials.com/esp32-i2c-communication-arduino-ide/
https://www.digikey.com/en/maker/projects/circuitpython-basics-i2c-and-spi/9799e0554de14af3850975dfb0174ae3
NOTE: As of 3/2021, confirmed `i2c = board.I2C()` works on QT Py, but it does not work on Raspberry Pi Pico.
Pico generates the error:
```python
AttributeError: 'module' object has no attribute 'I2C'
```
That's because the library doesn't define a default for the Pico:  https://github.com/adafruit/circuitpython/issues/4121
You'll need to manually define via busio.I2C the board GPIO pins you are using.  
```python
i2c = busio.I2C(board.GP1, board.GP0)
```

NOTE: CircuitPython School also has a great blurb on busio 
https://youtu.be/rSF_b8ab2gU?t=685
Creating an I2C object for use with Stemma QT devices is super easy.  Just:
```python
i2c = board.I2C()
```
Some example code might refer to busio and pass in specific board.SDA and board.SCL objects.  You should not need that if you're using Stemma QT and use the statement above.  You can even avoid importing busio if you're not using it anyplace else in your code.


NOTE: 10/27/2021 - CircuitPython School video "Don't Stand So Close to Me" has a great blurb regarding how QT Py RP2040 also needs to have the i2c object defined with busio when using the Stemma QT connector.  
https://youtu.be/Pn77QKCz2tM?t=918
```python
import board
import busio

i2c = busio.I2C(board.SCL1, board.SDA1)
```
Additional reference:  https://forums.adafruit.com/viewtopic.php?f=60&t=183777&p=892463&hilit=qt+py+rp2040+i2c+board.I2C#p892463
The STEMMA connector on the QTPYRP2040uses a separate set of pins for I2C  
board.SCL1 and board.SDA1  
see the guide [https://learn.adafruit.com/adafruit-qt-py-2040/pinouts#stemma-qt-3091651-3](https://learn.adafruit.com/adafruit-qt-py-2040/pinouts#stemma-qt-3091651-3)





Additional References



<small>This page was last updated on 2022-03-03 15:45:07 -0500.</small>