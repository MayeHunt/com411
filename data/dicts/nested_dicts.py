def shortPattern(): 
  pattern = {"sequence":"101","occurrences":5} 
  return pattern

def mediumPattern():
  pattern = {"sequence":"111000","occurrences":25}
  return pattern

def longPattern():
  pattern = {"sequence":"1100110011001100","occurrences":50}
  return pattern

def run():
  print("Analysing patterns...")
  patterns = {"short sequence":shortPattern(),"medium sequence":mediumPattern(),"long sequence":longPattern()}
  print(patterns)

run()