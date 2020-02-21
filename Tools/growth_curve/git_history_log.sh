#!/bin/bash

for arq in `ls /home/wagner/Documents/Projetos/projetos_baixados_final_git/`; do
    cd /home/wagner/Documents/Projetos/projetos_baixados_final_git/$arq
    git log --oneline > /home/wagner/GitHub/git_history/log_project/$arq.txt
    cd ..
    echo "$arq"
done 