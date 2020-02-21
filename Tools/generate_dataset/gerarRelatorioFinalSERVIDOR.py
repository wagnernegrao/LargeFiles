import glob
import os
import sys
from pydriller import RepositoryMining
import csv
import codecs

#verifica quais projetos iremos extrair, pois tenho mais projetos baixados do que os que vou analisar.
#coloco numa lista para verificar se ele esta dentro dos projetos a serem analisados

#os.chdir("/home/wagner/Documents/Projetos/projetos_baixados_final_git")

filename1 = "/home/wagnernegrao/GitHub/git_history/lista_todos_projetos.txt"
f = open(filename1, 'r')
file = f.readlines()

pasta = ""
vetPastas = []


for line in file:
    # print(line)
    vetPastas.append(line.replace('\n', ''))

print('-> ', vetPastas)

#for file in glob.glob("*.txt"):
#    pasta=file[0:len(file)-4]
#    vetPastas+=[pasta]

#resolvendo erro de codificação
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#arquivo para a geracao dos relatórios
os.chdir("/home/wagnernegrao/GitHub/git_history/resultados")
#c = open("D:\Pesquisas\CSVSNovos\largeFiles[1].csv", "w", newline="")
FILENAME = "resultado[18].csv"
ENCODING = 'utf-8'

#print('--> Passo 1')

