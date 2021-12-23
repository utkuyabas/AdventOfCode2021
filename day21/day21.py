import sys

MAX_DICE = 100
MAX_SCORE = 1000

def solve(all_lines):
    x_start, y_start = parse_file(all_lines)
    print(x_start, ", " , y_start)
    total_dice = 0
    the_end = False
    x_score, y_score = 0,0
    next_dice = 1
    def total_movement(dice):
        nonlocal total_dice
        total = 0
        for i in range(3):
            total_dice += 1
            if dice  > MAX_DICE:
                dice = 1
            print("dice ", dice)
            total += dice
            dice += 1
        print("total_mov: ", total)
        return total, dice
    while True:
        movement, next_dice  = total_movement(next_dice)
        x_start = ((x_start + movement) - 1 ) % 10 + 1
        x_score += x_start
        print("XScore: ", x_score," XPos: ", x_start)
        if  x_score >= MAX_SCORE:
            print("Total dice: ", total_dice)
            return total_dice * y_score
        movement, next_dice  = total_movement(next_dice)
        y_start = ((y_start + movement) - 1 ) % 10 + 1
        y_score += y_start
        print("YScore: ", y_score," YPos: ", y_start)
        if  y_score >= MAX_SCORE:
            print("Total dice: ", total_dice)
            return total_dice * x_score

        
       

        

def parse_file(lines):
    assert len(lines) == 2
    return int(lines[0].split(":")[1]), int(lines[1].split(":")[1])


if __name__ == "__main__":
    all_lines = []
    for line in sys.stdin:
        all_lines.append(line.strip())
    print(solve(all_lines))
