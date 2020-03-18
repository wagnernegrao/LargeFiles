#!/bin/bash

for arq in `ls /home/wagnernegrao/projetos_large_files/`; do
    cd /home/wagnernegrao/projetos_large_files/$arq
    git log --oneline > /home/wagnernegrao/Documents/dados_growth_curve/log_projeto/$arq.txt
    cd ..
    echo "$arq"
done 