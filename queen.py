def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    #up
    up = r_q + 1
    while up < n and [up,c_q] not in obstacles:
        count += 1
        up += 1
    #down 
    down = r_q -1
    while down > 0 and [down,c_q] not in obstacles:
        count += 1
        down -= 1
    #left 
    left = c_q - 1
    while left > 0 and [r_q, left] not in obstacles:
        count += 1
        left -= 1
    #right
    right = c_q + 1
    while right < n and [r_q, right] not in obstacles:
        count += 1
        right += 1
    #top right
    r_row, r_col = r_q +1, c_q +1
    while r_row < n and r_col < n and [r_row, r_col] not in obstacles:
        count +=1
        r_row +=1
        r_col +=1
    #bottom left
    l_row, l_col = r_q -1, c_q -1
    while l_row > 0 and l_col >0  and [l_row, l_col] not in obstacles:
        count +=1
        l_row -=1
        l_col -=1
    #top left
    tl_row, tl_col = r_q +1, c_q -1
    while tl_row < n and tl_col >0 and [tl_row, tl_col] not in obstacles:
        count +=1
        tl_row +=1
        tl_col -=1
    #bottom right
    br_row, br_col = r_q -1, c_q +1
    while br_row >0 and br_col < n and [br_row, br_col] not in obstacles:
        count +=1
        br_row -=1
        br_col +=1

    return count

def main():
    n = 5
    k = 3
    queen = [4,3]
    obstacles = [[5,5],[4,2],[2,3]]
    print(queensAttack(n,k,queen[0],queen[1],obstacles))

main()