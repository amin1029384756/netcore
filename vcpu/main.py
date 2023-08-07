import re
varpattern = re.compile("[A-Za-z0-9]+")
file1 = open('main.peercore', 'r')
Lines = file1.readlines()
for line in Lines:
    print(line)
    if varpattern.fullmatch(line.split()[0]) :
        ast = open('main.ast', 'a')
        ast.write(f'func {line.split()[0]} args ' + line.replace(line.split()[0], "") + "\n")