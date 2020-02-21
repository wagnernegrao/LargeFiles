#!/bin/bash

for name in $(cat lista_links_github.txt)
do
    git clone $name
done