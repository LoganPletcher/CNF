filename = input("enter the name of your file: ")
f = open(filename+'.txt')
line = 'empty'

literalList = []
literalCount = []
clauseCount = []
expressionList = 0
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
    i += 1
print("-------------------------------------------------")
