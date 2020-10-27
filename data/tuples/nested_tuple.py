def steps():
  likelihoods = [("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)]
  return likelihoods

def run():
  step = steps()
  good_steps = []
  bad_steps = []
  for x in range(len(step)):
    if step[x][1] >= 50:
      bad_steps.append(step[x])
    else:
      good_steps.append(step[x])
  print("Good steps: {}, Bad steps: {}".format(len(good_steps),len(bad_steps)))
run()
