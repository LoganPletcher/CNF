f = open('butz.txt')
line = 'empty'

expressionList = []
literalList = []
literalCount = []
clauseCount = []

while (line != ''):
    line = f.readline()
    for i in line:
        print i
    '''
    if (line[0] == '('
        and line[len(line)-1] == ')'):
        print line
'''
