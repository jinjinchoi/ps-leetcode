from collections import deque
path_lengths = []
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    
    coords = [ [-1]*51*2 for i in range(51*2)]
    visited = [ [False]*51*2 for i in range(51*2)]
    
    # 내부에 있는 애들 
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for i in range(x1*2,x2*2+1):
            for j in range(y1*2, y2*2+1):
                if x1*2 < i < x2*2 and y1*2 < j < y2*2:
                    coords[i][j] = 1
                elif coords[i][j] != 1:
                    coords[i][j] = 0
    dx, dy = [-1, 1, 0, 0],[0, 0, 1, -1]
    

        
    def dfs(startX, startY, visited, coords, path_length):
        # print("({}, {}) visited!".format(startX, startY))
        if startX==itemX*2 and startY==itemY*2:
            path_lengths.append(path_length//2)
            # print("Destination Reached: path_length {}".format(path_length))
            return
        for k in range(4):
            next_x = startX+dx[k]
            next_y = startY+dy[k]

            if coords[next_x][next_y]==0 and visited[next_x][next_y] == False:
                visited[next_x][next_y] = True
                dfs(next_x, next_y, visited, coords, path_length+1)
                visited[next_x][next_y] = False
    visited[characterX*2][characterY*2] = True
    dfs(characterX*2, characterY*2, visited, coords, 0)
    
    # print(path_lengths)
    return min(path_lengths)
