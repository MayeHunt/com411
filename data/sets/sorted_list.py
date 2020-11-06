def observed():
  observations = [] 
  for x in range(5):
    print("Enter an observation:")
    observation = input() 
    observations.append(observation)
  return observations

def removeObservations(observations):
  print("Would you like to remove observations (yes/no)?")
  yesNo = input() 
  if yesNo == 'yes':
    print("Enter an observation to be removed:")
    remove = input() 
    observations.remove(remove) 
  else:
    return 

def run():
  observations = observed() 
  removeObservations(observations)
  observationSet = set()

  for x in observations:
    observationSet.add((x, observations.count(x)))

  print(observationSet)
run()