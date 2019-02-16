import sys
import telnetlib
import time

HOST = "192.168.1.106" # update to your receiver's IP (recommend setting a static/DHCP reserved IP)
PORT = 8102
TIMEOUT = 10
tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

def get_internal_volume():
  tn.write("?V\r\n") # send "?V" command to get the current volume level
  output = tn.read_until("\r\n")
  if output.startswith("FL"):  # read next line
    print "Skipping FL line, and reading next line"
    output = tn.read_until("\r\n")
  if output.startswith("VOL"):
    currentlevel = int(output[3:])  # Pioneer responds with "VOL###" (ignore the "VOL" part of the string)
    return currentlevel
  else:
    print "Received unparsable volume response %s" % output
    return -1

def convert_display_to_internal_volume(display_volume):
  return 161 - 2 * int(display_volume)

def convert_internal_to_display_volume(internal_volume):
  return (161 - internal_volume) / 2.0

current_internal_volume = get_internal_volume()
current_display_volume = convert_internal_to_display_volume(current_internal_volume)
requested_display_volume = int(sys.argv[1])
requested_internal_volume = convert_display_to_internal_volume(requested_display_volume)

if requested_internal_volume < 131 and requested_internal_volume > -1: # my set upper limit to prevent damage to speakers
  newLevelString = str(requested_internal_volume).zfill(3)
  print "Volume should go from %.1f (%d) to %.1f (%d)" % (current_display_volume, current_internal_volume, requested_display_volume, requested_internal_volume)
  volumeCommand = "%sVL\r\n" % newLevelString
  tn.write(volumeCommand)
  time.sleep(0.5)
  tn.close()
else:
  print "Out of range"
