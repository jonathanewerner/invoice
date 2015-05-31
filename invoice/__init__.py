import invoice.core.app
import sys

def run():
    args = sys.argv[1:]
    invoice.core.app.run(args)
