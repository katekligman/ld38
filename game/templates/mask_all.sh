#!/bin/bash

rm MASK_*

for f in $(ls *.txt)
do
    mask $f
done

