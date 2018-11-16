#!/usr/bin/python3.6
import numpy as np

def get_unit(n):
    result = empty(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                result[i][j] = 1
    return result

def multip (m1, m2, n):
	mat = empty (n)
	for z in range(n):
		for j in range(n):
			for i in range(n):
				mat[j][i] += m1[j][z]*m2[z][i]
	#print (mat)
	return mat

def empty (n):
	mat = []
	for i in range(n):
		mat.append([])
		for k in range(n):
			mat[i].append(0)
	return mat

def pow (p, n):
	if p == 0:
		return get_unit
	if p == 1:
		return m1
	if p == 2:
		return multip (m1, m2, n)
	else:
		return multip(pow(p-1, n), m2, n)

m1 = np.loadtxt('input.txt')
print (m1)
p = int(input())
#m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = m1

n = 0
for i in m1:
	n = n+1

mat = []
mat = pow (p, n)

print("matrix^",p)
print(mat)

