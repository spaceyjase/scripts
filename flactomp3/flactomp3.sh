#!/bin/sh

if [ $# != 1 ]; then
    echo "Usage: flactomp3.sh <output path>"
    exit 1
fi

output_music_mp3="$1"

find . -type f -iname '*.flac' | while read FILE
do 
    FILENAME="${FILE%.flac}.mp3"
    if [ ! -f "$output_music_mp3/${FILENAME}" ]; then
        metaflac --export-tags-to=- "$FILE" | sed 's/=\(.*\)/="\1"/' | sed 's/^\(.*\)=/\U&/g' > tmp.tmp
        . ./tmp.tmp
        outputpath=`dirname "$FILE"`
        mkdir -p "$output_music_mp3/${outputpath}"
        flac -cd "$FILE" | lame -b 192 --tt "$TITLE" --tn "$TRACKNUMBER" --tg "$GENRE" --ty "$DATE" --ta "$ARTIST" --tl "$ALBUM" --add-id3v2 - "$output_music_mp3/${FILENAME}" 
        unset TITLE TRACKNUMBER GENRE DATE ARTIST ALBUM
    fi
done
rm tmp.tmp
