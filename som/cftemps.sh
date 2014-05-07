#!/bin/sh

### BEGIN INIT INFO
# Provides:          cftemps
# Required-Start:    
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Reads and uploads 2 temps
# Description:       Created by Crystalfontz America, Inc. to showcase
#                    our 10036+10037 with DOW
### END INIT INFO

# Some scripting options
DIR=/home/root/cftemps
DAEMON_NAME=cftemps
DAEMON="python $DIR/$DAEMON_NAME.py"

# This next line determines what user the script runs as.
DAEMON_USER=root

# The process ID of the script when it runs is stored here:
PIDFILE=/var/run/$DAEMON_NAME.pid

do_start () {
    start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --chuid $DAEMON_USER --startas $DAEMON
	echo "Starting $DAEMON_NAME using $DAEMON"
}
do_stop () {
    start-stop-daemon --stop --pidfile $PIDFILE --retry 10
	echo "Stopping $DAEMON_NAME"
}

case "$1" in

    start|stop)
        do_${1}
        ;;

    restart|reload|force-reload)
        do_stop
        do_start
        ;;

    status)
        status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
        ;;
    *)
        echo "Usage: /etc/init.d/$DAEMON_NAME {start|stop|restart|status}"
        exit 1
        ;;

esac

exit 0
