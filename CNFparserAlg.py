import random
filename = input("enter the name of your file: ")
f = open(filename+'.txt')
line = 'empty'

'''
variable for counting how many expressions there are
'''
expressions = 0
'''
array for holding arrays that contain all the clauses in an expression
'''
clauseList = []
'''
array for holding count of how many clauses are in each array
'''
clauseCount = []
'''
array for holding arrays that contain all the literal types in an expression
'''
literalList = []
'''
array for holding count of how many literal types there are
'''
literalCount = []
'''
array for holding arrays that contain the base values of all the literal types in an expression
'''
literalValues = []
'''
array for holding arrays that contain the yield values of all the literals in the clauses
'''
literalYields = []
'''
array for holding arrays that contain the yield values of all clauses in an expression
'''
clauseYields = []

