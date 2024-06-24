#!/bin/bash
# Simple while loop with numbers
number=1

while [ $number -le 5 ]
do
  echo "$number"
  number=$[ $number + 1 ]
done

# Read a text file line by line
echo
passwd_file="/etc/passwd"

while read line
do
  user=$(echo $line | cut -d: -f1)
  shell=$(echo $line | cut -d: -f7)
  if [ $shell = "/bin/bash" ] || [ $shell = "/bin/sh" ]
  then
    echo "The user $user has a shell $shell"
  fi
done 0< $passwd_file

# Break from an infinite while loop
echo ""
magick_number=${RANDOM:0:1}
echo "Enter a number from 1 to 9"

while true # condition is always true
do
  read counter
  if [ $counter -eq $magick_number ]
  then
    echo "Bye Bye, $counter = $magick_number"
    break
  fi
done















