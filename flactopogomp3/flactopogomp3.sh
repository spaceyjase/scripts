#!/bin/sh

# This is where my mp3s are mounted.  Alter as you see fit!
pogo_music_mp3="/media/pogoplug/pogo_music/Music (mp3)"

find . -type f -iname '*.flac' | while read FILE
do 
    FILENAME="${FILE%.flac}.mp3"
    if [ ! -f "$pogo_music_mp3/${FILENAME}" ]; then
        metaflac --export-tags-to=- "$FILE" | sed 's/=\(.*\)/="\1"/' | sed 's/^\(.*\)=/\U&/g' > tmp.tmp
        . ./tmp.tmp
        outputpath=`dirname "$FILE"`
        mkdir -p "$pogo_music_mp3/${outputpath}"
        flac -cd "$FILE" | lame -b 192 --tt "$TITLE" --tn "$TRACKNUMBER" --tg "$GENRE" --ty "$DATE" --ta "$ARTIST" --tl "$ALBUM" --add-id3v2 - "$pogo_music_mp3/${FILENAME}" 
        unset TITLE TRACKNUMBER GENRE DATE ARTIST ALBUM
    fi
done
rm tmp.tmp
