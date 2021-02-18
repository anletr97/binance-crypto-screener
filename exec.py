"""Execute file"""

def run(filename):
    """ Run filename """
    exec(open(filename).read())
