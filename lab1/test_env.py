import sys

def get_keys():
    keys = {}
    for a in sys.argv:
        temp = a.split('=', maxsplit=1)
        if (len(temp) > 1):
            keys[temp[0]] = temp[1]

    if (keys.get('--file') is not None):
        file = open(keys['--file'], 'r')
        for line in file:
            line = line.rstrip()
            temp = line.split('=', maxsplit=1)
            keys[temp[0]] = temp[1]
    return keys