def commaCode(stringList):
  output = ''
  for i in range((len(stringList) - 1)):
    output+= (stringList[i] + ', ')

  output += 'and ' + stringList[-1]
  print(output)

commaCode(['apples', 'bananas', 'tofu', 'cats', 'rats', 'Lucy'])