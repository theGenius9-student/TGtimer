import random as r
possibleMoves=["R", "R'", "U", "U'", "F", "F'", "D", "D'" "L", "L'", "B", "B'"]
scram = possibleMoves[r.randint(0, len(possibleMoves) - 1)]
timeList = []
numMoves = int(input("Input the number of moves you want your scramble to be. "))
  for i in range(5): 
      for i in range(numMoves - 1): 
        scram += " " + possibleMoves[r.randint(0, len(possibleMoves) - 1)]
      print(scram)
      time = float(input("input your time. "))
      timeList.append(time)
      scram = ""
  ao5 = round(sum(timeList) / len(timeList), 2)
  print("your ao5 is", ao5)
