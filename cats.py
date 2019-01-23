import re
import numpy as np
import scipy
l = []
f = open('strings.txt','r')
d = {}

for line in f:
	string = line.lower()
	spstring = re.split('[^a-z]', string)
	clear_l = [x for x in spstring if x is not '']
	l.append(clear_l)

z = [item for sublist in l for item in sublist]

g = 0
for j in range(len(z)):
	if z[j] not in d:
		d[z[j]] = g
		g += 1

s = np.zeros((22,254), dtype = int)

q = 0
for i in range(22):
	for j in range(254):
		s[i][j] = l[i].count(d.keys()[d.values().index(j)])

matrix = np.array(s)
d = matrix.reshape((22,254))

from scipy.spatial.distance import cosine

dists = []
for row in matrix:
	dists.append(scipy.spatial.distance.cosine(matrix[0,:], row))

print dists