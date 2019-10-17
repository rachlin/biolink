import sqlite3
import numpy as np
import matplotlib.pyplot as plt

print("Connecting to the datbase and getting the data...")
conn = sqlite3.connect('../../data/sources/disgenet_2018.db')
cursor = conn.cursor()

cursor.execute("select distinct EL from geneDiseaseNetwork")
distinct_ELs = cursor.fetchall()
map_el_to_number = {}

cursor.execute("select score, EL, EI from geneDiseaseNetwork where EI != '\\N';")
data = np.array(cursor.fetchall())

print("Converting categorical values for Evidence level to Numerical...")
counter = 0
for distinct_el in distinct_ELs:
    map_el_to_number[distinct_el[0]] = counter
    counter += 1
print(map_el_to_number)

print("Preparing the data for plotting...")
scores = data[:,0]
ELs = np.array([map_el_to_number[el] for el in data[:,1]])
EIs = data[:,2]

np.random.seed(19680801)

N = len(scores)
x = ELs
y = EIs
colors = np.random.rand(N)
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.title('Plotting EL vs EI for each association')
plt.scatter(x, y, c=colors, alpha=0.5)
plt.xlabel('Evidence Level')
plt.ylabel('Evidence Index')
# for i, score in enumerate(scores):
#     plt.annotate(score, (ELs[i], EIs[i]))
plt.show()



