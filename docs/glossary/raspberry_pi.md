
# Raspberry Pi

### [Back to Index](index.md)

*Related* [GPIO](gpio.md), [HAT](hat.md)

WIP

The [Raspberry Pi](https://www.raspberrypi.com) is a SBC (Single Board Computer) produced by the [Raspberry Pi Foundation](https://raspberrypi.org).


The Raspberry Pi is a General Purpose Computer which is different from a [microcontroller](microcontroller.md) which is a single purpose computer.  A chart comparing the Raspberry Pi to an Arduino is on the [microcontroller](microcontroller.md) glossary page.



The Raspberry Pi's schematics are released, but the board itself is not open hardware. The Raspberry Pi Foundation relies on income from the sale of Raspberry Pis to do its charitable work. 
Reference:  [https://opensource.com/resources/raspberry-pi](https://opensource.com/resources/raspberry-pi)


[What is Raspberry Pi? Specs and Models (2021 Guide)   8/25/2021](https://www.freecodecamp.org/news/what-is-raspberry-pi-specs-and-models-2021-guide/)


[CircuitPython on Raspberry Pi (Bare Metal / No OS)](https://learn.adafruit.com/circuitpython-on-raspberry-pi-bare-metal-no-os)



https://learn.adafruit.com/raspberry-pi-care-and-troubleshooting/


11/10/2021
#raspberrypi  Advanced options with Raspberry Pi Imager makes it a much better choice than Balena Etcher.
https://youtu.be/hCxT0A-5_9k?t=283
Open Advanced Settings Options
```
Ctrl-shift-x
```
Then you can set hostname, enable SSH, set password for pi user, Configure WiFi,  Set Locale Settings.   Awesome!
Additional reference:   https://learn.adafruit.com/raspberry-pi-zero-creation/using-rpi-imager



## 2/24/2020
#raspberrypi  confirmed 1.2 release
https://hackaday.com/2020/02/23/raspberry-pi-slips-out-new-pcb-version-with-usb-c-power-fix/
https://news.ycombinator.com/item?id=22402211


## 2/20/2020
#raspberrypi  
https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
Improved USB-C on newer Pi4s? - Raspberry Pi Forums
https://www.raspberrypi.org/forums/viewtopic.php?t=260719

https://tutorial.cytron.io/2020/02/22/how-to-check-if-your-raspberry-pi-4-model-b-is-rev1-2/

https://www.raspberrypi.org/documentation/hardware/raspberrypi/revision-codes/README.md
`cat /proc/cpuinfo`
The last three lines show the hardware type, the revision code, and the Pi's unique serial number.

Raspberry Pi 4B 4GB 
```
c03111	4B	1.1	4GB	Sony UK
c03112	4B	1.2	4GB	Sony UK
```

Saniabox  - Raspberry Pi 4B 2GB 
```
b03112  4B   1.2  
```

Raspberry Pi 4B 4GB rev 1.1
```

processor	: 3
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 108.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xd08
CPU revision	: 3

Hardware	: BCM2711
Revision	: c03111
Serial		: 10000000032c4bda
Model		: Raspberry Pi 4 Model B Rev 1.1
```

Raspberry Pi 4B 4GB  rev 1.2
```
processor	: 3
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 108.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xd08
CPU revision	: 3

Hardware	: BCM2711
Revision	: c03112
Serial		: 10000000717e4b0e
Model		: Raspberry Pi 4 Model B Rev 1.2
```

Raspberry Pi 4B 8GB
```
processor	: 3
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 108.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32 
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xd08
CPU revision	: 3

Hardware	: BCM2711
Revision	: d03114
Serial		: 1000000005056aef
Model		: Raspberry Pi 4 Model B Rev 1.4
```


## 11/9/2020
Raspberry Pi 400
```
processor	: 3
model name	: ARMv7 Processor rev 3 (v7l)
BogoMIPS	: 324.00
Features	: half thumb fastmult vfp edsp neon vfpv3 tls vfpv4 idiva idivt vfpd32 lpae evtstrm crc32 
CPU implementer	: 0sssssssssssssssssssssssssssssssssssssssssssssssx41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xd08
CPU revision	: 3

Hardware	: BCM2711
Revision	: c03130
Serial		: 1000000045f95cf0
Model		: Raspberry Pi 400 Rev 1.0
```





### References

- [Raspberry Pi Awesome list](https://www.awesomelists.io/awesome-raspberry-pi/)




- [Raspberry Pi inventory tracker](https://rpilocator.com)   
As referenced from:
    - https://www.jeffgeerling.com/blog/2022/its-dire-raspberry-pi-availability-tracker-launched
    - https://news.ycombinator.com/item?id=30154141


# Raspberry Pi OS

[Raspberry Pi OS versions](https://blog.adafruit.com/2022/10/21/raspberry-pi-os-versions-piday-raspberrypi-raspberry_pi/)

| Version | Codename | Debian release date | RPi OS release date |
| ------- | -------- | ------------------- | ------------------- |
| 9       | Stretch  | June 2017           | August 2017         |
| 10      | Buster   | July 2019           | July 2019           |
| 11      | Bullseye | August 2021         | November 2021       |
| 12      | Bookworm | Expected in 2023    | -                   |


<small>This page was last updated on 2022-10-21 11:43:07 -0500.</small>

