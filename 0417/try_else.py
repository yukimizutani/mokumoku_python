filename = input()
try:
    f = open(filename, 'r')
except OSError:
    print('cannot open', filename)
else:
    print(filename, 'has', len(f.readline()), 'lines')
    f.close()
