#!/bin/sh
wget -U Mozilla -qO - "http://thepiratebay.org/search/$1/0/7/0" | grep -o 'http\:\/\/torrents\.thepiratebay\.org\/.*\.torrent'
