import pandas as pd
from github import Github

user = ""
password = ""

filename = "directory-path to CSV"

# Le um csv com de projetos e o criador
df = pd.read_csv(filename, sep=",")

# adiciona tudo em uma lista
link_list = df.name.tolist()

# cria um objeto
g = Github(user, password)

project_stars = []

# Percorre cada link da lista
for link in link_list:
    try:
        # Obten a informacao do repositorio
        repo = g.get_repo(link)

        # Adiciona na lista a quantiade de estrelas
        project_stars.append(repo.stargazers_count)
    except:
        print(f"\n\nErro no projeto: {link}")

# Cria uma serie
stars = pd.Series(project_stars)


print(f"\nQuantidade de estrelas: ")
print(stars.describe())
