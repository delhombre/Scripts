#!/bin/bash
# Simple until loop with numbers
number=100

until [ $number -eq 0 ]
do
  echo $number
  number=$[ $number - 25 ]
done

# Create 500M files with until loop
echo
dir="until"
mkdir $dir
index=1
echo "Starting to create files ... please wait!"
sleep 2

until [ $index -gt 10 ]
do
  dd if=/dev/zero of=$dir/file-${index}.img bs=100M count=5 &> /dev/null
  ((index++))
done
ls -lh until
rm -fR until















