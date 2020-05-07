import random as r
import time

a = ["0","1"," "," "]
line = []
counter = 0

for i in range(118):
	x = r.randint(0,3)
	line.append(a[x])

	counter += 1

for i in range(10000):

	r_symbols = []

	if counter % 5 == 0:
		r_symbols = [r.randint(0,117) for x in range(10)]

	for i in r_symbols:
		line[i] = a[r.randint(0,3)]

	print(*line)
	counter += 1
	time.sleep(0.01)