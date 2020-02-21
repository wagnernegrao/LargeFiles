#!/bin/bash

name="$1"
commit="$2"


# echo "rodou => $name ==> $commit"


cd /home/wagnernegrao/GitHub/projetos_github/$name
git reset --hard $commit
date_git=$(git show -s --format=%ci $commit)
date="$(cut -d' ' -f1 <<<"$date_git")"

echo "$date"

cd ..


cloc --by-file /home/wagnernegrao/GitHub/projetos_github/$name --csv --out=/home/wagnernegrao/GitHub/git_history/projeto_cloc_final/$name.$commit.$date.csv
