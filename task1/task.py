import csv
from typing import Tuple
import argparse


def f(file: str, coordinate: Tuple[int, int]):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return list(reader)[coordinate[0]][coordinate[0] - 1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('-p', type=str)
    p.add_argument('-r', type=int)
    p.add_argument('-c', type=int)

    args = p.parse_args()

    print(f(args.p, (args.r, args.c)))
    
if __name__ == '__main__':
    main()