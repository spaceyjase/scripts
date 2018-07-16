#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage: gdrive-dl file-id output-file"
else
    # get the file's confirmation id
    echo "Attempting to get: $1"
    code=$(wget --quiet --save-cookies cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$1" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p')
    if [ -n "$code" ]
    then
        # file too big for virus scan, needs confirmation
        echo "File too big for scan, downloading anyway..."
        wget --quiet --show-progress --load-cookies cookies.txt "https://docs.google.com/uc?export=download&confirm=$code&id=$1" -O $2
    else
        # file is probably ok, passed virus check...
        wget --quiet --no-check-certificate "https://docs.google.com/uc?export=download&id=$1" -O $2
        echo "File saved to $2"
    fi
    rm cookies.txt
fi

