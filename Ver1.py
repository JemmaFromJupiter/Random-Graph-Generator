import random as rand
import numpy as np
import matplotlib.pyplot as plt
import time as t
from termcolor import colored, cprint
import os

def positive():
  os.system('clear')
  cprint(colored("Please Be Patient While We Retrieve The Data...", 'blue', attrs=['bold', 'blink']))
  pntX1 = rand.randint(0, 10)
  t.sleep(0.5)
  pntX2 = rand.randint(10, 30)
  t.sleep(0.5)
  pntX3 = rand.randint(30, 50)
  t.sleep(0.5)
  pntX4 = rand.randint(50, 70)
  t.sleep(0.5)
  pntX5 = rand.randint(70, 90)
  t.sleep(0.5)
  pntX6 = rand.randint(90, 110)
  t.sleep(0.5)
  pntX7 = rand.randint(110, 130)
  t.sleep(0.5)
  pntX8 = rand.randint(130, 150)
  
  t.sleep(0.5)
  
  pntY1 = rand.randint(0, 20)
  t.sleep(0.5)
  pntY2 = rand.randint(20, 40)
  t.sleep(0.5)
  pntY3 = rand.randint(40, 60)
  t.sleep(0.5)
  pntY4 = rand.randint(60, 80)
  t.sleep(0.5)
  pntY5 = rand.randint(80, 100)
  t.sleep(0.5)
  pntY6 = rand.randint(100, 120)
  t.sleep(0.5)
  pntY7 = rand.randint(120, 140)
  t.sleep(0.5)
  pntY8 = rand.randint(140, 160)
  
  cprint("Data Retrieved | Displaying Graph", 'green', attrs=['bold'])

  t.sleep(1)
  
  xpnts = np.array([pntX1, pntX2, pntX3, pntX4, pntX5, pntX6, pntX7, pntX8])
  ypnts = np.array([pntY1, pntY2, pntY3, pntY4, pntY5, pntY6, pntY7, pntY8])

  print(" Plot X Points: ", xpnts, "\n", "Plot Y Points: ", ypnts)
  plt.title("Random Graph")
  plt.plot(xpnts, ypnts)
  plt.grid()
  plt.show()