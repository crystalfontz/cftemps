cp cftemps/devicetree-zImage-imx28-cfa10037.dtb /boot/
cp cftemps/cftemps.sh /etc/init.d/
update-rc.d cftemps.sh defaults
