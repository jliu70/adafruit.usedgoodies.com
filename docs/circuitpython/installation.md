# installation

[CircuitPython hardware binaries downloads](https://circuitpython.org/downloads)

[CircuitPython Bundle Libraries](https://circuitpython.org/libraries)



Adafruit has a great walkthrough on how to [get started with CircuitPython with Raspberry Pi Pico](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/micropython-or-circuitpython)


General steps

1. Download UF2 binaries for your board
    - Go to Downloads site and click on your board
    - download and then go into bootloader mode 
    - drag and drop the UF2 file to your device USB device
2. Download Bundle Libraries
    - Manually
        - download the bundle, unzip, then drag and drop the libraries you need
    - Via Circup
        - can create a text file, e.g., `requirements.txt`
        - run `circup install -r requirements.txt`
