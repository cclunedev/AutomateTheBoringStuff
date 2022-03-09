def printTable(tableData):
  colWidths = [0] * len(tableData)

  for i in range(len(tableData)):
    maxLength = 0
    for item in tableData[i]:
      if len(item) > maxLength:
        maxLength = len(item)
    colWidths[i] = maxLength

  for i in range(len(tableData[0])):
    output = ''
    for j in range(len(tableData)):
      output += tableData[j][i].rjust(colWidths[j]) + ' '
    print(output)


tableDataOne = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose'],
                ['Lucy', 'Gunnar', 'Lola', 'Mando']]

printTable(tableDataOne)