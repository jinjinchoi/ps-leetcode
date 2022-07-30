from collections import deque, defaultdict
def solution(maps):
    h = len(maps)
    w = len(maps[0])
    dx,dy= [1,-1,0,0],[0,0,1,-1]
    path_dict = defaultdict(int)
    def bfs(v,):

        Q = deque([])
        Q.append(v)
        x, y = v
        visited = [ [False]*w for i in range(h)]
        # print("x:{}, y:{}".format(x,y))
        visited[x][y] = True
        path_dict[(x,y)] = 1

        path_length = 0
        while Q:
            x, y = Q.popleft()
            
            # print("x:{}, y:{}".format(x, y))
            for i in range(4):
                new_x = x+dx[i]
                new_y = y+dy[i]
                # print("LOOKING ON new_x:{}, new_y:{}".format(new_x, new_y))
                if h>new_x >= 0 and w>new_y >= 0 and maps[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    # print("REACHED new_x:{}, new_y:{}".format(new_x, new_y))
                    Q.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    path_dict[(new_x,new_y)] = path_dict[(x,y)] + 1
                    if new_x == (h-1) and new_y == (w-1):
                        return path_dict[(new_x,new_y)]
        return -1
    return bfs((0,0))