#comeca a escrita do csv
with codecs.open(FILENAME, "w", ENCODING) as fp:
    writer = csv.writer(fp)
    linhas=[]
    arquivos=[]
    file_name2=""
    extensao=""
    grava=0
    #primeira linha do csv
    writer.writerow(["Hash", "File_Name", "Extension", "ContributorName", "ContributorEmail","CommitterName","Committeremail",
                     "Date","addLines","excLines","linesOfCode","Complexity","changeType","Project_Name"])


    # pasta = 'coderVueJs\n'

    #print('--> Passo 2')

    # percorrendo a pasta com os clones dos projetos
    # /home/wagnernegrao/GitHub/projetos_github
    # /home/wagnernegrao/GitHub/projeto_git
    
    for i in glob.glob("/home/wagnernegrao/GitHub/projetos_github/*"):
        print("i",i)
        for j in range(len(i)-1,-1,-1):
            #print('externa pasta: ', pasta)
            #print('i[j]: ', i[j])
            if(i[j]=="/"):
                pasta=i[j+1:]
                print("interna pasta:",pasta)
                break
        if(pasta in vetPastas):
            #print("Pasta no vetPastas: ", pasta)
            for commit in RepositoryMining(i).traverse_commits():
                file_name2=""
                for m in commit.modifications:
                    if(m.new_path!=None):
                        #pegando apenas o nome do arquivo
                        file_name=m.new_path
                        for j in range(len(file_name)-1,-1,-1):
                            if(file_name[j]=="/"):
                                file_name2=file_name[j+1:]
                                #print("1",file_name2)
                                break
                        for j in range(len(file_name2)-1,-1,-1):
                            if(file_name2[j]=="."):
                                extensao=file_name2[j+1:]
                                file_name2=file_name2[0:j]
                                #print("file:",file_name2)
                                #print("extensao:",extensao)
                    if(commit.hash!=None and file_name2!=None and commit.author.name!=None and commit.author.email!=None and
                           commit.committer.name!=None and commit.committer.email!=None and commit.author_date!=None
                           and commit.project_name!=None and m.nloc!=None):
                            # adicionando em uma lista, todas as LOC
                            if(m.nloc>=1848 and file_name2 not in arquivos and file_name2!=""):
                                arquivos+=[file_name2]

            #print(arquivos)
            print("PROXIMO FOR")
            print('--> i: ', i)
            for commit in RepositoryMining(i).traverse_commits():
                file_name2=""
                for m in commit.modifications:
                    if(m.new_path!=None):
                        #pegando apenas o nome do arquivo
                        file_name=m.new_path
                        #print('--> File: ', file_name)
                        for i in range(len(file_name)-1,-1,-1):
                            if(file_name[i]=="/"):
                                file_name2=file_name[i+1:]
                                #print("file_name2:",file_name2)
                                break
                        for j in range(len(file_name2)-1,-1,-1):
                            if(file_name2[j]=="."):
                                extensao=file_name2[j+1:]
                                file_name2=file_name2[0:j]
                                #print("file:",file_name2)
                                #print("extensao:",extensao)
                    commit_author_email=""
                    commit_author_name=""
                    commit_committer_name=""
                    commit_committer_email=""                
                    commit_project_name=""
                    #print('file name 2: ', file_name2)
                    #print('arquivos: ', arquivos)
                    if file_name2 in arquivos:
                        if(commit.hash!=None and file_name2!=None and commit.author.name!=None and commit.author.email!=None and
                           commit.committer.name!=None and commit.committer.email!=None and commit.author_date!=None and
                           commit.project_name!=None and m.nloc!=None):
                            print('--> ',commit.hash, file_name2, commit.author.name.translate(non_bmp_map), commit.author.email.translate(non_bmp_map),
                                             commit.committer.name.translate(non_bmp_map), commit.committer.email.translate(non_bmp_map),
                                             commit.author_date.strftime("%Y-%m-%d %H:%M:%S"), m.added,m.removed,m.nloc,m.complexity,m.change_type.name,
                                              commit.project_name.translate(non_bmp_map))

                            commit_author_email=commit.author.email.translate(non_bmp_map)
                            commit_author_name=commit.author.name.translate(non_bmp_map)
                            commit_committer_name=commit.committer.name.translate(non_bmp_map)
                            commit_committer_email=commit.committer.email.translate(non_bmp_map)
                            commit_project_name=commit.project_name.translate(non_bmp_map)

                            commit_author_email=commit_author_email.replace(",","")
                            commit_author_name=commit_author_name.replace(",","")
                            commit_committer_name=commit_committer_name.replace(",","")
                            commit_committer_email=commit_committer_email.replace(",","")
                            commit_project_name=commit_project_name.replace(",","")

                            commit_author_email=commit_author_email.replace(";","")
                            commit_author_name=commit_author_name.replace(";","")
                            commit_committer_name=commit_committer_name.replace(";","")
                            commit_committer_email=commit_committer_email.replace(";","")
                            commit_project_name=commit_project_name.replace(";","")

                            commit_author_email=commit_author_email.replace("\n","")
                            commit_author_name=commit_author_name.replace("\n","")
                            commit_committer_name=commit_committer_name.replace("\n","")
                            commit_committer_email=commit_committer_email.replace("\n","")
                            commit_project_name=commit_project_name.replace("\n","")


                            commit_author_email=commit_author_email.replace("\t","")
                            commit_author_name=commit_author_name.replace("\t","")
                            commit_committer_name=commit_committer_name.replace("\t","")
                            commit_committer_email=commit_committer_email.replace("\t","")
                            commit_project_name=commit_project_name.replace("\t","")

                            
                            print("==============================================================")
                            print(commit.hash, file_name2, extensao, commit_author_name, commit_author_email,
                                             commit_committer_name, commit_committer_email,
                                             commit.author_date.strftime("%Y-%m-%d %H:%M:%S"), 
                                             m.added,m.removed,m.nloc,m.complexity,m.change_type.name,commit_project_name)

                            #escreve no cvs as informacoes dos arquivos que em algum momento atingiram 1048 linhas
                            writer.writerow([commit.hash, file_name2, extensao, commit_author_name, commit_author_email,
                                             commit_committer_name, commit_committer_email,
                                             commit.author_date.strftime("%Y-%m-%d %H:%M:%S"),
                                             m.added,m.removed,m.nloc,m.complexity,m.change_type.name,commit_project_name])
        else:
            print("A pasta não está no escopo -> ", pasta)
