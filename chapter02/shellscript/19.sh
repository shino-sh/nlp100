#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "cut -f 1 hightemp.txt | sort | uniq -c | sort -r"
