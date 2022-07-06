import sys, getopt


def main(argv):

    # default algorithm:
    algorithm = 1

    # parse command line options:
    try:
       opts, args = getopt.getopt(argv,"hr:l",["runtime=","live="])
    except getopt.GetoptError:
       print("Error")
       sys.exit(2)

    for opt, arg in opts:
       print(opt)
       print(arg)
       if opt == "-h":
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
       elif opt in ("-l", "--live"):
         print("live")
       elif opt in ("-r", "--runtime"):
          # use alternative algorithm:
          algorithm = arg

    print("Using algorithm: ", algorithm)

    # Positional command line arguments (i.e. non optional ones) are
    # still available via 'args':
    print("Positional args: ", args)

if __name__ == "__main__":
   main(sys.argv[1:])