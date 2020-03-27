#!/bin/bash

# Percorre cada link do arquivo e executa o comando do git
for name in $(cat lista_links_github.txt)
do
    git clone $name
done