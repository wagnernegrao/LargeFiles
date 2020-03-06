#!/bin/bash

name="$1"
commit="$2"


# echo "rodou => $name ==> $commit"


cd /home/wagnernegrao/projetos_large_files/$name
git reset --hard $commit
date_git=$(git show -s --format=%ci $commit)
date="$(cut -d' ' -f1 <<<"$date_git")"

echo "$date"

cd ..


cloc --by-file /home/wagnernegrao/projetos_large_files/$name --csv --out=/home/wagnernegrao/Documents/dados_growth_curve/dados_csv_cloc/$name*$commit*$date.csv
