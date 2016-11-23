import sys

if not sys.argv[1:]:
	print('Cara menggunakananya : python %s /etc/hosts' % sys.argv[0])
	sys.exit()

filename = sys.argv[1]
f = open(filename)
print f.read()
f.close()
