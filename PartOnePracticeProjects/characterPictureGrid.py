def characterPictureGrid(gridList):
  
  for i in range(len(gridList[0])):
    outLine = ''
    
    for j in range(len(gridList)):
      outLine += gridList[j][i]

    print(outLine)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],      
        ['0', '0', '0', '0', '0', '.'], 
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

characterPictureGrid(grid)