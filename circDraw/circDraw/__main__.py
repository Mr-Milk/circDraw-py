#from .draw import circDraw
import argparse
from .draw import circDraw
from .version import __version__

def main():
    backsplice, title, modification = None, None, None
    parser = argparse.ArgumentParser(description="Commmand Line Tool for visulizing circle RNA.")
    # version
    parser.add_argument("-v", "--version", action="store_true", help="Version of the package")
    parser.add_argument("-b", "--backsplice", help="Filename for drawing backsplicing site for circle RNA")
    parser.add_argument("-t", "--title", help="Title you want to ")
    parser.add_argument("-m", "--modification", help="Filename for drawing modication site on circle RNA")
    args = parser.parse_args()
    
    dict_args = vars(args)
    if not any(list(dict_args.values())):
        exit("Welcome to use circDraw (" + __version__ + ")!")
    elif args.version:
        exit("Version: " +  __version__)
    else:
        exit("Please perform drawing inside python3 to gain the best usage experience!")

if __name__ == '__main__':
    main()
   



