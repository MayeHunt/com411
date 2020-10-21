def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return (min(likelihoods),max(likelihoods))

def run():
  fall = likelihood() 
  print("Minimum likelihood of falling: {}%\nMaximum likelihood of falling: {}%".format(fall[0],fall[1]))

run() 