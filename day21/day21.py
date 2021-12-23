import sys

MAX_DICE = 100
MAX_SCORE = 1000
TARGET = 5

def solve_2(all_lines):
    x_start, y_start = parse_file(all_lines)
    x_score, y_score = 0,0
    scores = {}
    possibilities = {3:1, 4:3, 5:3, 6:6, 7:3, 8:3, 9:1}
    cache_hits = 0
    def solve_inner(x,y, is_x, x_score, y_score):
        nonlocal cache_hits
        nonlocal scores
        print("solve_inner(",x,",",y,",",is_x,",",x_score, ",",y_score,"):  ")
        if not is_x and x_score >= TARGET:
            print("x Win")
            return (1,0)

        if is_x and y_score >= TARGET:
            print("y win")
            return (0,1)

        if (x,y,is_x, x_score, y_score) in scores:
            cache_hits += 1
            return scores[(x,y,is_x,x_score, y_score)]

        x_total_win, y_total_win = 0, 0

        for pos, num in possibilities.items():
            x_score_t, y_score_t = 0, 0
            new_x, new_y = x, y
            if is_x:
                new_x = normalize_pos(x + pos)
                x_score_t = new_x
            else:
                new_y= normalize_pos(y + pos)
                y_score_t = new_y
            x_temp, y_temp = solve_inner(new_x, new_y, not is_x, x_score + x_score_t, y_score + y_score_t)
            x_total_win += (num * x_temp)
            y_total_win += (num * y_temp)
        print("Back in ","solve_inner(",x,",",y,",",is_x,",",x_score, ",",y_score,")")
        print("Totals: ", x_total_win,", ",y_total_win)

        scores[(x,y,is_x, x_score, y_score)] = (x_total_win, y_total_win)
        scores[(y,x, not is_x, y_score, x_score)] = (y_total_win, x_total_win)
        #print(scores)
        return (x_total_win,y_total_win)

    xlast, ylast = solve_inner(x_start, y_start, True, 0, 0)
    print(cache_hits)
    return max(xlast, ylast)


def normalize_pos(pos):
    return ((pos) - 1 ) % 10 + 1

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
    print(solve_2(all_lines))
