import sys

def solve(all_lines):
    x, y = 0,0
    aim = 0
    for line in all_lines:
        command, value = line.strip().split(" ")
        value = int(value)
        if command == "forward":
            x += value
            y += (aim * value)
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
    return x*y


if __name__ == "__main__":
    all_lines = []
    for line in sys.stdin:
        all_lines.append(line.strip())

    print(solve(all_lines))
