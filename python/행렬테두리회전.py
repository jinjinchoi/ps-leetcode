def solution(rows, columns, queries):
    answer = []
    matrix =  [ [1 + j + i*columns for j in range(columns)] for i in range(rows)]
    
    for query in queries:
         answer.append(rotate(matrix, query))
    return answer

def rotate(matrix, query):
    x1, y1, x2, y2 = [e-1 for e in query]
    left_top = matrix[x1][y1]
    _min = left_top
    
    for x in range(x1, x2):
        _moved = matrix[x+1][y1]
        _min = min(_moved, _min)
        matrix[x][y1] = _moved
    for y in range(y1, y2):
        _moved = matrix[x2][y+1]
        _min = min(_moved, _min)
        matrix[x2][y] = _moved
    for x in range(x2, x1, -1):
        _moved = matrix[x-1][y2]
        _min = min(_moved, _min)
        matrix[x][y2] = _moved  
    for y in range(y2, y1, -1):
        _moved = matrix[x1][y-1]
        _min = min(_moved, _min)
        matrix[x1][y] = _moved
    matrix[x1][y1+1] = left_top
    return _min
