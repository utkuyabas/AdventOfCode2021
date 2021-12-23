import sys
from typing import Counter

def solve(input):
    prev = input[0]
    count = 0
    for i in range(1,len(input)):
        line = input[i]
        if line > prev:
            count += 1
        prev = line
    return count
        




if __name__ == "__main__":
    all_lines = []
    for line in sys.stdin:
        all_lines.append(line.strip())
    print(solve(all_lines))