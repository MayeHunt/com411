import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

boxes = []

def init():
    global boxes
    small = {'x':[3, 3, 4, 4, 3],'y':[4, 3, 3, 4, 4]}
    medium = {'x':[2, 2, 5, 5, 2],'y':[5, 2, 2, 5, 5]}
    large = {'x':[1, 1, 6, 6, 1],'y':[6, 1, 1, 6, 6]}
    boxes.append(small) 
    boxes.append(medium) 
    boxes.append(large) 


def animate(frame): 
  global ax  
  global boxes
  ax.set_xlim(0, 7)
  ax.set_ylim(0, 7)
  index = frame % 3
  ax.plot(boxes[index]['x'],boxes[index]['y'], '-') 

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames = 3, interval = 1000,init_func = init)
  plt.show() 

run()