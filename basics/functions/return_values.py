def run():
  def sum_weights(beep_weight,bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

  def calc_avg_weight(beep_weight,bop_weight):
    avg_weight = sum_weights(beep_weight,bop_weight) / 2
    return avg_weight

  def runpls():
    print("Enter the weight for Beep:")
    beep_weight = int(input())
    print("Enter a weight for Bop:")
    bop_weight = int(input())
    print("Would you like to find the sum, or the average?")
    decision = input() 
    if(decision == 'sum'):
      print(sum_weights(beep_weight,bop_weight))
    elif(decision == 'average'):
      print(calc_avg_weight(beep_weight,bop_weight))
    else:
      ("Enter sum or average.")

  runpls() 