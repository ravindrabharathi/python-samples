def displayPathtoPrincess(n, grid):
    for i in range(n):
        for j in range(m):
            if (grid[i][j]=='p'):
                p_pos=(i,j)
            elif (grid[i][j]=='m'):
                bot_pos=(i,j)



    #print('princess is at '+str(p_pos))
    #print('bot is at '+ str(bot_pos))
    v_travel=p_pos[0]-bot_pos[0]
    h_travel=p_pos[1]-bot_pos[1]
    #print(h_travel,v_travel)
    if (v_travel>0):
        print('DOWN' * abs(v_travel))
    elif (v_travel<0):
        print('UP' * abs(v_travel))

    if (h_travel>0):
        print('RIGHT' * abs(h_travel))
    elif (h_travel<0):
        print('LEFT' * abs(h_travel))





# print all the moves here

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)