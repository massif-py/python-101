#! python3

colWidths = []
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOfLists):
    global colWidths
    for i in range(3):
        for j in range(4):
            colWidths += [len(tableData[i][j])]

printTable(tableData)
                       
    
