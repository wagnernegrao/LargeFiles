#!/bin/bash

for name in $(cat projects_name.csv)
do
  git clone git@github.com:$name.git
done
