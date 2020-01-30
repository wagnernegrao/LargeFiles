import re
import pandas as pd


filename = 'directory-path to CSV'
regex = r"m/.*?.git"


df = pd.read_csv(filename, sep=',')

link_list = df.link_project.tolist()


# cria uma nova lista com apenas o nome os projetos
for i in range(len(link_list)):
	link_list[i] = re.search(regex, link_list[i]).group()
	link_list[i] = link_list[i].replace('.git', '')
	link_list[i] = link_list[i][2:]

link = pd.Series(link_list)

link.to_csv('projects_name.csv', index=False)
