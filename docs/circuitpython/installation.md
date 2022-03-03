# Installation

Adafruit has [great documentation](https://learn.adafruit.com/welcome-to-circuitpython) for CircuitPython.

This page tries to supplement the existing documentation by providing a quick overview and a summary of the overall process.

Other documentation listed at [Additional Referernces](index.md#additional-references)


## CircuitPython installation has two general steps:

1. Installing the CircuitPython UF2 image onto your device
2. Installing additional CircuitPython Libraries as needed

## I. CircuitPython UF2 Image

Installation of CircuitPython via CircuitPython UF2 image installation is a simple drag-and-drop operation because Adafruit devices usually support USB mode.

When you connect the microcontroller to your computer via a USB cable, it will appear on your computer as a USB drive.

!!! warning
    Make sure that the cable you use is a USB **data** cable.  If you are using a USB charging cable, the device will not be mounted on your system as a USB drive.


### UF2 Steps 

1. Download UF2 image for your board
    - Go to [CircuitPython Downloads](https://circuitpython.org/downloads) site and click on your board
    - NOTE: if your board does not appear on the list, then it probably does not support CircuitPython.  The majority of Adafruit devices support CircuitPython.
2. Place your device into bootloader mode 
    - Refer to documentation for your device as this process varies
3. Drag and drop the UF2 file you downloaded in the first step to your device via the mounted Bootloader USB drive 
    - The name of the mounted Bootloader drive varies.  For example, the `Raspberry Pi Pico` bootloader drive is named `RPI-RPI2`)
    - If the copy is successful, you should see the Bootloader drive automatically unmount, and then a new drive usually named `CIRCUITPY` will automatically mount


If the above three steps are done successfully, you are done!  You can start coding with CircuitPython on your device.  Thereafter when you reconnect your device to your computer, it should automatically been seen as a USB drive named `CIRCUITPY`.   You will no longer see the bootloader disk mounted unless you place the device into bootloader mode -- usually you will only go to the bootloader mode to upgrade CircuitPython. 

Located on your `CIRCUITPY` drive folder, the main starter program is `code.py` 

Use any editor of your choice  --  saved changes to `code.py` run immediately.

!!! note
    *A Beginner's Recommendation*.

    **Mu Editor**

While you may use any editor of your choice the [Mu Editor](https://codewith.mu/en/download) is a great editor for beginners.
There are versions for Windows, Mac OS, and Linux.

- When you first run Mu Editor, it should prompt you to pick a mode
    - You may pick the mode for "CircuiPython".  
        - The advantage to "CircuitPython mode" is that the Mu Editor will let you access the Serial Console where you can interact with the REPL (Read Eval Print Loop) 

 
#### Additional References

- Great video walkthrough of the process: [CircuitPython School - CircuitPython Installation](https://www.youtube.com/watch?v=Wa1E8ze3v04&list=PL9VJ9OpT-IPSsQUWqQcNrVJqy4LhBjPX2&index=2)

- Another great video walkthrough of the process: [DroneBot Workshop - CircuitPython with Raspberry Pi Pico](https://www.youtube.com/watch?v=07vG-_CcDG0)



## II. CircuitPython Libaries

Once you have CircuitPython installed on your device, you can start coding in CircuitPython immediately.
However, once your code makes calls beyond the libraries included with the binary install  -- most commonly after you attach sensors or other breakouts to the microcontroller -- you will need the following additional steps: 

- Download the CircuitPython Library Bundle
- Copy additional libraries to the microcontroller

The full CircuitPython Library Bundle is around 3.5MB compressed.

- Since the storage available on most microcontrollers is limited
    - There is often not enough capacity to store the complete CircuitPython Library bundle
    - Only copy additional libraries individually based upon the sensors, components and other breakouts you attach

As of Feb 15, 2022, the number of CircuitPython libraries is 344!


### The main options for copying additional libraries onto the microcontroller are:

- For Adafruit Learn Guides:  [Bundlefly](../glossary/bundlefly.md)
- Manual
- Using a tool (I highly recommend `circup`)

### Bundlefly  

!!! note
    *A Beginner's Recommendation*.

    **[Bundlefly](../glossary/bundlefly.md)**

    All CircuitPython Adafruit Learn Guides now have a feature called [Bundlefly](../glossary/bundlefly.md) which will allow users to download one zip file which includes the code, all required libraries, and if needed, asset files.
    
    Find the download link called `Download Project Bundle` located at the beginning of any CircuitPython code section.

    Once you have extracted all the files from the downloaded zip file, you just drag-and-drop them onto your microntroller CIRCUITPY drive.


### Manual  

1. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries)
    - !!! warning
        Make sure to download the bundle that matches the major version of your CircuitPython 
    - Unzip the bundle, then drag and drop the individual libraries you need

!!! note
    Most Adafruit learn guides and other 3rd party tutorials reference the manual method.


### Using a tool: circup 

[Circup](https://circup.readthedocs.io/en/latest/) is a great way to install CircuitPython libraries and keep all your CircuitPython libraries up to date.

While `circup` does require some intial setup, you should only need to do the setup once.

Circup usage is very similar to python `pip`.

!!! note
    IMHO using `circup` is vastly superior to copying CircuitPython libraries manually, but it does require the user to be comfortable with the command line.

**Circup Advantages**

- No need to manually: 
    - Download the CircuitPython Bundle Library zip file
    - Extract the bundle zip file
    - Drag and drop individual libraries to the microcontroller
- Install individual libraries by name or a list of libraries in a text file.
- Generate a list of libraries currently installed on your device with the `freeze` option. (see below for more info)


I first learned about `circup` from one of John Park's CircuitPython Parsec videos: 

- [Adafruit Blog on John Park's CircuitPython Parsec:  CircUp  CircuitPython Updater](https://blog.adafruit.com/2021/09/17/john-parks-circuitpython-parsec-circup-adafruit-johnedgarpark-adafruit-circuitpython/)  
- [Video: John Park's CircuitPython Parsec: Circup CircuitPython Updater](https://www.youtube.com/watch?v=TXKoDqLprgY)   (9/17/2021)


#### Circup Initial Setup - only need to run once

**Pre-requisite**

- Have a working Python3 installation on your computer.
    - For Windows, best to download [python](https://www.python.org/downloads/windows/) and install.
    - For Mac, you have options such as 
        - [homebrew](https://docs.brew.sh/Homebrew-and-Python) 
        - [Command Line Tools (must have an Apple ID)](https://stackoverflow.com/questions/68011799/how-to-install-python-3-8-required-to-be-downloaded-from-xcode-command-line-to) (what I use)
    - For Linux, check your distro documentation for info on how to install Python3 (if not already installed)

I recommend to install circup via a python virtual environment.

Although if you prefer, you may skip the virtual environment creation and directly `pip install circup` onto your computer.

**Create Python Virtual Environment** (optional - skip to **Install Circup** if you don't want to use a virtual environment)

On a Mac:
```
python3 -m venv ~/.virtualenvs/circup
```
On Linux:
```
python3 -m venv ~/.virtualenvs/circup
```

On Windows:

Pre-requisites

- Install Python on your computer

```
python -m venv ~/.virtualenvs/circup
```

**Activate Virtual Environment**

Mac and Linux
```
. ~/.virtualenvs/circup/bin/activate
```

Windows
```
source ~/.virtualenvs/circup/Scripts/activate
```


**Install Circup**

On all platforms:
```
pip install circup
```

On Mac/Linux if you did not use a virtual environment:
```
pip3 install circup
```

#### Circup Usage

NOTE: If using a python virtual environment, before you can call circup, you will first need to activate the virtual environment. (see **Activate Virtual Environment** above)

**Command Examples**

- Circup install a library

```
circup install adafruit_debouncer
```
- Circup remove a library

```
(circup) jliu@JEFFREYs-MBP ~ % circup uninstall adafruit_debouncer
Found device at /Volumes/CIRCUITPY, running CircuitPython 6.3.0.
A newer version of CircuitPython (7.0.0) is available.
Get it here: https://circuitpython.org/downloads
Uninstalled 'adafruit_debouncer'.
```

- Circup install list of libraries from a text file 

```
(circup) jliu@JEFFREYs-MBP /Volumes/CIRCUITPY/lib % circup install -r ../requirements.txt
Found device at /Volumes/CIRCUITPY, running CircuitPython 6.3.0.
A newer version of CircuitPython (7.0.0) is available.
Get it here: https://circuitpython.org/downloads
Searching for dependencies for: ['a newer version of circuitpython (7.0.0) is available.', 'adafruit_debouncer', 'found device at /volumes/circuitpy, running circuitpython 6.3.0.', 'get it here: https://circuitpython.org/downloads']
WARNING:
    a newer version of circuitpython (7.0.0) is available. is not a known CircuitPython library.
WARNING:
    found device at /volumes/circuitpy, running circuitpython 6.3.0. is not a known CircuitPython library.
WARNING:
    get it here: https://circuitpython.org/downloads is not a known CircuitPython library.
Ready to install: ['adafruit_debouncer']
  

Installed 'adafruit_debouncer'.
```

- Circup create list of libraries from installed libraries on microcontroller
    - Similar to the `pip freeze` command. 
    - NOTE: Instead of the `freeze` option, you may also manually create a text file with a list of libraries.

```
circup freeze > requirements.txt
```


- Circup update existing libraries
```
circup update
```


#### Circup Miscellaneous Info

- Circup bundles-show
```
(circup) jliu@JEFFREYs-MBP ~ % circup bundle-show
adafruit/Adafruit_CircuitPython_Bundle
 https://github.com/adafruit/Adafruit_CircuitPython_Bundle
 version = 20210921
adafruit/CircuitPython_Community_Bundle
 https://github.com/adafruit/CircuitPython_Community_Bundle
 version = 20210921
circuitpython/CircuitPython_Org_Bundle
 https://github.com/circuitpython/CircuitPython_Org_Bundle
 version = 0.0.3
``` 
[Github Issue requesting support for community bundle and future bundles](https://github.com/adafruit/circup/pull/110)


- Circup bundles by default are downloaded to User's `DATA_DIR/circup` 

NOTE:  Mac default `DATA_DIR/circup` directory is  `~/Library/Application\ Support/circup`
```
(circup) % ls -lrt ~/Library/Application\ Support/circup
total 35752
-rw-r--r--  1 jliu  staff  11320 Sep 21 11:55 circuitpython-org-bundle-py.zip
-rw-r--r--  1 jliu  staff   5506 Sep 21 11:55 circuitpython-org-bundle-6mpy.zip
-rw-r--r--  1 jliu  staff   4992 Sep 21 11:55 circuitpython-org-bundle-7mpy.zip
drwxr-xr-x  5 jliu  staff  160 Sep 21 11:55 circuitpython
-rw-r--r--  1 jliu  staff  4531939 Dec  5 10:25 adafruit-circuitpython-bundle-6mpy.zip
-rw-r--r--  1 jliu  staff  1398845 Dec  5 10:25 circuitpython-community-bundle-py.zip
-rw-r--r--  1 jliu  staff   866768 Dec  5 10:25 circuitpython-community-bundle-6mpy.zip
-rw-r--r--  1 jliu  staff   655732 Dec  5 10:25 circuitpython-community-bundle-7mpy.zip
-rw-r--r--  1 jliu  staff  7197908 Jan  1 19:44 adafruit-circuitpython-bundle-py.zip
-rw-r--r--  1 jliu  staff  3607698 Jan  1 19:44 adafruit-circuitpython-bundle-7mpy.zip
drwxr-xr-x  8 jliu  staff  256 Jan  1 19:44 adafruit
-rw-r--r--  1 jliu  staff  160 Jan  1 19:44 circup.json

(circup) jliu@JEFFREYs-MBP ~/Library/Application Support/circup  % du -sh .
 51M   .
```

Config file `circup.json`
```
% find ~ -name circup.json
/Users/jliu/Library/Application Support/circup/circup.json
```

Circup help
```
(circup) jliu@JEFFREYs-MBP ~  % circup --help
Usage: circup [OPTIONS] COMMAND [ARGS]...

  A tool to manage and update libraries on a CircuitPython device.

Options:
  --verbose         Comprehensive logging is sent to stdout.
  --path DIRECTORY  Path to CircuitPython directory. Overrides automatic path
                    detection.
  --version         Show the version and exit.
  --help            Show this message and exit.

Commands:
  bundle-add     Add bundles to the local bundles list, by "user/repo"...
  bundle-remove  Remove one or more bundles from the local bundles list.
  bundle-show    Show the list of bundles, default and local, with URL,...
  freeze         Output details of all the modules found on the connected...
  install        Install a named module(s) onto the device.
  list           Lists all out of date modules found on the connected...
  show           Show a list of available modules in the bundle.
  uninstall      Uninstall a named module(s) from the connected device.
  update         Update modules on the device. Use --all to automatically
                 update all modules without Major Version warnings.

```

#### Circup Resources
- [Circup documentation](https://circup.readthedocs.io/en/latest/)
- [Circup Github repo](https://github.com/adafruit/circup)
- [Adafruit Learn Guide: Circup](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/)



<small>This page was last updated on 2022-03-03 12:51:07 -0500.</small>