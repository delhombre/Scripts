#!/bin/bash
# Series of values separated by spaces
for path in /etc /var/log /srv
do
  echo "Starting backup of $path"
done

# Iterates through a variable substitution
echo ""
target_list="127.0.0.1 1.1.1.1 www.kernel.org"
for target in $target_list
do
  ping -c 1 -q $target 1> /dev/null
  echo "ping $target return code=$?"
done

# Iterates through a sequence of numbers
echo ""

for id in {006..012}
do
  echo "Restarting machine srv${id}techni ..."
done













