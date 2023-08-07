sar = open('gen.py', 'r')
lines = sar.readlines()
initt = []
for line in lines:
    initt.append("    " + line)
sar = open('gen.py', 'w')
sar.writelines(initt)