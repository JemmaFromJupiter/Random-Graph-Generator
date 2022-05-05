import random as rand
import numpy as np
import matplotlib.pyplot as plt
import time as t
from termcolor import colored, cprint
import os

def positive():
	os.system('clear')
	cprint("Please Be Patient While We Retrieve The Data...", 'blue', attrs=['bold', 'blink'])
	pntX1 = rand.randint(0, 10)
	t.sleep(0.5)
	pntX2 = rand.randint(10, 20)
	t.sleep(0.5)
	pntX3 = rand.randint(30, 40)
	t.sleep(0.5)
	pntX4 = rand.randint(40, 50)
	t.sleep(0.5)
	pntX5 = rand.randint(50, 60)
	t.sleep(0.5)
	pntX6 = rand.randint(60, 70)
	t.sleep(0.5)
	pntX7 = rand.randint(70, 80)
	t.sleep(0.5)
	pntX8 = rand.randint(80, 90)
	t.sleep(0.5)
	pntY1 = rand.randint(0, 10)
	t.sleep(0.5)
	pntY2 = rand.randint(10, 20)
	t.sleep(0.5)
	pntY3 = rand.randint(30, 40)
	t.sleep(0.5)
	pntY4 = rand.randint(40, 50)
	t.sleep(0.5)
	pntY5 = rand.randint(50, 60)
	t.sleep(0.5)
	pntY6 = rand.randint(60, 70)
	t.sleep(0.5)
	pntY7 = rand.randint(70, 80)
	t.sleep(0.5)
	pntY8 = rand.randint(80, 90)

	cprint("Data Retrieved | Displaying Graph", 'green', attrs=['bold'])

	t.sleep(1)

	xpnts = np.array([pntX1, pntX2, pntX3, pntX4, pntX5, pntX6, pntX7, pntX8])
	ypnts = np.array([pntY1, pntY2, pntY3, pntY4, pntY5, pntY6, pntY7, pntY8])

	print("Plot X Points: ", xpnts, " ", "Plot Y Points: ", ypnts)
	plt.title("Random Graph")
	plt.plot(xpnts, ypnts)
	plt.grid()
	plt.show()