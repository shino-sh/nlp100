#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "sed -e $'s/\t/ /g' hightemp.txt"
