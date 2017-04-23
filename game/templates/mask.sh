#!/bin/bash

if [ $# -eq 0 ]
  then
      echo "No arguments supplied"
      exit -1
  fi

cat $1 | sed 's/./ /g' > MASK_$1
