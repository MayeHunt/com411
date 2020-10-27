def observed():
  observations = []
  for x in range(7):
    print("Please enter an observation:")
    observation = input()
    observations.append(observation)
  return observations

def run():
  print("Counting observations...")
  observations = observed()
  observations_set = set()

  for x in observations:
    observations_set.add((x, observations.count(x)))

  print(observations_set)

run()