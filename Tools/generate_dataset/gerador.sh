#!/bin/bash

for name in $(cat lista_nome_projetos.txt)
do
	python3 gerarRelatorioFinalSERVIDOR.py $name
done
