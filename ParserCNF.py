f = open('butz.txt')
line = 'empty'
i = 0
while(line != ''):
    character = 'empty'
    i += 1
    while(character != ''):
        character = f.readline(1)
        print character
    f.seek(1)
    line = f.readline()
    print line
