#!/usr/bin/python
# -*- coding: utf8 -*-
import re
from time import strptime
import csv
import os
import subprocess
import glob
import pandas as pd


def read_names():
    filename_project = "/home/wagnernegrao/Dropbox/pasta/git_history/list_project.txt"

    f = open(filename_project, 'r')
    file = f.readlines()

    project_list = []

    for line in file:
        print(line)
        project_list.append(line.replace('\n', ''))

    return(project_list)


def read_log(name):
    filename = f"/home/wagnernegrao/Dropbox/pasta/git_history/log_project/{name}"

    f = open(filename, 'r')
    file = f.readlines()

    log_list = []

    # cria uma lista para adicionar as hash dos commits
    for line in file:
        log_list.append(line.split(' ')[0])

    log_list.reverse()  # reordena do commit mais antigo para o mais atual

    return(log_list)


def write_new_csv(project):
    path = '/home/wagnernegrao/GitHub/git_history/projeto_cloc_final'

    text = '/home/wagnernegrao/GitHub/git_history/projeto_cloc_final/'

    filenames = glob.glob(path + '/*.csv')

    files = []
    flag = False
    for filename in filenames:
        if(project == filename.replace(text, '').split('.')[0]):
            files.append(filename)
            flag = True

    dfs = []

    if(flag == True):
        for file_ in files:
            dfs.append(pd.read_csv(file_, error_bad_lines=False))

        for i in range(len(dfs)):
            size = len(dfs[i])
            project_data = [[], [], []]

            for j in range(size):
                data = files[i].replace(text, '').split('.')
                # print(data)
                project_data[0].append(data[0])
                project_data[1].append(data[1])
                project_data[2].append(data[2])

            dfs[i].insert(0, 'Project', project_data[0], True)
            dfs[i].insert(1, 'Commit',  project_data[1], True)
            dfs[i].insert(2, 'Date',    project_data[2], True)

        if(len(dfs) != 0):
            df_ = pd.concat(dfs, ignore_index=True)
            df_.to_csv(f'/home/wagnernegrao/GitHub/git_history/projetos_concatenados/{project}.csv', index=False)


name_list = read_names()  # retorna uma lista de nomes dos projetos

# print(name_list)

for name in name_list:

    log_list = read_log(name)

    project_name = name.replace('.txt', '')  # pega o nome do projeto

    for i in range(0, len(log_list), 500):
        print(i)
        os.system(f"bash get_cloc.sh {project_name} {log_list[i]}")

    write_new_csv(project_name)




# cloc --by-file coderVueJs/ --csv --out=Vue.csv
# git log --oneline
# 0a31ad7188
