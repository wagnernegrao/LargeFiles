import pandas as pd
from github import Github

user = ''
password = ''


filename = 'directory-path to CSV'
df = pd.read_csv(filename, sep=',')
link_list = df.name.tolist()




g = Github(user, password)

project_stars = []

for link in link_list:
	try:
		# print(f'\nProjeto: {link}')
		repo = g.get_repo(link)

		# print(f'Quantidade de estrelas: {repo.stargazers_count}\n\n')
		project_stars.append(repo.stargazers_count)
	except:
		print(f'\n\nErro no projeto: {link}')


stars = pd.Series(project_stars)


print(f'\nQuantidade de estrelas: ')
print(stars.describe())
