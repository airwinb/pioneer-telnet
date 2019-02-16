# Volume Control of Pioneer Receivers via Telnet
Simple script to control the volume on a Pioneer receiver via telnet.

Based off of telnet commands listed at http://www.pioneerelectronics.com/StaticFiles/PUSA/Files/Home%20Custom%20Install/SC-35-RS232.pdf and http://blog.raymondjulin.com/2012/07/15/remote-control-your-pioneer-vsx-receiver-over-telnet/, this script takes in a single command-line argument (integer) and sets the volume to the desired level.

**NOTE**: Pioneer receivers internally use a different numerical scale for volume than what shows up in the volume the LCD display of the receiver itself (dB). The value in this script has been scaled for my Pioneer (VSX-920-K) and may differ depending on your TV and receiver.

**REQUIREMENTS**:
- update the IP address
- adjust the upper limit as needed
- adjust the scaling, if necessary

**SYNTAX**: 
```
python set-volume.py #
```
