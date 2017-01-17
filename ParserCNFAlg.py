import random
filename = input("enter the name of your file: ")
f = open(filename+'.txt')
line = 'empty'

literalList = []
literalCount = []
clauseCount = []
expressionList = 0
valueList = []
while (line != ''):
    line = f.readline()
    expressionList += line.count('\n')
print("Number of Expressions", expressionList)
f.seek(0)
for i in range (0, expressionList):
    print("-------------------------------------------------")
    newLiterals = []
    literalList.append(newLiterals)
    tempClause = 0
    line = f.readline()
    tempClause = line.count('(')
    clauseCount.append(tempClause)
    print(line, "\nNumber of Clauses", clauseCount[i])
    tempLiteral = 0
    for x in line:
        if(x.isalpha()):
            if not(x in literalList[i]):
                literalList[i].append(x)
                tempLiteral += 1
    literalCount.append(tempLiteral)
    print("List of Literals:", literalList[i])
    print("Number of Literals", literalCount[i])
    literalValues = []
    for y in range (0, literalCount[i]):
        literalValues.append(random.randrange(0,2))
    valueList.append(literalValues)
    print("List of Literal Values:", valueList[i])
    finalValue = False
    trueValues = []
    trueValues2 = []
    for x in range (0,len(line)):
        if(line[x].isalpha()):
            k = 0
            for j in literalList[i]:
                if line[x] == j:
                    tempValue = valueList[i][k]
                    if line[x-1] == '!':
                        if tempValue == 1:
                            tempValue = 0
                        elif tempValue == 0:
                            tempValue = 1
                    trueValues.append(tempValue)
                if line[x-2] == '|':
                    
                k += 1
    i += 1
print("-------------------------------------------------")
