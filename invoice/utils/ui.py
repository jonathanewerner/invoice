import sys

def err(msg):
    print('Error: {}'.format(msg), file=sys.stderr)
    sys.exit(1)

