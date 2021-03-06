#!/bin/bash

# Get current time since epoch
DATE_PC_orig=`date "+%s"`	
DATE_PC="$(($DATE_PC_orig + 10))"

# Convert to pi date locale
DATE_PI=`ssh rosberrypi@192.168.0.108 date -d @$DATE_PC`

# Save date in shell script
echo sudo date -s \'"$DATE_PI"\'> pi_updateclock.sh
echo groupRBP >> pi_updateclock.sh

# Set date of pi over SSH with shell script
ssh rosberrypi@192.168.0.108 -tt 'bash -s' < pi_updateclock.sh
