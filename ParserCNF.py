f = open('butz.txt')
line = 'empty'
i = 0
clauseOpen = False
clause = 'empty'
clauseCNT = 0
clauseGroup = 0
expressionCNT = 0
expressionList = []
clauseList = []
literalList = [None]
literalOpen = False
literal = 'empty'
while(line != ''):
    line = f.readline()
    if '\n' in line:
        expressionCNT += 1
f.seek(0)
line = 'empty'
while(line != ''):
    line = f.readline(1)
    if(line == '('):
        clauseCNT += 1
    if(line == '\n'):
        clauseGroup += 1
        clauseCNT = 0
if(clauseCNT > 0):
    clauseGroup += 1
    clauseCNT = 0

f.seek(0)
line = 'empty'
for x in range(0, clauseGroup):
    newList = []
    clauseList.append(newList)
print clauseList

for i in range(0, expressionCNT + 1):
    line = f.readline()
    expressionList.append(line)
line = 'empty'
f.seek(0)
j = 0
for expression in expressionList:
    for character in expression:
        if (character == '('):
            clause = character
            clauseOpen = True
        elif (clauseOpen):
            clause += character
            if(character == ')'):
                print j
                clauseList[j].append(clause)
                clause = 'empty'
                clauseOpen = False
        if (character != '(' and
            character != ')' and
            character != '!' and
            character != 'V' and
            character != '^' and
            literalOpen == False):
            literal = character
            literalOpen = True
        elif (character != '(' and
            character != ')' and
            character != '!' and
            character != 'V' and
            character != '^' and
            literalOpen == True):
            literal += character
        else:
            lite
    j += 1
for clauses in clauseList:
    print clauses


'''
while(line != ''):
    line = f.readline(1)
    if (line == '('):
        clause = line
        clauseOpen = True
    if(clauseOpen):
        clause += line
        if(line == ')'):
            clause = 'empty'
            clauseCNT += 1
            clauseOpen = False
'''
#print clauseCNT
