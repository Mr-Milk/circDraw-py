#from .draw import circDraw
import argparse
from .draw import circDraw

def main():
    parser = argparse.ArgumentParser(description="Commmand Line Tool for visulizing circle RNA.")
    parser.add_argument("-b", "--backsplice", help="Filename for drawing backsplicing site for circle RNA")
    parser.add_argument("-t", "--title", help="Title you want to ")
    parser.add_argument("-m", "--modification", help="Filename for drawing modication site on circle RNA")


if __name__ == '__main__':
    main()



