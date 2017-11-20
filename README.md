# automaticwatering

## Crontab
This will runn the scheduler every minute
Also reboots every 3 days just to be safe

 0 * * * * python /home/pi/sprinkler/runner.py
 0 0 */3 * * reboot

## Startup initialization
Add this to your favorite startup script

/etc/rc.local

echo "Initializing GPIO"
/usr/local/bin/init_gpio.py

if [ $? -eq 0 ]; then
  echo 'Success'
else
  echo 'Failed'
fi

## Schematic
[Circuit sketch available here](https://circuitmaker.com/Projects/Details/Zoltan-Damo/Automatic-sprinkler)
