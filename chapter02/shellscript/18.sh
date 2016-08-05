#!/usr/bin/bash

echo_and_do () {
  echo "> $1"
  eval "$1"
}

echo_and_do "sort -k 3r,3 -t $'\t' hightemp.txt"
