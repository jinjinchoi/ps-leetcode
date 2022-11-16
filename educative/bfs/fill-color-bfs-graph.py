from typing import List, Tuple

def flood_fill(image: List[List[int]], start: Tuple[int, int], replacement_color: int) -> None:
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    from collections import deque

    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] = replacement_color # replace root color
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement_color # replace color
                queue.append(neighbor)
                visited[r][c] = True

    bfs(start)

#Driver code
inputs =  ["2 2","1 1"]
inputs1 = ["9", "9"]
inputs2 = ["5", "4"]
inputs3 = [
    ["0 1 3 4 1","3 8 8 3 3","6 7 8 8 3","12 2 8 9 1","12 3 1 3 2"],
    ["0 1 6 4","2 3 3 5","3 3 3 3","6 4 3 4"]
]
expected_outputs = [
    ["0 1 3 4 1","3 9 9 3 3","6 7 9 9 3","12 2 9 9 1","12 3 1 3 2"],
    ["0 1 6 4","2 9 9 5","9 9 9 9","6 4 9 4"]
]
for i in range(len(inputs)):
    start = tuple(int(x) for x in inputs[i].split())
    color = int(inputs1[i])
    image = [];
    for j in range(int(inputs2[i])):
        image.append([int(x) for x in inputs3[i][j].split()])
    flood_fill(image, start, color);
    actual_output =[]
    for row in image:
        actual_output.append(' '.join(str(x) for x in row))
    print("Flood fill : ",actual_output)
