import sqlite3
import numpy as np
import matplotlib.pyplot as plt

conn = sqlite3.connect('../../data/sources/disgenet_2018.db')
cursor = conn.cursor()
cursor.execute("select distinct EL from geneDiseaseNetwork")
distinct_ELs = cursor.fetchall()
map_el_to_number = {}

counter = 0
for distinct_el in distinct_ELs:
    map_el_to_number[distinct_el[0]] = counter
    counter += 1

print(map_el_to_number)
# cursor.execute("select geneId, diseaseId, association, associationType, pmid, score, EL, EI, year from geneDiseaseNetwork left join geneAttributes USING (geneNID) left join diseaseAttributes USING (diseaseNID) where association != `\N`;"")
cursor.execute("select score, EL, EI from geneDiseaseNetwork;")

data = np.array(cursor.fetchall())
scores = data[:,0]
ELs = np.array([map_el_to_number[el] for el in data[:,1]])
EIs = data[:,2]


plt.scatter(ELs, EIs)
plt.title('Plotting EL vs EI for each association')
plt.xlabel('EL')
plt.ylabel('EY')
for i, score in enumerate(scores):
    plt.annotate(score, (ELs[i], EIs[i]))

plt.show()




