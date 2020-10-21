def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)

def run():
  fall = likelihood() 
  print("Minimum likelihood of falling: {}%".format(fall))

run() 