#!/bin/bash
# if statement using return code(s) as condition
ip1=$1
ip2=$2
path=$3

if [ -z $ip1 ] || [ -z $ip2 ] || [ -z $path ]
then
  echo "Usage: 3 pameters --> ip1 ip2 path"
  exit 30 # Between 1 and 255
fi

if ping -c 1 $ip1 1> /dev/null && ping -c 1 $ip2 1> /dev/null
then
  echo "$ip1 and $ip2 are reachable"
else
  echo "At least one ip address is not reachable"
fi

if [ -d $path ]
then
  echo "$path exists"
else
  echo "$path doesn't exist"
fi

# Nesting if statements
dow=$(date +%u) # Day Of Week
if [ $dow = 1 ]
then
  echo "Monday"
elif [ $dow = 2 ]
then
  echo "Tuesday"
elif [ $dow = 3 ]
then
  echo "Wednesday"
elif [ $dow = 4 ]
then
  echo "Thursday"
elif [ $dow = 5 ]
then
  echo "Friday"
else
  echo "Is not a working day"
fi















