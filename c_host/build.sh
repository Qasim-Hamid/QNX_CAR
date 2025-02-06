#!/bin/bash
Input=$1
Output=${1%.*} 
qcc -Vgcc_ntoaarch64le -o $Output $Input
Error=$?
if [ $Error -ne 0 ]; then
    echo Error Code: $Error
else
    sudo mv $Output ../c_target
    ls -l ../c_target/$Output
fi
