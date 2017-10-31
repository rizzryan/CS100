f = open('cs100.txt', 'r')
f2 = open('cs100copy.txt', 'w')

f2.write(f.read())

f.close()
f2.close()
