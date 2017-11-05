import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=str, default = 'trundle',
                        help="What is the troll?")
    args = parser.parse_args()
    sys.stdout.write(str(troll(args)))
    

def troll(args):
    if args.x == 'trundle':
        print('im the troll king, king!')

    elif args.x == 'trolol':
        print('trololooolololololol')

    elif args.x == 'troller':
        print('9x rpt dis troller hehexd')

if __name__ == "__main__":
    main()
