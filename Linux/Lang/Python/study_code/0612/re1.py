import fileinput, re
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)
