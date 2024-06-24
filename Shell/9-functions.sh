#!/bin/bash
#### Functions ####
get_date() {
  echo $(date +%d-%m--%Y)
}

#### Main code ####
today=$(get_date)
echo "Today : $today"
