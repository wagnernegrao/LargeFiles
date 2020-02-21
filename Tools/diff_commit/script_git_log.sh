#!/bin/bash

INPUT=lista_de_diretorios2.csv
OLDIFS=$IFS
IFS=','

[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read project name dirr
do
    git git log --oneline -M --stat --follow --pretty="%aI, %s, %an, %ae" -- $dirr > /home/wagner/GitHub/files_txt/$project-$name.txt
	echo "Project: $project"
    echo "Name : $name"
	echo "Dir : $dir"

    echo "Test: /home/wagner/GitHub/files_txt/$project-$name.txt"
done < $INPUT
IFS=$OLDIFS
