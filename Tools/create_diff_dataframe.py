import re
from time import strptime
import csv

def read_file(file):
    '''
    Percorre o arquivo adiciona na lista de log as adicoes e remocoes do commit
    e a data do commit
    '''
    regex1 = 'nged,.*'
    regex2 = '\d\d\d\d\S\d\d\S\d\d'
    regex3 = ':\d\d,(\s\S.*),'
    #regex3 = ':(\s\S.*),'
    
    log_list = []
    date_log = []
    log_commits  = []

    for line in file:
        try:
            #print(line)
            log_list.append(re.search(regex1, line).group())
        except:
            pass

        try:
            date_log.append(re.search(regex2, line).group())
        except:
            pass

        try:
            log_commits.append(re.search(regex3, line).group())
        except:
            pass

    return(log_list, date_log, log_commits)

def cleaner(log_list, log_commits, author):
    '''
    Remove alguns excessos e deixa apenas a adicao e remocao
    '''
    values_commits = []
    for line in log_list:
        values_commits.append(line.replace('nged, ', '').split(','))


    commits = []
    '''
    Limpa o inicio e final do commit 
    '''
    for i in range(len(author)):
        aux = re.sub(author[i], "", log_commits[i]).replace(',,','').replace(': ', '')
        commits.append(re.sub(r'\d\d',"", aux).replace(':, ',''))
    return(values_commits, commits)

def generate_author(log_commits):
    '''
    Pega o nome do autor do commit
    '''
    
    author = []
    regex4 = ',\s(.*),$'
    for i in range(len(log_commits)):
        aux = re.search(regex4,log_commits[i]).group()
        aux_list = aux.split(',')
        author.append(aux_list[len(aux_list) - 2])
    
    return(author)

def generate_diff(values_commits):
    '''
    Para cada linha de commits pego apenas o valor de adicao/remocao, o
    try-except serve para momentos em que ocorre apenas remocao ou adicao
    '''
    
    insertions = []
    deletions = []

    for i in values_commits:
        try:
            insertions.append(i[0].split(' ')[0])
        except:
            insertions.append(0)

        try:
            deletions.append(i[1].split(' ')[1])
        except:
            deletions.append(0)

    return(insertions, deletions)


def generate_date(date_log):
    '''
    Primeiro converte converte o mes para numeral e posteriormente adiciona na
    lista a data estruturada pt-br
    '''
    dates = []
    for i in date_log:
        #print(i)
        month = strptime(i.split(' ')[1],'%b').tm_mon
        day   = i.split(' ')[2]
        year  = i.split(' ')[4]
        dates.append(f'{day}-{month}-{year}')

    return(dates)


def create_csv(date_log, authors, commmits, insertions, deletions, NameFile='file'):
    '''
    Cria um dataframe com data, adicoes e remocoes, está estruturado do commit
    atual para o commit mais antigo. A flag NameFile serve para especificar um
    nome para o arquivo de saída, se não recebe por default file.
    '''
    dataframe = [['Date','Author','Commit','Insertions','Deletions']]

    for i in range(len(insertions)):
        try:
            dataframe.append([date_log[i], authors[i], commmits[i], insertions[i], deletions[i]])
        except:
            dataframe.append([date_log[i], 'NaN', 'NaN', insertions[i], deletions[i]])

    with open(f'{NameFile}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(dataframe)


filename = 'directory-path to CSV'


f = open(filename, 'r')
file = f.readlines()

log_list, date_log, log_commits = read_file(file)

print(len(log_list), len(date_log), len(log_commits))

authors = generate_author(log_commits)

values_commits, commmits = cleaner(log_list, log_commits, authors)

insertions, deletions = generate_diff(values_commits)

#dates = generate_date(date_log)
print(len(date_log), len(authors), len(commmits), len(insertions), len(deletions))
create_csv(date_log, authors, commmits, insertions, deletions, '?')

#print(commmits)
