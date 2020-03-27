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
    """
    Le o arquivo passado pelo diretorio e retorna uma lista
    """
    filename_project = "/home/wagnernegrao/GitHub/LargeFiles/Tools/growth_curve/project_list/list_project.txt"

    f = open(filename_project, "r")
    file = f.readlines()

    project_list = []

    for line in file:
        print(line)
        project_list.append(line.replace("\n", ""))

    return project_list


def read_log(name):
    """
    Le o log referente ao nome e retorna uma lista com o log do arquivo
    """
    filename = f"/home/wagnernegrao/Documents/dados_growth_curve/log_projeto/{name}"

    f = open(filename, "r")
    file = f.readlines()

    log_list = []

    # cria uma lista para adicionar as hash dos commits
    for line in file:
        log_list.append(line.split(" ")[0])

    log_list.reverse()  # reordena do commit mais antigo para o mais atual

    return log_list


def write_new_csv(project):
    path = "/home/wagnernegrao/Documents/dados_growth_curve/dados_csv_cloc"

    text = "/home/wagnernegrao/Documents/dados_growth_curve/dados_csv_cloc/"

    filenames = glob.glob(path + "/*.csv")

    files = []
    flag = False

    for filename in filenames:
        if project == filename.replace(text, "").split("*")[0]:

            files.append(filename)
            flag = True

    dfs = []

    if flag == True:

        # Cria uma lista com cada csv de log
        for file_ in files:
            dfs.append(pd.read_csv(file_, error_bad_lines=False))

        for i in range(len(dfs)):
            size = len(dfs[i])
            project_data = [[], [], []]

            for j in range(size):
                data = files[i].replace(text, "").split("*")
                # print(data)
                project_data[0].append(data[0])
                project_data[1].append(data[1])
                project_data[2].append(data[2])

            dfs[i].insert(0, "Project", project_data[0], True)
            dfs[i].insert(1, "Commit", project_data[1], True)
            dfs[i].insert(2, "Date", project_data[2], True)

        if len(dfs) != 0:
            df_ = pd.concat(dfs, ignore_index=True)
            df_.to_csv(
                f"/home/wagnernegrao/Documents/dados_growth_curve/projetos_concatenados/{project}.csv",
                index=False,
            )


name_list = read_names()  # retorna uma lista de nomes dos projetos

for name in name_list:

    log_list = read_log(name)

    project_name = name.replace(".txt", "")  # pega o nome do projeto

    # percorre os commits
    for i in range(0, len(log_list), 250):
        print(i)
        os.system(f"bash get_cloc.sh {project_name} {log_list[i]}")

    write_new_csv(project_name)
