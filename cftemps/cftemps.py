try: import simplejson as json
except ImportError: import json
import tempfile
import os,datetime,time
from datetime import timedelta

slaves = []
times = []
cfaArray = []
logFileName = 'temps.json'
localPath = '/home/root/cftemps/'
username = 'USERNAME'
password = 'PASSWORD'
webserver = 'WEBSERVER'
remotePath = '/'

def LoadSlaves():
	# This function records the name of each of the attached 1 wire devices
	slavesFile = open('/sys/devices/w1_bus_master1/w1_master_slaves')

	i = 0
	for slave in slavesFile:
#		print("Slave " + str(i) + ": "+ slave[0:-1]) # for debugging
		slaves.append(slave[0:-1])
		i += 1
	slavesFile.close()

def _GetTemps():
	# This function iterates through the individual files and pulls their respective values
	slaveTemps = []
	global slaves
	for slave in slaves:
		slaveFile = open('/sys/devices/w1_bus_master1/'+slave+'/w1_slave')	
		slaveFile.readline()
		slaveData = slaveFile.readline()
		slaveTempC = int(slaveData[slaveData.find('t=')+2:-1])/1000
		slaveTempF = (slaveTempC * 9 / 5) + 32
		slaveTemps.append(slaveTempF)
	slaveFile.close()
	return slaveTemps

def GetTemps():
	# This function takes the slave's obtained values and stores then in the arrays
	# 60 seconds per minute = 60
	# 60 minutes per hour = 60 * 60 = 3600
	# 24 hours per day = 3600 * 24 = 86400
	# 10 samples per second = 86400 /10 = 8640	
	temps = _GetTemps()
	if len(times) >= 8640:
		times.pop(0)
	if len(cfaArray) >= 8640:
		cfaArray.pop(0)
				
	# PST offset
	tempTime = datetime.datetime.now()
	times.append(tempTime.strftime('%Y-%m-%d_%I:%M%p'))
	cfaArray.append({"timestamp": tempTime.strftime('%Y-%m-%d_%I:%M%p'), "freezer": temps[0], "fridge": temps[1]})

LoadSlaves()
while True:
	# Read/Write/Upload every 30 seconds
	for i in range(0, 3):
		GetTemps()

		# Write the values to the file
		with open(logFileName, 'w') as f:
			json.dump(cfaArray, f)
	
		# delay for 10 seconds then do it again
		time.sleep(10)
	
	# Upload the records to the webserver
	os.system("ftpput -u " + username + " -p " + password + " -P 21 " + webserver + " " + remotePath + logFileName + " " + localPath + logFileName + ";")
	
