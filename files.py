'''
file = open("filename.txt", "r")

outfile = ""

for line in range(1,11):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("filename.txt", "w")
file.write(outfile)
file.close()
'''

file = open("teams.txt", "r")
lines = ""

for line in range(1,11):
    if line == 1:
        lines += file.readline()
    if line == 4:
        lines += file.readline()
print(lines)


file.close()