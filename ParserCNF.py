class CNF:
    def __init__(self, string):
        temp = ''
        crClause = False #Boolean to determine if a clause is being made
        for x in string:
            if(x == '('):
                temp = x
                crClause = True
                self.clauseCount += 1
            elif(crClause):
                temp += x
            if(x.isalpha()):
                if x not in self.literals:
                    self.literals.append(x)
                    self.literalCount += 1
            if(x == ')'):
                crClause = False
                self.clauses.append(temp)
        for x in range(0,len(self.clauses)):
            if(x != 0):
                self.expression += '^'
            self.expression += self.clauses[x]
        
    expression = ''
    clauses = []
    literals = []
    literalCount = 0
    clauseCount = 0

import random
filename = input("enter the name of your file: ")
f = open(filename+'.txt')
line = "empty"
while(line != ''):
    line = f.readline()
    cnf = CNF(line)
    print(cnf.expression)
    print(cnf.clauseCount)
    print(cnf.literalCount)
