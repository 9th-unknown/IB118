#!/usr/bin/python3.6

import math

def func(x):
	f = x*x - 2
	#f = math.log2(x)-11
	#f = x*x*x - x*x - x - 1
	#f = math.sin(x)
	return f

print("A")
a = int(input())
print("B")
b = int(input ())
print("e")
e = float(input())

if func(a) * func(b) < 0:
	c = (a+b)/2
if func(a) * func(c) <= 0:
	b = c
else:
	a = c


while abs(b-a)>e:
	if func(a) * func(b) < 0:
		c = (a+b)/2
	#print(c)
	if func(a) * func(c) <= 0:
		b = c
	else:
		a = c
x = (a+b)/2
print("x = ",x)
