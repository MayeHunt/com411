import matplotlib.pyplot as plt   
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
    
def animate(frame): 
  global ax  
  ax.cla()
  ax.set_xlim(0, 10)
  ax.set_ylim(-1, 1)
  x = np.arange(0, 10,0.01)
  y = np.sin(x + frame)
  ax.plot(x,y) 

def run():
  global fig
  simple_animation = animation.FuncAnimation(fig, animate, frames = 720, interval = 100)
  plt.show() 

run() 