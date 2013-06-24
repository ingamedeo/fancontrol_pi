
         -----------------------------------------------------
           Fan Control Script - Raspberry Pi - By ingamedeo


 This script controls a cooling fan (5V) connected throught GPIO.

 You have to use a Transistor as a switch to turn fan on or off.

 For more information about the electric circuit please refer to fan.png

 This script turns on automatically the 5V fan when temperature reaches 50 C

 Main script is: fan.py (python2)

 Temperature checker script is: temp.sh

 Systemd unit for autostart is: fan.service (Working on Archlinux ARM)

 WARNING! You should change the path of the temp.sh script in fan.py for have it working!!

 Enjoy! :D

 For any questions / suggestions send an e-mail to: <ingamedeo[at]gmail[dot]com>
