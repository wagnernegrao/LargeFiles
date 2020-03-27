#!/bin/bash

# Para cada pasta no endereco citado entra na pasta e executa o comando do git
# e salva no diretorio passado

for arq in `ls /home/wagnernegrao/projetos_large_files/`; do
    cd /home/wagnernegrao/projetos_large_files/$arq
    git log --oneline > /home/wagnernegrao/Documents/dados_growth_curve/log_projeto/$arq.txt
    cd ..
    echo "$arq"
done 