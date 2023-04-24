#!/bin/bash
for i in {4..12}
do
    # Create the file in the directory
    touch level_$(printf "%02d" $i)/vulnerable_code.c
    
    # Add content to the file
    echo "// Vulnerable code for level $i" >> level_$(printf "%02d" $i)/vulnerable_code.c
    
    
done
