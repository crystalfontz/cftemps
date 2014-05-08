cftemps
=======

CFA10036+CFA10037 Fridge Monitor Showcase

A simple demonstration using a [CFA10036+CFA10037](https://www.crystalfontz.com/product/CFA100375) and 2x [WR-DOW-17](https://www.crystalfontz.com/product/WRDOWY17.html) DS18B20 1-Wire Digital Thermometers to monitor and chart the temperatures of the fridge and freezer in our breakroom here at Crystalfontz.

The project is a python script that reads the values from the attached 1-wire chain, writes them to a json file which is then uploaded to a webserver.
There's also an included html page that can read that json file and use the Google visualization API to chart the data onto a graph showing temperature over time.

Live demo!
=======
Want to see it [in action](http://www.crystalfontz.com/CFA10036/demo/temp-sensor)?

The example is written as a jumping off point to be expanded into whatever application you can think of.

Installation
=======
Cloning the project will pull down two folders 'www' and 'cftemps'.

The 'www' folder contains a webpage that needs to be put in the same location as the output of the python script and will be the entry point for the monitoring.
This path needs to have ftp access and will need to be specified in the cftemps.py script

The 'cftemps' folder contains an installation shell script that will perform 3 functions.
* Copy the device tree into the root folder that will enable 1-wire (w1_bus_master1) functionality on port 1 pin 21 of the SOM
* Copy the actual initialization script into /etc/init.d/
* Add the script to the default runlevels in rc.d

Instructions
=======
* Make a folder to house the project. All scripts point to /home/root/ by default but that can be changed
* Clone the repository into the new folder
* Change permissions on the two shell scripts
```shell
chmod 755 cftemps/*.sh
```
* Run the installer
```shell
cftemps/install_script.sh
```
* Change the applicable settings in the [python script](som/cftemps.py)
```
username = 'USERNAME'
password = 'PASSWORD'
webserver = 'WEBSERVER'
```
* Reboot to enable the new device tree and kick off the service
```
shutdown -r now
```
* Enjoy
