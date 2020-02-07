#!/bin/bash

INPUT=lista_de_diretorios.csv
OLDIFS=$IFS
IFS=','

[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read name dir
do
    git git log --oneline -M --stat --follow --pretty="%aI, %s, %an, %ae" -- $dir > /home/wagner/GitHub/files_txt/$name.txt
	echo "Name : $name"
	echo "DOB : $dir"
done < $INPUT
IFS=$OLDIFS